#include<iostream>
using namespace std;

struct node{
	int num;
	struct node *right,*left;
}root;

class tree {
	node *temp=NULL,*root=NULL,*r=NULL,*n=NULL;
	public:
		node *create();
		void insert();
		void display();
};

node *tree::create(){
	r=new (struct node);
	cout<<"ENTER THE NO YOU WANT TO ADD :- ";
	cin>>r->num;
	r->left=NULL;
	r->right=NULL;
}

void tree::insert(){
	r=create();
	int prev,current=0;
	while(temp!=NULL){
		if(p=NULL){
			r=new (struct node);
			cout<<"ENTER THE NO YOU WANT TO ADD :- ";
			cin>>r->num;
			r->left=NULL;
			r->right=NULL;
		}
		else{
			p=p;
			cout<<"ENTER THE VALUE ";
			cin>>prev;
			while(True){
				if(prev<p->num){
					p->left=new(Node);
                    p= p->left;
					p->num=prev;
					 p->left=NULL;
					 p->right=NULL;
					 break;
				}

				else if(prev>p->num){
					if (p->right== NULL) {
						p->right=new(Node);
						p=p->right;
                        p->num=prev;
                        p->left=NULL;
                        p->right=NULL;
                        break;
				}
			}
		}
		current++;
   }
}
void tree::display(){
	r=temp;
	while(r!=NULL){
		cout<<r->num;
		r=r->right;
	}
}
int main(){
	tree t;
	t.insert();
	t.display();
	return 0;
}
