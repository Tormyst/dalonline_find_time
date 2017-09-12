# coding: utf-8
from termcolor import colored, COLORS, HIGHLIGHTS
from sys import argv
from re import compile as re


TIME_START = 8
TIME_END = 20
COLOR_LIST = list(COLORS)
COLOR_LIST.remove('grey')
HIGHLIGHT_LIST = list(HIGHLIGHTS)
HIGHLIGHT_LIST.remove('on_grey')

argc = len(argv)
if argc <= 1:
    print('Usage file [classes...]')
    exit(-1)
elif argc == 2:
    title_print = True
    timetable = False
else:
    title_print = False
    timetable = True

class_info = True

title = re('^CSCI (\d*) (.*)$')
classes = argv[2:]
if len(classes) > 5:
    print('TOO many classes right now fix me')
    exit(-1)

times = [[] for _ in classes]

curr_num = ''
curr_title = ''
selected = -1

with open(argv[1], 'r') as in_file:
    for line in in_file:
        match = title.match(line)
        if match:
            curr_num = match.group(1)
            curr_title = match.group(2)
            if title_print:
                print('{} {}'.format(curr_num, curr_title))

            if curr_num in classes:
                selected = classes.index(curr_num)
            else:
                selected = -1
        elif selected >= 0:
            data = line.split(',')
            if len(data) == 8:
                times[selected].append({
                    'type': data[0],
                    'days': [d != ' ' for d in data[1:6]],
                    'time': [int(i) for i in data[6].split('-')],
                    'location': data[7]
                })


if timetable:
    print('      Mon    Tue    Wed    Thu    Fri ')
    for time in range(TIME_START, TIME_END):
        for minutes in [0, 30]:
            t = (time*100) + minutes
            to_print = '{:2}:{:02}:'.format(time,minutes)
            for weekday in range(5):
                for class_int in range(len(classes)):
                    """
                    list(map(lambda x: print('{} {} {}, t={}, weekday={}'.format(
                                    x['days'][weekday]
                                   ,x['time'][0] - 5
                                   ,x['time'][1] + 5,t,weekday)),
                               times[class_int]))
                    """

                    if any(map(lambda x: x['days'][weekday]
                                   and (x['time'][0] - 5) <= t
                                   and (x['time'][1] + 5) >= t,
                               times[class_int])):
                        to_print += colored(' ', COLOR_LIST[class_int],
                                        HIGHLIGHT_LIST[class_int])
                    else:
                        to_print += ' '
                to_print += (' '*(7 - len(classes)))
            print(to_print)
