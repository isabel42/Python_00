import datetime

x = datetime.datetime.now()


print("Seconds since Jan 1, 1970:", f"{x.timestamp():,.4f}", "or", "{:.2e}".format(x.timestamp()), "in scientific notation" )
print (x.strftime("%b"),x.strftime("%d"),x.strftime("%Y"))