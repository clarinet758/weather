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
http://weather.service.msn.com/data.aspx?src=vista&weadegreetype=C&culture=ja-JP&wealocations=wc:JAXX0013

"""


class Weather:
    day = [u'今日', u'明日']
    key = ['temperature','low','high','skytextday','precip']
    def __init__(self, name, code):
        self.name = name
        self.code = code



    def reg(self,quo):
        sp = quo.split('=')[1]
        sp = sp.replace("\"","")
        return sp


    def tweet(self, message):
        message = message.encode('utf-8')
        print message


    def today(self,w):
        cnt = 0
        for i in w:
            if key[0] in i:
                temp = reg(self,i)
                cnt+=1
            elif key[3] in i:
                sky = reg(self,i)
                cnt+=1
            elif key[4] in i:
                pre = reg(self,i)
                cnt+=1
            if cnt >= 3:
                t = u"%sの%sら辺の天候は%sで気温は%s度くらい 降水確率は%sくらい #%d" % (self.day[0], self.name, sky, temp, pre, x.microsecond)
                tweet(self,t)
                break


    def get_weather(self):
        ep = "http://weather.service.msn.com/data.aspx?src=vista&weadegreetype=C&culture=ja-JP&wealocations=wc:"
        t = urllib2.urlopen(ep+self.code)
        u = t.read()
        v = u.split(' ')
        x = datetime.datetime.now()
        if x.hour % 2:
            today(self,v)
#            pass
        else:
            today(self,v)
#        message = u"%sの%sら辺の天候は%sで気温は最高%s度くらいで最低が%s度くらい #%d" % (self.day[dt], self.name, telop, tem_max, tem_min, x.microsecond)
#        oat.tweet(message)


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
