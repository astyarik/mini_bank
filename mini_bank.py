import random

class human():
	def __init__(self, name, balance, debtor=False, admin=False):
		self.name = name
		self.balance = balance
		self.debtor = debtor
		self.admin = admin
	
	def pay(self, payer):
		while True:
			summ = int(input("Введите сумму перевода\n>>> "))
			if summ < 0:
				print("Введите положительное число!")
			else:
				break
				
		if self.balance >= summ:
			self.balance -= summ
			payer.balance += summ
		else:
			print("Недостаточно денег!")

	def check(self):
		for user in users:
			print(f"Баланс:\n{user.name} - {user.balance}\n")
		if self.debtor:
			print("А еще Вы должник")
		if self.admin:
			print("А еще Вы админ")
			
	def role(self):
		if self.balance < 0:
			print(f"\n{self.name} - [Должник]")
			self.debtor = True
		if self.balance > 0:
			self.debtor = False
		if self.admin == True:
			print(f"{self.name} - [Админ]")
			
	def work(self):
		chanse = random.uniform(0.1, 1)
		worked = random.randint(100, 200)	
		if chanse <= 0.2:
			worked *= 2
			print("Вы получили зарплату в удвоенном размере!")
		self.balance += worked
		print(f"Вы заработали {worked} монет!")
		

ivan = human("Иван", 100)
jhon = human("Джон", -50, debtor=True)
admin1 = human("Админ", 1000, admin=True)

name = str(input("Введите своё имя\n>>> ")) or "Вы"
you = human(name, 500)

users = [you, jhon, admin1, ivan]

while True:
	while True:

			try:
				choise = int(input("Выберете действие:\n1. Перевести\n2. Проверить баланс\n3. Админ-мод\n4. Работать\n5. Выход\n>>> "))
				if choise == 1:
					payer = None
					payers = input("Введите имя, кому переводите\n>>> ")
					for user in users:
						if user.name == payers:
							payer = user
							break

					if payer:
						you.pay(payer)
					else:
						print("Нет такого")

				elif choise == 2:
					you.check()

				elif choise == 3:
					break

				elif choise == 4:
					you.work()
					
				elif choise == 5:
					print("Выход")
					break

			except ValueError:
				print("Неверное число!")

	if choise == 3:
		choice = int(input("Выбор действия\n1. Снять деньги\n2. Дать деньги\n3. Создать посетителя\n>>> "))
		try:
			if choice == 1:
				userr = input("Введите имя, чьи деньги снимаете\n>>> ")
				money = int(input("Выберите сумму\n>>> "))
				for user in users:
					if user.name == userr:
						userr = user
						user.balance -= money 
						break

			elif choice == 2:
				userr = input("Введите имя, кому даете деньги\n>>> ")
				money = int(input("Выберите сумму\n>>> "))
				for user in users:
					if user.name == userr:
						userr = user
						user.balance += money 
						break
			elif choice == 3:
				name = input("Введите имя\n>>> ")
				balance = int(input("Введите его начальный баланс\n>>> "))
				nameis = round(random.uniform(1, 1000000))
				nameis = human(name, balance)
				users.append(nameis)

		except ValueError:
			print("Неверное число")
	else:
		break
