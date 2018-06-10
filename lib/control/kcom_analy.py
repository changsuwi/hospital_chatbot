# coding=utf-8
from __future__ import print_function

# import pandas as pd
import jieba

import jieba.posseg as pseg
jieba.set_dictionary('jieba/dict.txt')

jieba.load_userdict('userdict/symptom.txt')
jieba.load_userdict('userdict/time.txt')
jieba.load_userdict('userdict/position.txt')
jieba.load_userdict('userdict/others.txt')
jieba.initialize()
import re
from collections import defaultdict
import matplotlib.pyplot as plt

import time as timer


def kcom_analy(kcom_str):
    start_time = timer.time()
    max_length = 0
    split = kcom_str.replace("有", "")
    split = split.replace("會", "")
    split = split.split()

    t_now = 0
    m = 0
    pre_time = list()
    event_w = list()
    event_now = list()

    for s in split:
        t_w = list()
        sym_w = list()
        pos_w = list()

        last_t = 0
        last_n = 0
        last_f = 0
        last_sym = 0
        t = 0
        sym = 0

        line = pseg.cut(s, HMM=False)
        for k, f in line:
            print('%s %s' % (k, f), end=' ')

            if f == 't':
                last_n = 0
                last_sym = 0
                last_f = 0
                if t_now == 0:
                    if sym == 1:
                        event = dict()
                        event['time'] = t_w
                        event['sym'] = sym_w
                        event_w.append(event)
                        t_w = list()
                        sym_w = list()
                        pos_w = list()
                        sym = 0
                        t_w.append(k)
                        last_t = 1
                        t = 1
                    elif last_t == 1 and t == 1:
                        t_w.append(k)
                        last_t = 1
                        t = 1
                    elif t == 0:
                        t_w.append(k)
                        last_t = 1
                        t = 1

            elif f == 'tnow' or f == 'tg':
                last_n = 0
                last_t = 0
                last_sym = 0
                last_f = 0
                t_now = 1
                if sym == 1:
                    event = dict()
                    event['time'] = t_w
                    event['sym'] = sym_w
                    event_w.append(event)
                    t_w = list()
                    sym_w = list()
                    pos_w = list()
                    sym = 0

            elif f == 'sym':
                if last_n == 1:
                    for p in pos_w:
                        sym_w.append(p + k)
                    pos_w = list()
                else:
                    sym_w.append(k)

                last_n = 0
                last_t = 0
                last_sym = 1
                last_f = 0
                sym = 1

            elif f == 'f':
                last_f = 1
                last_sym = 0
                last_n = 0
                last_t = 0
                n = k
            elif f == 'pos':
                if last_f == 1:
                    n = n + k
                    pos_w.append(n)
                elif last_n == 1:
                    pos_w.append(k)
                else:
                    n = k
                    pos_w.append(n)

                last_n = 1
                last_sym = 0
                last_f = 0
                last_t = 0
            elif f == 'm' and last_sym == 1:
                last_t = 0
                last_f = 0
                last_n = 0
                last_sym = 0
                if len(t_w) == 0:
                    t_w.append(k)
                    m = 1
                    last_t = 1

            else:
                last_f = 0
                last_t = 0
                last_n = 0
                last_sym = 0

        if len(sym_w) > 0:
            if t_now == 1:
                event_now += sym_w
            else:
                event = dict()
                if len(t_w) == 0:
                    event['time'] = pre_time
                else:
                    event['time'] = t_w
                event['sym'] = sym_w
                event_w.append(event)
        elif len(t_w) > 0:
            pre_time = t_w

    total = list()

    time = ''
    for e in event_w:
        event = dict()
        # print(e)
        if len(e['time']) > 0:
            time = ''.join(e['time'])
        event['time'] = time
        event['sym'] = e['sym']

        total.append(event)

    if m == 1:
        m_t = ''
        for idx, e in reversed(list(enumerate(total))):
            if len(e['time']) > 0:
                m_t = e['time']
            else:
                e['time'] = m_t

    for idx, e in reversed(list(enumerate(total))):
        if idx != 0:
            if e['time'] == total[idx - 1]['time']:
                # print(e)
                total[idx - 1]['sym'] += e['sym']
                del total[idx]

    if len(event_now) > 0:
        total.append({'time': '現在', 'sym': event_now})
        # for e_now in event_now:
        #total.append({'time': '現在', 'sym': [e_now]})

    print('%s' % kcom_str)
    for period in total:
        print('時間： %s' % period['time'].encode('utf-8'))
        print('症狀： %s' % ','.join(period['sym']).encode('utf-8'))
    print('\n')
    return total
