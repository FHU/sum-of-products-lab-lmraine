#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    sum = 0
    for i in range(len(list1)):
        sum += (int(list1[i]) * int(list2[i]))
    return sum

if __name__ == '__main__':
    list1 = input("Enter first number:").split()
    list2 = input("Enter second number:").split()

    #if len(list1) != len(list2):
    #    print("Error")

    if len(list1) == len(list2):
        sum_prod = sum_of_products(list1, list2)
        print(sum_prod)