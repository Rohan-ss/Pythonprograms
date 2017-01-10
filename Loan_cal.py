amt = eval(input("Enter Borrowed Ammount :"))
ri = eval(input("Enter Rate of Intrest :"))
y = eval(input("Enter Term in (Years)"))
year = y*12

print("Ammount Borrowed : $",float(amt))
print("Total Intrest Paid : $",float(ri))

intr = (amt*ri)/100

amtpaid = (amt+intr)/year
amt=amt+intr
print("Monthly Emi :",amtpaid)

amtbal =0
a=(amt*ri)/100
print("Month\tAmmount Paid\tReaming Balance")
for i in range(year):
        
        print("%i \t %f \t %f" %(i,amtbal,amt))
        amtbal=amtpaid
        amt=amt-amtpaid
    
        



