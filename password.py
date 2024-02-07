import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "!@#$%^&*()"

pas = lower + upper + number + symbols

length = int(input("Enter The Length Of Password You Want : "))
password = ""

for a in range(length):
	password += random.choice(pas)

print("Your Generated Password is :" +password)

print("GENERATED SUCCESSFULLY ")

