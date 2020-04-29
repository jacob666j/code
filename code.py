password = str("a123456")
n = 0
while n < 3:
	ans = input("請輸入密碼: ")
	if ans == password:
		print("登入成功!")
		break
	else:
		print("密碼錯誤! 還有", 2-n,"次機會")
		n = n+1


