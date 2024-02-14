class mo_list:
    def print_list():
        fruit_list = ['사과', '바나나', '키위', '오렌지']
        for i in range(len(fruit_list)):
            print(100+i*10, fruit_list[i])
        
    def add_list(num1,num2):
        my_list = [num1, num2, 41, 50, 2, 4, 3, 4, 5, 8, 9, 10]
        even_sum = 0
        for num in my_list:
            if num % 2 == 0:
                even_sum += num
        
        print("짝수들의 합:", even_sum)

