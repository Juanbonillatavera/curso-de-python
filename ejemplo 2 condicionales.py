years=int(input("Digite el año"))
if years%4==0 and years%100!=0 or years%400==0:
  print(f"el {years}  es bisiesto ")
else:
  print(f"el {years} no es bisiesto")
  
