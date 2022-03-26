import datetime
start = datetime.datetime.now()
while 1:
    name = input('как звать')
    print(f'hello{name}')
    print(f'time out{datetime.datetime.now() -start}')