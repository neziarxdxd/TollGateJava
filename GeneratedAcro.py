import xlrd
d = {}
f = open("C:\\Users\\MY-PC\\Desktop\\TollGateJava\\NEWFILE.txt", "w")
wb = xlrd.open_workbook('D:\\New folder\\Book1.xlsx')
sh = wb.sheet_by_index(3)

for i ,j in  :
    print(i,j)


#print("hash.put("+"\""+start+"-"+destination+"\""+':'+str(value_Price[j+1])+")\n")
#f.close()