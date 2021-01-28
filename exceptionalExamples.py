#%%
print(x)
#%%
class myError(Exception):
    def __init__(self, message, expression):
        self.message = message
        self.expression = expression
#%%
numberList = [1,2,3]
for x in numberList:
    try:
        if x == 2:
            raise myError('There was a problem with x:', x)
        else:
            print(x)
    except myError as e:
        print(f'{e.message} {e.expression}')
#%%

try:
    # print(x) # NameError
    x = [1,2,3]
    print(x[3])
except NameError as someAlias:
    print(someAlias)
except IndexError as someAlias:
    print(f'Index Error: {someAlias}')    
except Exception as e: # All other cases
    print(f'Error caught gracefully: {e}')
finally:
    print('Always hit')
# %%
while True: # This loop will never exit even though it doesn't work
    try:
        print(y)
    except:
        raise myError('y is no defined', 'y')
#%%


# %%
