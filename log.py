import logging
#logging.info("fdsf")
logging.basicConfig(level=logging.DEBUG,
    filename="log.txt",
    format="%(asctime)s-->%(levelname)s==>%(message)s")
print("welcome")
logging.info("app execution started")
a=input("Enter a vlaue:")
logging.info("a value entered..")
b=input("Enter b value:")
logging.info("b value entered..")
logging.debug("before conversion a=%s,b=%s"%(a,b))
try:
    a=float(a)
    logging.info("a value converted...")
    b=float(b)
    logging.info("b value converted ...")
    logging.debug("after conversion: a=%s, b=%s"%(a,b))
    res=a/b
    logging.info("calculation completed..")
    print("result=%s"%res)
    logging.debug("result=%s"%res)
except ZeroDivisionError as err:
    logging.error(err)
    print("expecting b!=0")
except ValueError as err:
    logging.error(err)
    print("expecting digits only for a,b")
except Exception as err:
    logging.error(err)
    print(err)
    print("something went wrong, contact with admin.")
except:
    logging.error("some system level errors are occured..")
    print("sometinh went wrong in machine")
print("thnak you")
logging.info("app execution completed.......")