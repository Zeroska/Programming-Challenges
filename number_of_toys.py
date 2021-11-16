def cal_number_of_toys(arrList,total_money):
    number_of_toys = 0
    arrList.sort()
    for i in range(len(arrList)):
        money_left = total_money - arrList[i]
        if (money_left) > 0:
            number_of_toys += 1
            # update total money I can buy
            total_money = money_left
        elif(money_left) < 0:
            return number_of_toys
        elif(money_left) == 0:
                number_of_toys + 1
    return number_of_toys
    
def main():
	test = (1,2,3)
	print(cal_number_of_toys(test,4))

if __name__ == '__main__':
	main()