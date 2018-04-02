print("Hola mundo!1")

print("Hola mundo!2")

a= "Funcionó el if"
print(a)

if 1>2:
	print(a)
elif 5>2:
	print("5 mayor que 2!")
else: 
	print("no fue verdadera")


def funct1():
	print('Hi there\n How are you?')
	
funct1()


def funct2(name):
	if name == 'David':
		print("Hola David!")
	elif name == "Alejandro":
		print ("Hola Alejandro")
	else:
		print ("Hola " + name + "!")

funct2("Lau")

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    funct2(name)
    print('Next girl')

for i in range(1,6):
	print(i)