// Author: Pratik Gupta
// Reg No: 183
// 8 Aug, 2019

#include <bits/stdc++.h>
#include <fstream>
using namespace std;

int orientation(pair<int,int> a, pair<int,int> b, 
								pair<int,int> c) 
{ 
	int res = (b.second-a.second)*(c.first-b.first) - 
			(c.second-b.second)*(b.first-a.first); 

	if (res == 0) 
		return 0; 
	if (res > 0) 
		return 1; 
	return -1; 
}

vector<pair<int,int>> convexhull(pair<int,int> p1,pair<int,int> p2,pair<int,int> p3,pair<int,int> p4, vector<pair<int,int>> a, vector<pair<int,int>> b)
{
    vector<pair<int, int>> ret; 
    int uppera, lowera, upperb, lowerb;
    auto id = find(a.begin(),a.end(),p1);
    uppera = distance(a.begin(),id);
    id = find(a.begin(),a.end(),p2);
    lowera = distance(a.begin(),id);
    id = find(b.begin(),b.end(),p3);
    upperb = distance(b.begin(),id);
    id = find(b.begin(),b.end(),p4);
    lowerb = distance(b.begin(),id);
    int n1 = a.size(), n2 = b.size(); 
	int ind = uppera; 
	ret.push_back(a[uppera]); 
	while (ind != lowera) 
	{ 
		ind = (ind+1)%n1; 
		ret.push_back(a[ind]); 
	} 

	ind = lowerb; 
	ret.push_back(b[lowerb]); 
	while (ind != upperb) 
	{ 
		ind = (ind+1)%n2; 
		ret.push_back(b[ind]); 
	} 
	return ret; 
}
int main()
{
    vector<pair<int, int> > a,b,c; 
    int x,y;
    ifstream first_input;
    first_input.open("first_input.txt");
    if(!first_input)
    {
        cerr<<"Unable to open 1st input file";
        exit(1);
    }
    while(first_input>>x>>y){
        a.push_back(make_pair(x,y));
        c.push_back(make_pair(x,y));
    }
    first_input.close();

    ifstream second_input;
    second_input.open("second_input.txt");
    if(!second_input)
    {
        cerr<<"Unable to 2nd input file";
        exit(1);
    }
    while(second_input>>x>>y){
        b.push_back(make_pair(x,y));
        c.push_back(make_pair(x,y));
    }
    first_input.close();

    vector <pair<int,int>> point;
    int count1 = 0, count2 = 0, n1 = a.size(), n2 = b.size();
    for (auto e:a)
    {
        for (auto f:b)
        {
            for (auto g:c)
            {
                if (e!=g && f!=g)
                {
                    if (orientation(e,f,g) >= 0) count1++;
                    else if(orientation(e,f,g) <= 0) count2++;
                }
            }
            if(count1 == n1 + n2 -2 || count2 == n1 + n2 - 2)
            {cout<<"tangent at ("<<e.first<<","<<e.second<<") and ("<<f.first<<","<<f.second<<")"<<endl;
            point.push_back(e);
            point.push_back(f);}
            count1 = 0;
            count2 = 0;
        }
    }
    vector <pair<int,int>> ans = convexhull(point[0],point[2],point[1],point[3],a,b);

    cout<<"Convex Hull will be"<<endl;
    ofstream op;
    op.open("q1_output.txt");
    for (auto l:ans)
    {
        op<<l.first<<" "<<l.second<<endl;
        cout<<l.first<<" "<<l.second<<endl;
    }
    op.close();
    return 0;
}