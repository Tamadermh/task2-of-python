#1.Create a simple function that takes 2 numbers and print their values

s=int(input("enter first num "))
t=int(input("enter second num "))


def sim_func(x=0,y=0):
    print(x,y)

    
sim_func(s,t)


'''In the above return function , use keyword arguments when calling the
function'''

sim_func(x=2,y=4)




'''.In the above return function , give x and y default values of 0 and call the
function with no arguments'''

sim_func()



'''Create the same sum function using the lambda'''
sum_func2= lambda  x ,y : print(x,y)
'''.Call the lambda function at the same definition line'''
sum_func2(3,5)



'''Write the difference between the local variable and global variable'''

'''المتغير الخاص يكون
معرف داخل الدالة ولايمكن ا
ستخدامه في مكان اخر الا ان يحول الى متغير عام والمتغير العام يمكن است
خدامه في كامل اقسام الكود'''
