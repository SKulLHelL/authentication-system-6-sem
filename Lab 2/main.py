data = open(r"T:\.temp\dump.csv",'r',encoding="utf-8").read()
print("DNS имен из трафика: "+str(data.count('CNAME'))+"; % нежелательного трафика - "+str(round(data.count('CNAME')*100/data.count(',"DNS",'),3)))
