list1=[]
list2=[]
list3=[]
list4=[]

#initalising List with default values
#list1 is used to set flag, inital flag is -1
#list2 is used to add telephone no, inital telephone no is 0
#list3 is used to create chain, inital chain is 0
#list4 is used to insert name, inital data is no 

def initial(n):
    for i in range(0,n):
        list1.append(-1)
        list2.append(0)
        list3.append(1)
        list4.append("No Data")

#insertion using linear probing(open addresing) and without replacement
def insert(n):
    key=int(input("\t\tENTER TELEPHONE NUMBER TO INSERT :-"))
    name=str(input("\t\tENTER THE NAME :- "))
    hval=key%n
    a=hval
    if(list1[hval]==-1):
        list2[hval]=key
        list1[hval]=1
        list3[hval]=0
        list4[hval]=name
        
    else:
        for i in range(0,n):
            new=0
            hval=(key+i)%n
            if (list1[hval]==-1):
                list2[hval]=key
                list1[hval]=1
                list4[hval]=name
                for i in range(hval,n):
                    keey=list2[i]%n
                    if(a==keey):
                        if(i!=hval):
                            new=i
                for i in range(0,hval):
                    keey=list2[i]%n
                    if(a==keey):
                        if(i!=hval):
                            new=i
                list3[new]=hval
                break

#insertion using Quardratic probing
def insertinQuardratic(n):
    key=int(input("\t\tENTER TELEPHONE NUMBER TO INSERT :-"))
    name=str(input("\t\tENTER THE NAME :- "))
    for i in range(0,n):
        hval=(key+(i*i))%n
        if(list1[hval]==-1):
            list2[hval]=key
            list1[hval]=1
            list4[hval]=name
            break

#searching in Quardratic probing            
def qusearch(list1,list2,list3,n):
    no_search1=int(input("\t\tENTER TELEPHONE NUMBER YOU WANT TO SEARCH :- "))
    flagg=0
    for i in range(0,n):
        hval=(no_search1+(i*i))%n
        if(list2[hval]==no_search1):
            flagg=1
            break
    if(flagg==1):
        print("\t\tTELEPHONE NUMBER FOUND ")
    else:
        print("\t\tTELEPHONE NUMBER NOT FOUND ")

#searching in linear probing            
def search(list1,list2,list3,n):
    no_search=int(input("\t\tENTER TELEPHONE NUMBER YOU WANT TO SEARCH :- "))
    hval=no_search%n
    if(list2[hval]==no_search):
            print("\t\tTELEPHONE NUMBER FOUND ")

    else:
        inex=hval
        flagg=0
        while(list3[hval]!=0):
            if(list2[inex]==no_search):
                flagg=1
                break
            else:
                new_index=list3[inex]
                inex=new_index
        if(flagg==1):
            print("\t\tTELEPHONE NUMBER FOUND ")
        else:
            print("\t\tTELEPHONE NUMBER NOT FOUND ")

            
#display function is used to display whole list
def newdisplay(n):
    print("\t\t------------------------------------------------------")
    print("\t\t|","FLAG","|","TELEPHONE NO","|","Name","|","CHAIN","|")
    print("\t\t------------------------------------------------------")
    for i in range(0,n):
        print("\t\t|",list1[i],"|",list2[i],"|",list4[i],"|",list3[i],"|")
    print("\t\t-----------------------------------------------------")

def newdisplay2(n):
    print("\t\t----------------------------------------------")
    print("\t\t|","FLAG","|","TELEPHONE NO","|","Name","|","|")
    print("\t\t----------------------------------------------")
    for i in range(0,n):
        print("\t\t|",list1[i],"|",list2[i],"|",list4[i],"|")
    print("\t\t---------------------------------------------")
      
#MENU FOR LINEAR PROBING
def linearprobing():
    print("\t\t--------------------------------------------------")
    print("\t\t\t\tWELCOME TO LINEAR PROBING")
    print("\t\t--------------------------------------------------\n\n")
    n=int(input("\t\tENTER SIZE OF THE LIST "))
    initial(n)
    while(True):
        print("\n")
        print("\t\t1. PRESS 1 FOR INSERTING DATA ")
        print("\t\t2. PRESS 2 FOR SEARCHING DATA ")
        print("\t\t3. PRESS 3 FOR DISPLAY ALL DATA ")
        print("\t\t4. PRESS 4 TO GO BACK ")
        print("\t\t5. PRESS ANY KEY FOR EXIT \n")
        ch=int(input("\t\tENTER YOUR CHOICE :- "))
        print("\n")
        if(ch==1):
            insert(n)
        elif(ch==2):
            search(list1,list2,list3,n)
        elif(ch==3):
            newdisplay(n)
        elif(ch==4):
            break
        else:
            break
#MENU FOR QUARDRATIC PROBING
def Quardraticprobing():
    print("\t\t--------------------------------------------------")
    print("\t\t\t\tWELCOME TO QUADRATIC PROBING ")
    print("\t\t--------------------------------------------------\n\n")
    n=int(input("\t\tENTER SIZE OF THE LIST "))
    initial(n)
    while(True):
        print("\n")
        print("\t\t1. PRESS 1 FOR INSERTING DATA ")
        print("\t\t2. PRESS 2 FOR SEARCHING DATA ")
        print("\t\t3. PRESS 3 FOR DISPLAY ALL DATA ")
        print("\t\t4. PRESS 4 TO GO BACK ")
        print("\t\t5. PRESS ANY KEY FOR EXIT \n")
        ch=int(input("\t\tENTER YOUR CHOICE :- "))
        print("\n")
        if(ch==1):
            insertinQuardratic(n)
        elif(ch==2):
            qusearch(list1,list2,list3,n)
        elif(ch==3):
            newdisplay2(n)
        elif(ch==4):
            main()
        else:
            break
        
#MAIN MENU OR INDEX
def main():
    while(True):
        print("\t\t--------------------------------------------------")
        print("\t\t\t\tWELCOME TO SYSTEM ")
        print("\t\t--------------------------------------------------\n\n")
        print("\n")
        print("\t\t1. PRESS 1 FOR LINEAR PROBING")
        print("\t\t2. PRESS 2 FOR QUADRATIC PROBING")
        print("\t\t3. PRESS 3 FOR EXIT \n")
        ch=int(input("\t\tENTER YOUR CHOICE :- "))
        print("\n")
        if(ch==1):
            linearprobing()
        elif(ch==2):
            Quardraticprobing()
        elif(ch==3):
            break
        else:
            break

main()
