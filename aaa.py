import re

ret =re.match('\w{3}','zdfsfs')
print(ret)
result = ret.group()
print(result)
# 我来了

ret =re.search('zd','zdfsfs')
print(ret)
result = ret.group()
print(result)


ret =re.findall('aba','ababa')
print(ret)

