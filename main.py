def sum_of_products(list1, list2):
    product = 0
    total = 0

    for i in range(len(list1)):
        product = list1[i] * list2[i]
        total += product
    
    return total

if __name__ == '__main__':
   # Input list A
    list_A = [int(n) for n in input().split()]

    # Input list B
    list_B = [int(n) for n in input().split()]

    sum_product = sum_of_products(list_A, list_B)

