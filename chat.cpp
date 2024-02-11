#include<iostream>
#include<string.h>
using namespace std;
void user_input(int ch){
string user;
int num;
switch(ch){
case 1:
getline(cin,user);
cout<<"hello,"+user+","<<endl;
break;
case 2:
cin>>num;
if(num<18){
cout<<"you are young"<<endl;
}
else{
cout<<"your are mature"<<endl;
}
break;
case 3:
cout<<endl;
cin>>user;
cout<<"congratulation for completing "+user<<endl;
break;


}
}
void agent(){
switch(1){
case 1:
cout<<"what's your name?"<<endl;
user_input(1);
case 2:
cout<<"what's your age"<<endl;
user_input(2);

case 3:
cout<<"your qualification"<<endl;
user_input(3);
break;


}

}
int main(){
agent();

}
