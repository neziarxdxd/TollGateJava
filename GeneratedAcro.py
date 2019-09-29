import xlrd
d = {}
f = open("C:\\Users\\MY-PC\\Desktop\\TollGateJava\\NEWFILE.txt", "w")
wb = xlrd.open_workbook('D:\\New folder\\Book1.xlsx')
sh = wb.sheet_by_index(3)
x= len(sh.col_values(0))

for i in range(x):
    f.write("hash.put(\"{}\",\"{}\");\n".format(  sh.cell(i,0).value,sh.cell(i,1).value))



#print("hash.put("+"\""+start+"-"+destination+"\""+':'+str(value_Price[j+1])+")\n")
f.close()