def maxProfit(prices):
        # sẽ là phần từ đầu tiên chúng ta 
        buy = prices[0]
        mx_profit = 0
    
        # Vì chúng ta không cần phải trừ số đầu cho nên
        # Chúng ta sẽ bắt đầu từ phần tử số 1
        for i in range(1,len(prices)):
            #Check xem phần từ đầu tiên chúng ta mua có lời không
            # Trừ phần từ thứ 1 cho phần từ thứ 0 và tiếp tục như vậy
            profit = prices[i]-buy
            

            # nếu như tiền lời lớn hơn mx_profit (maximum_profit)
            # thì đây là profit chúng ta cần
            if profit>mx_profit:
                mx_profit = profit
            # Giá mua vị trí đang đứng mắc ngày tiếp theo thì chúng ta
            # gán giá của nó vào buy

            if buy>prices[i]:
                buy = prices[i]

        # Sau khi chạy hết for thì trả về số lời thật sự
        return mx_profit

def main():
    # Test case
    good = [1,2]
    print(maxProfit(good))

if __name__ == '__main__':
    main()