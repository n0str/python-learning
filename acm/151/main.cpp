#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;


int n,m,a,b;
int ok;
vector < vector < int > > g(400);
vector <char> part (400, -1);

int check1(int f, int t, int l)
{
	part[t] = 1;
	for (int i=0;i<g[t].size();i++)
	{
		if (g[t][i] == f)
		{
			if (l%2 == 0)
				ok = 0;
		}
		else
		{
			if (part[g[t][i]] == -1)
				check1(f, g[t][i], l + 1);
		}
	}
	return 0;
}

int main()
{
	ifstream I("INPUT.TXT");
	ofstream O("OUTPUT.TXT");
	I >> n >> m;
	ok = 1;
	for (int i=0;i<m;i++)
	{
		I >> a >> b;
		g[a].push_back(b);
		g[b].push_back(a);
	}


	for (int i=1;i<n+1;i++)
	{
		for (int j=0;j<n;j++)
			part[j] = -1;
		check1(i, i, 0);
	}
	
	if (ok)
		O << "YES";
	else
		O << "NO";
	return 0;
}