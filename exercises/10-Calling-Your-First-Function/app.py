def is_odd(my_number):
  	return (my_number % 2 != 0)


def my_main_code():
    # your code here
    result = is_odd(45345)
    # print(result) if we do not use return on line 9 & or "print" on line 11. Print is for other humans; Return is for computer to use only
    return result

print (my_main_code())