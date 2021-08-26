#include <map>
#include <iostream>
#include <fstream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <random>

using namespace std;

struct customerData{
	string customerName, projectName, customerParts;
};

struct builderData{
	string builderName;
	int builderAbility, builderVar;
};

typedef struct customerData cStruct;
typedef struct builderData bStruct;

void split(const string& s, char c, vector<string>& v) {
    string::size_type i = 0;
    string::size_type j = s.find(c);

    while (j != string::npos) {
        v.push_back(s.substr(i, j-i));
        i = ++j;
        j = s.find(c, j);

      	if (j == string::npos)
        	v.push_back(s.substr(i, s.length()));
   }
}

vector<string> readFile(string name){
	vector<string> arr;
	string myText;
	ifstream MyReadFile(name.c_str());
	int i=0;
	while (getline (MyReadFile, myText)) {
		vector<string> v;
		split(myText, '.', v);
		arr.push_back(v[0]);
		i++;
	}
	MyReadFile.close();
	return arr;
}

map<string, int> partsComplexity(vector<string> parts){
	map<string, int> d;
	for (int i=0; i<parts.size(); i++){
		vector<string> v;
		split(parts[i], ':', v);
		d[v[0]] = stoi(v[4]);
	}
	
	return d;	
}

string allocateBuilder(vector<string> builders){
	int num = (rand() % ( builders.size() + 1 ));
	if(num > 0){
		num -= 1;
	}
	return builders[num];	
}

cStruct getCustomerData(string customer){
	cStruct c;
	vector<string> cArray;
	split(customer, ':', cArray);
	c.customerName = cArray[0];
	c.projectName = cArray[1];
	c.customerParts = cArray[2];
	
	return c;
}

bStruct getBuilderData(string builder){
	bStruct b;
	vector<string> bArray;
	split(builder, ':', bArray);
	b.builderName = bArray[0];
	b.builderAbility = stoi(bArray[1]);
	b.builderVar = stoi(bArray[2]);
	
	return b;
}

int getMapValue(map<string, int> mymap, string c){
	for (auto& x: mymap) {
		if(x.first == c){
			return x.second;
		}
	}
	return 0;
}

void writeToFile(string str){
	ofstream MyFile("Output.txt", ios_base::app);
	MyFile << str;
}

double getRandND(int builderAbility, int robotVar){
	default_random_engine generator;
	normal_distribution<double> distribution(builderAbility, robotVar);
	return distribution(generator);
}

int setRobotComplexity(int &cmp, cStruct cInfo, map<string, int> d){
	int count = 0;
	for(char c : cInfo.customerParts){
		string s(1, c);
		cmp += getMapValue(d, s);
		count++;
	}
	
	if(cmp > 100){
		cmp = 100;
	}
	return count;
}

bool getBuildStatus(int &rand_nm, bStruct bInfo, int robotVariability, int robotComplexity){
	int constNum = 0;
	bool success = false;
	
	for(int i=1; i<=3; i++){
		if(i==2){
			constNum = 5;
		}
		else if(i==3){
			constNum = 10;
		}
		
		rand_nm = (int) getRandND(bInfo.builderAbility, robotVariability);
		
		if(rand_nm >= robotComplexity){
			success = true;
			break;	
		}
	}
	return success;
}

void updateOutputFile(bool success, int rand_nm){
	string str;
	string status="Build Fail";
	if(success){
		status = "Build Successful";
	}
	str = ":"+to_string(rand_nm) + ":" + status + "\n";
	writeToFile(str);
}

int main(){
	vector<string> parts = readFile("Parts.txt");
	vector<string> customers = readFile("Customers.txt");
	vector<string> builders = readFile("Builders.txt");
	
	srand(time(0));
	map<string, int> d = partsComplexity(parts);
	
	for (int i=0; i<customers.size(); i++){
		string builder = allocateBuilder(builders);
		
		cStruct cInfo;
		cInfo = getCustomerData(customers[i]);
				
		bStruct bInfo;
		bInfo = getBuilderData(builder);		
		
		int robotComplexity = 20;
		int count = setRobotComplexity(robotComplexity, cInfo, d);		
		
		string str = cInfo.customerName+":"+cInfo.projectName+":"+bInfo.builderName+":"+cInfo.customerParts+":"+to_string(robotComplexity);
		writeToFile(str);
		
		int robotVariability = 5 + count + bInfo.builderVar;
		
		int rand_nm = 0;
		bool success = getBuildStatus(rand_nm, bInfo, robotVariability, robotComplexity);
		
		updateOutputFile(success, rand_nm);
	}
	
	return 0;
}