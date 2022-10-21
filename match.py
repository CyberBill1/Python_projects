# 4. understanding switch

bike = 'Yamaha'

if bike == 'Hero':
	print("bike is Hero")

elif bike == "Suzuki":
	print("bike is Suzuki")

elif bike == "Yamaha":
	print("bike is Yamaha")

else:
	print("Please choose correct answer")

match bike:
    case "hero":
         print("bike is Hero")
    case "suzuki":
         print("bike is suzuki")
    case _:
         print("bike not found")