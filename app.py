### Exception Handling

bank_db = {'123':{'name':'amol','bal':'100'}}

def check_acc_no(no):
    if no not in bank_db:
        raise IndexError('Account does not exist')
    return True

def check_balance(no):
    if check_acc_no(no):
        print(f"{bank_db[no]['bal']}")

def withdraw(no,amt):
    if check_acc_no(no):
        if bank_db[no]['bal'] < amt:
            raise MemoryError('Insufficient balance')
        else:
            bank_db[no]['bal']-=amt


try:
    no = input('enter your account number : ')
    check_balance(no)
    print('Banking operation done !!')
except IndexError as ind:
    print('Invalid account number')
    print(ind)
except MemoryError as mem:
    print('Account has low balance')
    print(mem)
else:
    print('Please rate our service')
finally:
    print('Thanks for banking with us')
    
