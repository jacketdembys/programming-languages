#include <iostream>
#include <cmath>

// function prototype for simon()
void simon(int);
int stonetolb(int);

// main function
int main()
{

    using namespace std;
    // Display a message
    /*
    cout << "Come up and C++ me some time." << endl;
    cout << "You won't regret it!" << endl;
    */

    // Input and Output
    /*
    int carrots;
    cout << "How manny carrots do you have?" << endl;
    cin >> carrots;
    cout << "Here are two more. ";
    carrots = carrots + 2;
    cout << "Now you have " << carrots << " carrots." << endl;
    */

    // Using built-in functions
    /*
    double area;
    cout << "Enter the floor area, in square feet, of your home: ";
    cin >> area;
    double side = sqrt(area);
    cout << "That's the equivalent of a square " << side
         << " feet to the side." << endl;
    cout << "How fascinating!" << endl;
    */

   // Using user-defined functions
   /*
   simon(3);
   cout << "Pick an integer: ";
   int count;
   cin >> count;
   simon(count);
   cout << "Done!" << endl;
   */
   // Another user-defined function
   int stone;
   cout << "Enter the weight in stone: ";
   cin >> stone;
   int pounds = stonetolb(stone);
   cout << stone << " stone = ";
   cout << pounds << " pounds." << endl;

    return 0;
}

void simon(int n)
{
    using namespace std;
    cout << "Simon says touch your toes " << n << " times." << endl;
}

int stonetolb(int sts)
{
    return 14*sts;
}




