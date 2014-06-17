#include <iostream>
#include <fstream>
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */

using namespace std;

int main () {
  ofstream myfile;
  myfile.open ("RunCollatz.in");
  srand (time(NULL)); // initialize random seed

  for (int i = 0; i < 1000; i++) {
	int endpoint1 = rand() % 999999 + 1;
	int endpoint2 = rand() % 999999 + 1;
	myfile << endpoint1 << " " << endpoint2 << "\n";
  }
  
  myfile.close();
  return 0;
}
