#include <string>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;
int R,C;

int split(const string& s, char c,vector<string> &v)
{
	int count = 1;
	string::size_type i = 0;
	string::size_type j = s.find(c);

	while(j != string::npos){
		v.push_back(s.substr(i,j-i));
		i = j++ +1;
		j = s.find(c,j);
		count++;
	}
	v.push_back(s.substr(i,s.length()));
	return count;
}

void buildBand(int **band){
	for(int i=0;i<R;i++)
		for(int j=0;j<C;j++)
			band[i][j] = C*i + j + 1;
}

void display(int **band,int rows=R,int columns=C){
	for(int i=0;i<rows;i++){
		cout << "|";
		for(int j=0;j<columns;j++)
			cout << band[i][j] << " ";
		cout << "|"<< endl;
	}
}

void swap(int **band,const int k1,const int k2,const char option){
	int temp;
	if(option == 'R')
		for(int i=0;i<C;i++){
			temp = band[k1][i];
			band[k1][i] = band[k2][i];
			band[k2][i] = temp;
		}
	else if(option == 'C'){
		for(int i=0;i<R;i++){
			temp = band[i][k1];
			band[i][k1] = band[i][k2];
			band[i][k2] = temp;
		}
	}
}

void reverse(int **band,const char k){
	if(k == 'R'){
		for(int i=0;i<R;i++)
			for(int j=0;j<C/2;j++){
				int temp = band[i][j];
				band[i][j] = band[i][C-j-1];
				band[i][C-j-1] = temp;
			}
	}
	else if(k == 'C'){
		for(int i=0;i<C;i++)
			for(int j=0;j<R/2;j++){
				int temp = band[j][i];
				band[j][i] = band[R-j-1][i];
				band[R-j-1][i] = temp;
			}
	}
}

void transpose(int **band){
	int t_R = C,t_C = R;
	int *array[t_R];
	for(int i=0;i<t_R;i++)
		array[i] = new int[t_C];
	for(int i=0;i<R;i++)
		for(int j=0;j<C;j++){
			array[j][i] = band[i][j];
		}
	for(int i=0;i<t_R;i++)
		band[i] = array[i];
	R = t_R; C = t_C;
}

int main(void){
	int cases,k1,k2,v;
	char k;
	cin >> cases;
	for(int i=0;i<cases;i++){
		string line;
		int N;
		cin >> R >> C >> N;
		getline(cin,line);
		int *band[R];
		for(int h=0;h<R;h++)
			band[h] = new int[C];
		buildBand(band);
		cout << "Case: #" << i+1 << endl;

		for(int j=0;j<N;j++){
    		vector <string> vec;
			getline(cin,line);
			int length = split(line,' ',vec);
			if(length == 2){
				istringstream str(vec[0] + " " + vec[1]);
				str >> k;
				str >> v;
				if(k == 'P'){
					for(int x=0;x<R;x++)
						for(int l=0;l<C;l++)
							if(band[x][l] == v)
								cout << x+1 << " " << l+1 << endl;
				}
				else{
					cout << "WTF" << endl;
					return 0;
				}
			}
			else if(length == 3){
				istringstream str(vec[0] + " " + vec[1] + " " + vec[2]);
				str >> k;
				str >> k1;
				str >> k2;
				switch(tolower(k)){
					case 'v':
						cout << band[k1-1][k2-1] << endl;
					break;

					case 'r':
						swap(band,k1-1,k2-1,'R');
					break;

					case 'c':
						swap(band,k1-1,k2-1,'C');
					break;
				}
			}
			else if(length == 1){
				istringstream str(vec[0]);
				str >> k;
				switch(tolower(k)){
					case 'r':
						reverse(band,'R');
					break;
					case 'c':
						reverse(band,'C');
					break;
					case 't':
						transpose(band);
					break;
				}
			}
		}
	}
	return 0;
}
