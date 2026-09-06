#Packing
address = ("247", "Brickfieild", "London", "UK", "259764")

for x in address:
    print(x, end=" ")

#unpacking
houseno, apartName, city, country, pin = address

print()
print("HNO:", houseno)
print("Apt NO:", apartName)
print(city)
print(country)
print(pin)

