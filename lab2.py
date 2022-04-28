def main():
    temp = [33,55,77,22,99,100,101]
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    print(calc_median_temperature(temp))
    print(calc_min_max_temperature(temp))
    print(calc_average_temperature(temp))
    display_main_menu()
    num_list = get_user_input()
    print(num_list)

def funcName(parameter1, parameter2):
    print("this is a dummy function")
    return 10

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    strlist = []
    floatlist = []
    strlist = input()
    strlist = strlist.split(",")
    for i in strlist:
        floatlist.append(float(i))
    return floatlist

def calc_average_temperature(temp):
    sum = 0.0
    count = 0
    for i in temp:
        count += 1
        sum += float(i)
    sum = sum/count
    return sum

def calc_min_max_temperature(temp):
    max = temp[1]
    min = temp[1]
    min_max_list = []
    for i in temp:
        if (i>max):
            max = i
        if (i<min):
            min = i
    min_max_list.append(float(min))
    min_max_list.append(float(max))
    return (min_max_list)

def calc_median_temperature(temp):
    temp.sort()
    median = 0.0
    size = len(temp)
    if (size%2)==0:
        median = (temp[int(size/2-1)]+temp[int(size/2)])/2
    else:
        median = (temp[int(size/2-0.5)])
    return float(median)

if __name__== "__main__":
    main()