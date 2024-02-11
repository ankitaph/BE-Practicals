#include<iostream>
using namespace std;
int arr[10];
void selection_sort(int *arr,int n){
int i,min;
 for(i=0;i<n;i++)
 {
  min=i;
  for(int j=i+1;j<n;j++){
    if(arr[min]>arr[j]){
       min=j; 
   
  }
 
 }
 int temp=arr[min];
 arr[min]=arr[i];
 arr[i]=temp;
 
}
}
int main(){
int n;
cout<<"enter the size of array"<<endl;
cin>>n;
for(int i=0;i<n;i++){
cin>>arr[i];
}
selection_sort(arr,n);
cout<<"the sorted array"<<endl;
for(int j=0;j<n;j++){
cout<<arr[j]<<" ";

}





}
