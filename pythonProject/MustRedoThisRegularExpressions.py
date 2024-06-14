import re

#s = "Python exercises consist of various Modules"
#result = re.match("python", s)
#print(result.group())

# code on line 5 in order to match the word Bitcoin at the beginning of
# the string using the match() method and ignoring the case. This way, no matter if
# you have bitcoin or Bitcoin, the match is done either way.
# import re
# s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the
# current financial system. In 2017, the price of 1 BTC reached $20000, with a
# market cap of over $300B."
# print(result.group())

s = "Bitcoin was born on jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."
result = re.match("Bitcoin", s, re.I)
print(result.group())

# code on line 5 in order to match the words Bitcoin was
# at the beginning of the string using the match() method. Use the dot (.)
# belonging to regex syntax in your solution.
# import re
# s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the
# current financial system. In 2017, the price of 1 BTC reached $20000, with a
#  market cap of over $300B."
# result =
# print(result.group())

# s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. in 2007, the price of 1 BTC reached  $20000, with a market cap of over $300B."
# result = re.match(r"B.{6} .{3}", 5)
# print(result.group)

# 
s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. in 2007, the price of 1 BTC reached  $20000, with a market cap of over $300B."
result = re.search(r"(\d(4))\s", s)
print(result.group(1))