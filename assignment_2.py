#%% Intro

'''
Please The following code SHOULD run and FINISH...but doesn't

This is an example of an infinite loop.  This is NOT a good thing to 
have in your code.  It will cause your code to run forever and never
finish.  This is a problem because it will cause your code to use up
all of the resources on your computer and cause it to crash.

Please fix the code so that it runs and finishes.

You should only need to change two lines of code to fix this problem!
'''


#%%
# Code

# Count to 10 Program

finished_program = False
i = 0

while finished_program == False:


    print(f'Testing i = {i}')

    if i == 10:
        finished_program = True

    i += 1
