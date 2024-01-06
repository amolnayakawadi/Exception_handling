### Exceptions 

## raise

operating_system = input('Enter your os system :')
if operating_system != 'Linux':
    raise NameError(f'{operating_system} operating system is not supported')
print('Welcome to the Linux')
print('This is the new operating system')


## Assert

operating_system = input('Enter your os system :')
assert operating_system == 'Linux',(f'{operating_system} operating system is not supported')
print('Welcome to the Linux')
print('This is the new operating system')
