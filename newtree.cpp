#include<iostream>
using namespace std;
int cnt=0;
struct node{
	int chcnt,scnt;
	string bname,chname,sname;
	struct node *broot[10];
}*root=NULL;

class book{
	int i,j,k;
	public:
		void create();
		void display(node *r);		
};

void book::create()
{
	root=new node();
	cout<<"ENTER NAME OF BOOK :- ";
	cin.ignore();
	getline(cin,root->bname);
	cnt+=1;
	cout<<"ENTER HOW MANY CHAPTERS ARE THERE IN BOOK "<<root->bname<<" :- ";
	cin>>root->chcnt;
	cin.ignore();
	cnt+=1;
	for(i=0;i<root->chcnt;i++){
		root->broot[i]=new node();
		cout<<"ENTER NAME OF CHAPTER "<<(i)+1<<" :- ";
		getline(cin,root->broot[i]->chname);
		cout<<"ENTER HOW MANY SECTIONS ARE THERE IN "<<root->broot[i]->chname<<" :- ";
		cin>>root->scnt;
		cin.ignore();
		cnt+=root->chcnt;
		for(j=0;j<root->scnt;j++){
		    root->broot[i]->broot[j]=new node();
			cout<<"ENTER NAME OF THE SECTION "<<j+1<<" :- ";
			getline(cin,root->broot[i]->broot[j]->sname);
			cnt+=root->scnt;		
		}
	}
}

void book::display(node *r){
	cout<<"\n\tNAME OF BOOK IS :- "<<root->bname;
	cnt+=1;
	for(i=0;i<root->chcnt;i++){
		cout<<"\n\tNAME OF CHAPTER IS :- "<<root->broot[i]->chname;
		cnt+=1;
		cout<<"\n\tSECTION IN CHAPTER IS :-	"<<root->broot[i]->chname;
		cnt+=1;
		for(j=0;j<root->scnt;j++){
			cout<<"\n\tNAME OF THE SECTION IS :- "<<j+1<<"\t"<<root->broot[i]->broot[j]->sname;
			cnt+=root->scnt;
		}
	}
}

int main(){
	book b;
	int ch;
	char ans;
	do
	{
	cout<<"WELCOME TO BOOK MANAGEMENT SYSTEM";
	cout<<"\nENTER 1 FOR INSERTING RECORDS ";
	cout<<"\nENTER 2 FOR DISPLAY ";
	cout<<"\nENTER YOUR CHOICE :-";
	cin>>ch;
	switch(ch){
		case 1:
			b.create();
			break;
		case 2:
			b.display(root);
			cout<<"\n\tTIME COMPLEXITY OF PROGRAM IS O("<<cnt<<")";
			break;
		case 3:
			break;
    }
	cout<<"\n DO YOU WANT TO CONTINUE (Y/N)";
	cin>>ans;
	}while(ans=='y'||ans=='Y');
	return 0;
}
