import re

pattern = re.compile(r'[a-z]+',re.I)#re.I是忽略大小写

# r = pattern.match('123abd')
r1 = pattern.search('123aBd567657')
print(r1.group())

pattern2 = re.compile(r'[h]?[t]?[f]?tp[s]?://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]')
# r2 = pattern2.search('<li> <h6>农林牧渔、卫生、科学研究</h6><a href="http://ypt.cnki.net" target="_blank">农业</a><a href="http://shipin.cnki.net" target="_blank">食品</a><a href="http://www.chkd.cnki.net" target="_blank">医疗</a><a href="http://r.cnki.net/index/yaoye" target="_blank">药业</a><a href="http://r.cnki.net/index/cdchy" target="_blank">公共卫生</a> </li>')
# print(r2.group())

r3 = pattern2.findall('<li> <h6>农林牧渔、卫生、科学研究</h6><a href="https://ypt.cnki.net" target="_blank">农业</a><a href="https://shipin.cnki.net" target="_blank">食品</a><a href="http://www.chkd.cnki.net" target="_blank">医疗</a><a href="ftp://r.cnki.net/index/yaoye" target="_blank">药业</a><a href="http://r.cnki.net/index/cdchy" target="_blank">公共卫生</a> </li>')
print(r3)
