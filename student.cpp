#include<iostream>
#include<fstream>
using namespace std;
struct student
{
    int rno;
    string sname;
    char div;
    string address;
}s;
class operation
{
    ifstream in;
    ofstream out;
    public:
    void addRecord();
    void dispRecord();
    void search();
    void delRecord();
};
void operation::addRecord()
{
    out.open("studentdb.txt",ios::app);
    cout<<"\n ENTER ROLL NO OF THE STUDENT :- ";
    cin>>s.rno;
    cout<<"\n ENTER NAME OF STUDENT :- ";
    cin>>s.sname;
    cout<<"\n ENTER DIVISION OF STUDENT :- ";
    cin>>s.div;
    cout<<"\n ENTER ADDRESS OF STUDENT :- ";
    cin>>s.address;
    if(out.is_open()){
        out<<s.rno<<"\t"<<s.sname<<"\t"<<s.div<<"\t"<<s.address<<"\t"<<endl;
    }
    else
       cout<<"Error in operning file";
    out.close();
}
void operation::dispRecord()
{
    in.open("studentdb.txt",ios::in);
    if(in.is_open()){
        while(in>>s.rno && getline(in,s.sname)){
          cout<<s.rno<<"\t"<<s.sname<<"\t"<<s.div<<"\t"<<s.address<<endl;
        }
    }
        else
        cout<<"\n Error in file opening";
     in.close();    
}
void operation::search()
{
    int key,flag=0;
    in.open("studentdb.txt",ios::in);
    cout<<"\n Enter roll no to search";
    cin>>key;
    if(in.is_open()){
        while(in>>s.rno && getline(in,s.sname)){
            if(key==s.rno)
            {
                flag=1;
                break;
            } 
        }
         if(flag==1)
            {
                cout<<s.rno<<endl<<s.sname<<endl<<s.div<<endl<<s.address<<endl;
            }
            else 
               cout<<"\n Record not found";
   }
        else
        cout<<"\n Error in file opening";
     in.close();    
}
void operation::delRecord()
{
    int key,flag=0;
    in.open("studentdb.txt",ios::in);
    ofstream temp;
    temp.open("temp.txt",ios::app);
    cout<<"\n Enter roll no to delete record";
    cin>>key;
    if(in.is_open()){
        while(in>>s.rno && getline(in,s.sname)){
            if(key!=s.rno)
            {
                temp<<s.rno<<"\t"<<s.sname<<"\t"<<s.div<<"\t"<<s.address<<endl;
            }
            else
               flag=1; 
        }
        in.close(); 
        temp.close();
         if(flag==1)
            {
                remove("studentdb.txt");
                rename("temp.txt", "studentdb.txt");
                cout << "Record deleted successfully." << endl;
            }
            else 
            {
              remove("temp.txt");  
              cout<<"\n Record not found";
            }       
   }
        else
        cout<<"\n Error in file opening";
     in.close();    
}
int main()
{
    operation op;
    int ch;
    char ans;
    do{
    cout<<"\n-------Student Record System-------";
    cout<<"\n 1. Insert Record";
    cout<<"\n 2. Display Record";
    cout<<"\n 3. Search Record";
    cout<<"\n 4. Delete Record";
    cout<<"\n 5. Exit";
    cout<<"\n Please Enter Your Choice";
    cin>>ch;
    switch(ch)
    {
    case 1: op.addRecord();
        break;
    case 2: op.dispRecord();
        break;
    case 3:op.search();
        break; 
    case 4:op.delRecord();
        break;         
    case 5:
         exit(0);
    }
    cout<<"\n Do you want to continue (Y/N)";
    cin>>ans;
    }while(ans=='y'|| ans=='Y');
    return 0;
}
