a='hcltech'
from nsetools import Nse
nse = Nse()
print nse
q=nse.get_quote(a)
from pprint import pprint
pprint(q)
