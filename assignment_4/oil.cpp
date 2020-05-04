#include<iostream>
#include<fstream>
#include "oil.h"
#include<queue>
using namespace std;


void Search(int left, int right, queue<int>& answer){
    int mid = (left+right)/2;
    int deter = observe(left,right);
    if (deter == 2){
        Search(mid+1,right,answer);
        Search(left,mid,answer);
    }else if(deter == 1){
        answer.push(left);
        answer.push(right);
    }else{
        return ;
    }
    
}


int main(void){
    initial();
    int N=oil_size();
    int min = 999999;
    int max = -1;
    queue<int> answer;
    Search(0,N-1,answer);
    while(!answer.empty()){
        int iter = answer.front();
        if ( iter < min)
            min = iter;
        if (iter > max)
            max = iter;
        answer.pop();
    }
    oil_report(min,max);
}
