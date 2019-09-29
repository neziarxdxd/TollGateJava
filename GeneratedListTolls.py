x= "Angeles,Balagtas,Bocaue,Clark North,Clark South,Concepcion,Dau,Dinalupihan,Dolores,Floridablanca,Mabalacat (Mabiga),Marilao,Mexico,Meycauayan,Mindanao Avenue,Porac,Pulilan,San Fernando,San Miguel,San Simon,Sta. Ines,Sta. Rita,Tabang,Tarlac,Tipo/SFEX,Valenzuela"
'''
x=x.split(",")
for i in x:
    print("jComboBox1.addItem(\"{}\");".format(i))

'''
y="BAL	MIN	KAR	VAL	MEY	MAR	BOC	STR	PUL	SNM	SNF	MXC	ANG	DAU"
y=y.split()

for i in y:
    print("jComboBox2.addItem(\"{}\");".format(i))
    

    



