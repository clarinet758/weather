#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime
import json
import oat
import time
import urllib2

"""
降水確率メモ
http://ism1000ch.hatenablog.com/entry/2014/02/04/033533

xml memo
http://hikm.hatenablog.com/entry/20090206/1233950923
http://weather.service.msn.com/data.aspx?src=vista&weadegreetype=C&culture=ja-JP&wealocations=wc:JAXX0013

"""


class Weather:
    day = [u'今日', u'明日']

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_weather(self):
        ep = "http://weather.service.msn.com/data.aspx?src=vista&weadegreetype=C&culture=ja-JP&wealocations=wc:"
        t = urllib2.urlopen(ep+self.code)
        u = t.read()
        self.v = u.split(' ')

        x = datetime.datetime.now()
        dt = 0
        if x.hour % 2:
            dt = 1
        base = f['forecasts'][dt]
        telop = base['telop']
        if base['temperature']['max']==None:
            tem_max = str(base['temperature']['max'])
        else:
            tem_max = str(base['temperature']['max']['celsius'])
        if base['temperature']['min']==None:
            tem_min = str(base['temperature']['min'])
        else:
            tem_min = str(base['temperature']['min']['celsius'])
        message = u"%sの%sら辺の天候は%sで気温は最高%s度くらいで最低が%s度くらい #%d" % (self.day[dt], self.name, telop, tem_max, tem_min, x.microsecond)
        message = message.encode('utf-8')
        oat.tweet(message)


place = [Weather(u'東京都','JAXX003')]
#         Weather(u'熊本県熊本', '430010'),
#         Weather(u'京都府舞鶴', '260020'),
#         Weather(u'東京都23区', '130010'),
#         Weather(u'千葉県市川', '120010'),
#         Weather(u'宮城県仙台', '040010')]


def test(places):
    for p in places:
        p.get_weather()
        time.sleep(5)

test(place)
