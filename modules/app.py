#customercreate()
'''
import sales, pur
print(sales.x)
print(pur.x)
sales.customercreate()
pur.suppliercreate()
'''
'''
import sys
print(sys.path)
print("*"*25)
import sales
sales.customercreate()
'''
'''
import sys
sys.path.append("/home/khyaathipython/Desktop")
print(sys.path)
import sales
'''
#import pur
'''
from pur import suppliercreate
suppliercreate()
'''
'''
from pur import suppliercreate
pur.suppliercreate()
'''
#import ERP
'''
from ERP import stock, accounts
stock.product_in()
accounts.receivable_account()
'''
'''
from ERP.stock import product_in
product_in()
'''
'''
import ERP
stock.product_in()
'''
from ERP import stock, accounts