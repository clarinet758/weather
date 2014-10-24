#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime
import json
import oat
import time
import urllib2


class Weather:
    day = [u'今日', u'明日']

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_weather(self):
        ep = "http://weather.livedoor.com/forecast/webservice/json/v1?city="
        t = urllib2.urlopen(ep+self.code)
        f = json.load(t)
        x = datetime.datetime.now()
        dt = 0
        if x.hour % 2:
            dt = 1
        base = f['forecasts'][dt]
        telop = base['telop']
        if dt:
            tem_max = str(base['temperature']['max']['celsius'])
            tem_min = str(base['temperature']['min']['celsius'])
        else:
            tem_max = str(base['temperature']['max'])
            tem_min = str(base['temperature']['min'])
        message = u"%sの%sら辺の天候は%sで気温は最高%s度くらいで最低が%s度くらい" % (self.day[dt], self.name, telop, tem_max, tem_min)
        message = message.encode('utf-8')
        oat.tweet(message)


place = [Weather(u'千葉県北西部', '120010'),
         Weather(u'東京都23区', '130010'),
         Weather(u'熊本県熊本', '430010'),
         Weather(u'京都府舞鶴', '260020')]


def test(places):
    for p in places:
        p.get_weather()
        time.sleep(5)

test(place)
