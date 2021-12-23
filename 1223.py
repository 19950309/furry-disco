sandwich_oders = ['egg','breast','sausage','pastrami','pastrami','pastrami']
finished_sandwiches = []
print('Sorry, the pastrami has sold out')
while 'pastrami' in sandwich_oders:
    sandwich_oders.remove('pastrami')

while sandwich_oders:
    finished_sandwich = sandwich_oders.pop()
    print('I made your %s sandwich' %(finished_sandwich)) 
    finished_sandwiches.append(finished_sandwich)
for i in finished_sandwiches:
    print(i)


responses = {}
active = True
while active:
    name =  input('what is your name?')
    dream_place = input('if you could visit one place in the world, where would you go?')
    responses[name] = dream_place
    repeat = input('do you want next person reply? (yes/no)')
    if repeat == 'yes':
        continue
    else:
        active = False
print('\n------result--------')
for k,v in responses.items():
    print('%s would like to visit %s' %(k,v))
