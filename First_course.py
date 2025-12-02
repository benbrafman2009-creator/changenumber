
def bneg(num, byet):
	ones_num = []
	byenry_num = [1] * byet

    # count down from byet-1 to 0
	for i in range(byet - 1, -1, -1):
		if (2 ** i) <= num:
			ones_num.append(i)
			num -= 2 ** i

    # if we still have leftover value, the number didn't fit
	if num != 0:
		return -1

    # set the bits we collected
	for i in range(len(ones_num)):
		byenry_num[byet - 1 - ones_num[i]] = 0
	for j in range(-1, -len(byenry_num)-1 , -1):
		if(byenry_num[j] == 0):
			byenry_num[j] = 1
			break
	return byenry_num




def main():
	print(bneg(3,5)) #דוגמא

if __name__ == '__main__':
	main()



