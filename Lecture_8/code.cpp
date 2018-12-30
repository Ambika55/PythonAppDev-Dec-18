#include <iostream>
#include <fstream>
using namespace std;

class A {
	public:
		int a = 4;
		char b = 'a';
};

int main() {
	ofstream file;
	file.open("output.bin", ios::binary);

	A a;

	file.write((char *)& a, sizeof(a));
}
