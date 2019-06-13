import time
print("welcome")
try:
	print("try")
	time.sleep(100)
	print(1/0)
except Exception as err:
	print("this is exception block")
	print(err)
except:
	print("this is except block")
finally:
	print("finally")
print("thank youuuuu")
time.sleep(5)