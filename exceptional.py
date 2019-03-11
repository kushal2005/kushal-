
try:
	s=1
	print(s)
except:
    print("error")
else:
    print("hi")
finally:
    print("sucess")

#exceptional handling
try:
   #e=1
   print(e)      
except:
	print("error")
else:
	print("hii")
finally:
	print("succes")

try:
	#w=1
	print(w)
	raise NameError
except NameError:
	print("u have not defined s")
except:
	print("unsucess")
else:
	print("hii")

finally:
	print("succes")

