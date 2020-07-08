#Fechas
dates = {"06-02","07-02", "13-02", "14-02", "20-02", "21-02", "27-02", "28-02", "06-03","07-03", "13-03", "14-03", "20-03", "21-03", "27-03", "28-03"}

for x in dates:
    if "02" in x:
        y = x.split("-")
        febrero = [int(y[0])]
        #print(febrero)
        for i in range(1,31,1):
            if i not in febrero:
                print (i)
        
    
