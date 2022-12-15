"""Advent of Code Day 15"""
import re
from scipy.spatial import distance


def read_input():
    '''read coordinates of sensors and beacons'''
    with open("input.txt", encoding="utf-8") as file:
        return [{'sensor': (coords:=[*map(int, re.findall(r"\d+", line))])[:2], 'beacon': coords[2:]} for line in file.readlines()]


if __name__ == "__main__":
    Y_COORD = 2000000
    s_b = read_input()
    s_m = [{'sensor': x['sensor'], 'dist': distance.cityblock(x['sensor'], x['beacon'])} for x in s_b]

    # part one
    s_f = [*filter(lambda x: distance.cityblock(x['sensor'], [x['sensor'][0], Y_COORD]) <= x['dist'], s_m)]
    points = set()
    for line in s_f:
        dist_to_line = distance.cityblock(line['sensor'], [line['sensor'][0], Y_COORD])
        for x_coord in range(line['sensor'][0] - line['dist'] + dist_to_line, line['sensor'][0] + line['dist'] - dist_to_line):
            points.add((x_coord, Y_COORD))
    print(len(points))

    # part two
    for y in range(0, 4000001):
        s_f = [*filter(lambda x: abs(x['sensor'][1] - y) <= x['dist'], s_m)]
        line_points = set()
        ranges = []
        for line in s_f:
            dist_to_line = abs(line['sensor'][1] - y)
            start = line['sensor'][0] - line['dist'] + dist_to_line
            end = line['sensor'][0] + line['dist'] - dist_to_line

            start = start if start >= 0 else 0
            end = end if end <= 4000001 else 4000001
            if len(ranges) > 0 and any((r[0] <= start <= r[1]) or (r[0] <= end  <= r[1]) for r in ranges):
                for r in ranges:
                    if r[0] <= start <= r[1]:
                        r[1] = max(r[1], end)
                        break
                    if r[0] <= end <= r[1]:
                        r[0] = min(r[0], start)
                        break
            else:
                ranges.append([start, end])

        s_ranges = sorted(ranges, key=lambda x: x[1])
        if any(0 <= r[1] + 1 <= 4000001 and not any(a[0] <= r[1] + 1 <= a[1] for a in s_ranges if a != r) for r in s_ranges):
            for r in s_ranges:
                x = r[1] + 1
                if 0 <= x <= 4000001 and not any(a[0] <= x <= a[1] for a in s_ranges if a != r):
                    print((x * 4000000) + y)
                    break
            break
