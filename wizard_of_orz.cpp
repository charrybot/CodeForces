#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
    int t; //test cases
    cin >> t;
    int panel[2*100000]={};
    string num[10] = {"9", "8", "7", "6", "5", "4", "3", "2", "1", "0"};
    for (int T=0; T<t; T++)
    {
        int n; // the number of panels
        cin >> n;
        string first="", second="";
        if (n%2==1) //odd
        {
            for (int i=0; i<n/2; i++)
            {
                first += num[i%10];
            }
            second = first;
            reverse(second.begin(), second.end());
            cout << first << num[(n/2)%10] << second << endl;
        }
        else if (n==2)
        {
            cout << "98" << endl;
        }
        else
        {
            for (int i=0; i<n/2; i++)
            {
                first += num[i%10];
            }
            second = first;
            reverse(second.begin(), second.end());
            cout << first << second.substr(1, second.size()) << 0 << endl;
        }
    }
}


