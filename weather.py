#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import datetime
import oat
import time
import urllib2
import json


class Weather3:
    def __init__(self, api_key, hour, name, code, tag):
        self.api_key = api_key
        self.day = [u'今日', u'明日'][hour == 8].encode('utf-8')
        self.name = name.encode('utf-8')
        self.code = code
        self.indx = [-1]*25
        self.indx[6] = 5
        self.f = self.indx[hour]
        self.tag = tag

    def get_json(self):
        url = 'http://api.openweathermap.org/data/2.5/forecast?id={0:}&APPID={1:}'.format(self.code, self.api_key)
        o = urllib2.urlopen(url)
        r = o.read()
        j = json.loads(r)
        return j

    def get_info(self):
        ind = self.f
        data = self.get_json()
        base = data['list'][ind]
        tenki = base['weather'][0]['main']
        t_max = str('{0:.2f}'.format(base['main']['temp_max']-273.15))
        t_min = str('{0:.2f}'.format(base['main']['temp_min']-273.15))
        return (tenki, t_max, t_min)

    def make_txt(self):
        d = self.get_info()
        temp = "{0:}の{1:}ら辺の天候は{2:}です。最高気温は{3:}度くらいで、最低気温は{4:}度くらい。 #{5:}"
        text = temp.format(self.day, self.name, d[0], d[1], d[2], self.tag)
        return text

    def tweet(self):
        message = self.make_txt()
#        print message
        oat.tweet(message)

    def run(self):
        self.tweet()
        time.sleep(5)

if __name__ == '__main__':
    target = [[u'品川', 1852140], [u'船橋', '1863905'], [u'熊本', '1858421'], [u'宇治', '1849372']]
    jikan = datetime.datetime.now()
    flag = jikan.hour
    tag = jikan.microsecond

    for i in target:
        w = Weather3(oat.api_key, flag, i[0], i[1], tag)
        w.run()
