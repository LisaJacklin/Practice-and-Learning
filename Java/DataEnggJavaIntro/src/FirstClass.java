
public class FirstClass {
	public static void main(String[] args) {
		//this is the main function here in java!
		
		//don't create any static function aside from main!
		int i = 10;
		float f = 2.5f;
		double d = 5.5;
		boolean b = true;
		char c = 'a';
		System.out.println("Hello World");
		
		//call function f within class C
		C o = new C();
		o.f(); //this calls the new object of type class C
		
	}
}
//in java the main function needs to be written inside of the class
//java is fully oriented in object orientation!
//since c++ isn't entirely object oriented, this isn't the case for it.

class C {
	int f() { //functions must have a return type
		System.out.println("Inside f");
		return 0;
	}
}