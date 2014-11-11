#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# caution:Creating Middle
import datetime
import oat
import time
import urllib2


class Weather:
    day = [u'今日', u'明日']
    key = ['temperature', 'low', 'high', 'skytextday', 'precip']

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def reg(self, quo):
        sp = quo.split('=')[1]
        sp = sp.replace("\"", "")
        sp = sp.decode('utf-8')
        return sp

    def tweet(self, message):
        message = message.encode('utf-8')
#        print message
        oat.tweet(message)

    def today(self, w):
        cnt = 0
        for i in w:
            if self.key[0] in i:
                temp = self.reg(i)
                cnt += 1
            elif self.key[3] in i:
                sky = self.reg(i)
                cnt += 1
            elif self.key[4] in i:
                pre = self.reg(i)
                cnt += 1
            if cnt >= 3:
                t = u"%sの%sら辺の天候は%sで気温は%s度くらい 降水確率は%s％くらい #%d" % (self.day[0], self.name, sky, temp, pre, self.xms)
                self.tweet(t)
                break

    def tomorrow(self, w):
        cnt = s = p = 0
        for i in w:
            if self.key[1] in i:
                low = self.reg(i)
                if low != '':
                    cnt += 1
            elif self.key[2] in i:
                high = self.reg(i)
                if high != '':
                    cnt += 1
            elif self.key[3] in i and s < 2:
                sky = self.reg(i)
                s += 1
                if s == 2:
                    cnt += 1
            elif self.key[4] in i and p < 2:
                pre = self.reg(i)
                p += 1
                if p == 2:
                    cnt += 1
            if cnt >= 4:
                t = u"%sの%sら辺の天候は%sで気温は最高%s度くらいで最低%s度くらい 降水確率は%s％くらい #%d" % (self.day[1], self.name, sky, high, low, pre, self.xms)
                self.tweet(t)
                break

    def get_weather(self):
        ep = "http://weather.service.msn.com/data.aspx?src=vista&weadegreetype=C&culture=ja-JP&wealocations=wc:"
        t = urllib2.urlopen(ep+self.code)
        u = t.read()
        v = u.split(' ')
        x = datetime.datetime.now()
        self.xms = x.microsecond
        if x.hour % 2:
            self.tomorrow(v)
        else:
            self.today(v)


place = [Weather(u'熊本県', 'JAXX0043'),
         Weather(u'京都府', 'JAXX0047'),
         Weather(u'東京都', 'JAXX0085'),
         Weather(u'宮城県', 'JAXX0104')]


def test(places):
    for p in places:
        p.get_weather()
        time.sleep(5)

test(place)
