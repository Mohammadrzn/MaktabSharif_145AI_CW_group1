try :
    age=int(input('enter age'))
except:
    print('eror')
    age=int(input('enter age'))
if age <18 :
    print('you are not adult')
else:
    print('you are adult')