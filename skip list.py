import random

class Node:
    def __init__(self, value, level):
        self.value=value
        self.forward=[None]*(level+1)

class SkipList:
    def __init__(self,max_level=3):
        self.max_level=max_level
        self.header=self.create_node(float('-inf'),max_level)
        
    def create_node(self,value,level):
        new_node=Node(value,level)
        return new_node
    
    def random_level(self):
        level=0
        while random.random()<0.5 and level<self.max_level:
            level+=1
        return level
    
    def insert(self,value):
        update=[None]*(self.max_level+1)
        current=self.header
        for i in range(self.max_level,-1,-1):
            #print("i in for ",i)
            while current.forward[i] and current.forward[i].value<value:
                current=current.forward[i]
                #print("i in while ",current.forward[i])
            update[i]=current
        level=self.random_level()
        print(level)

        if level>self.max_level:
            level=self.max_level
        new_node=self.create_node(value,level)
        for i in range(level+1):
            new_node.forward[i]=update[i].forward[i]
            update[i].forward[i]=new_node
            skip_list.display()
    def display(self):
        for level in range(self.max_level,-1,-1):
            node=self.header.forward[level]
            while node:
                print(f"{node.value} ->",end="")
                node=node.forward[level]
            print("None")
        print("\n")

skip_list=SkipList(max_level=3)

def main():
    while(True):
        print("\n1.PRESS 1 FOR INSERTING")
        print("2.PRESS 2 FOR DISPLAY")
        print("3.PRESS 3 FOR EXIT")
        CH=int(input("\nENTER YOUR CHOICE :- "))
        if CH==1:
            no=int(input("\nENTER NO YOU WANT TO INSERT :- "))
            skip_list.insert(no)
            ans=str(input("\nDO YOU WANT TO CONTINUE :- "))
            if(ans=='y' or ans=='Y'):
                main()
            else:
                break
        elif CH==2:
                skip_list.display()
                ans=str(input("\nDO YOU WANT TO CONTINUE :- "))
                if(ans=='y' or ans=='Y'):
                    main()
                else:
                    break
        elif CH==3:
            print("\nSUCCESSFULLY EXIT")
            break
        else:
            print("\nENTER CORRECT CHOICE ")
            main()
main()
            
