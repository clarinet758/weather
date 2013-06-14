#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import pywapi
from urllib import urlencode
import datetime
import otoken

result = pywapi.get_weather_from_yahoo('JAXX0043', 'metric')
time = datetime.datetime.now()
ms = time.microsecond

weather = u"@hoge 熊本の現在から今夜くらいの天候は" + result['forecasts'][0]['text'] + u" 気温は最高" \
        + result['forecasts'][0]['high'] \
       + u"で最低が" + result['forecasts'][0]['low'] + u"くらい。"

twit = weather.encode("utf-8")
print weather
print twit
otoken.client.request('https://api.twitter.com/1.1/statuses/update.json', 'POST', urlencode({'status': twit}))
