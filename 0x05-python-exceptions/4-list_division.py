#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    quo = 0
    for i in range(list_length):
        try:
            quo = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            quo = 0
        except ZeroDivisionError:
            print("division by 0")
            quo = 0
        except IndexError:
            print("out of range")
            quo = 0
        finally:
            newlist.append(quo)
    return newlist
