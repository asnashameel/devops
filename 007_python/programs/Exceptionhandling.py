try:
    # print(10+'50')
    # print("50" + 10)
     print(5/0)
    

except TypeError:
    print('something went wrong')
except ValueError:
    print(' value error')
except ZeroDivisionError:
    print('zero division error')
finally:
    print("always executed")