sl="Today is Friday"

# (1) 
In [5]: sl.endswith("day")
Out[5]: True

# (2)
In [6]:sl.count("day")
Out[6]: 2

# (3)
In [10]: sl.find("day")
Out[10]: 2

# (4)
In [11]: sl.rfind("day")
Out[11]: 12

# (5)
new1="Today is Saturday."

# (6)
In [8]:new1.swapcase()
Out[8]: 'tODAY IS sATURDAY.'

# (7)
In [13]: str.istitle("Today is Friday")
Out[13]: False

# (8)
In [14]:"Today is Friday".rjust(20)
Out[14]: '     Today is Friday'

# (9)
In [15]: max("Today is Friday")
Out[15]: 'y'

#(10)
In [17]: sl[2:5]
Out[17]: 'day'
