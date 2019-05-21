#include <iostream>
using namespace std;

/*
int main()
{
    cout << "Hello, world, it is coming from Berk!" << endl;
	return 0;
}
*/

class Greeter{
	public:
		void greet(){
			cout << "Hey from C++" << endl;
		}
		
		void show_num(int num1){
			cout << num1 << endl;
		}
		
		void show_nums(int num1, int num2){
			cout << num1 << " " << num2 << endl;
		}
		
		void sum(int num1, int num2){
			cout << num1 + num2 << endl;
		}
		
		int sum_r(int num1, int num2){
			return num1 + num2;
		}
};

extern "C"{
	Greeter* Greeter_new(){ return new Greeter(); }
	void Greeter_greet(Greeter* greeter){ greeter->greet(); }
	void Greeter_show_num(Greeter* greeter, int num){ greeter->show_num(num); }
	void Greeter_show_nums(Greeter* greeter, int num1, int num2){ greeter->show_nums(num1, num2); }
	void Greeter_sum(Greeter* greeter, int num1, int num2){ greeter->sum(num1, num2); }
	//int Greeter_sum_r(Greeter* greeter, int num1, int num2){return greeter->sum_r(num1, num2); }
	//int Greeter_sum_r(int* k, int num1, int num2){return k->sum_r(num1, num2); }

}