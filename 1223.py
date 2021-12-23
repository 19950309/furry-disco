sandwich_oders = ['egg','breast','sausage']
finished_sandwiches = []
while sandwich_oders:
    finished_sandwich = sandwich_oders.pop()
    print('I made your %s sandwich' %(finished_sandwich)) 
    finished_sandwiches.append(finished_sandwich)
for i in finished_sandwiches:
    print(i)

