if __name__ == '__main__':
    N= int(input())
    list=[]
    count = 0
    while count < N:
        command = input()
        if command.find('insert')==0:
            i = int(command[7])
            e = int(command[9:])
            list.insert(i,e)
        elif command.find('print')==0:
            print(list)
        elif command.find('append')==0:
            e = int(command[7:])
            list.append(e)
        elif command.find('sort')==0:
            list.sort()
        elif command.find('pop')==0:
            list.pop()
        elif command.find('reverse')==0:
            list.reverse()
        elif command.find('remove')==0:
            e = int(command[7:])
            list.remove(e)
        count+=1


