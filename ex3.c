/******************************************
* Student name: Noah Gorny
* Student: 209399757
* Course Exercise Group: 02
* Exercise name: ex3
******************************************/
#include <stdio.h>
// To have clearer use of boolean variables
typedef enum boolean {false=0,true=1} bool;
// Declaring functions
// First mission functions
void FirstMission();
void PrintMultTable(int small, int big);

// Second mission functions
void SecondMission();
void PrintDivided(int n, int div1, int div2, char key);
bool Determine_Operator(bool cond1, bool cond2, char key);

// Third mission functions
void ThirdMission();
void PrintFibonacci(int n);

// Fourth mission functions
void FourthMission();
void FindSmalls(int new_num);

// Fifth mission functions
void FifthMission();

// The main function
int main(int argc, char const *argv[])
{
	// To determine which mission to do
	int mission_number;
	// Boolean to stop the assignment loop
	bool stop_assign=false;
	// Main assignment loop
	while(stop_assign==false)
	{
		printf("Please select the assignment:\n");
		scanf("%d", &mission_number);
		switch(mission_number)
		{
			case 1:
			firstMission();
			break;
			case 2:
			secondMission();
			break;
			case 3:
			thirdMission();
			break;
			case 4:
			fourthMission();
			break;
			case 5:
			fifthMission();
			break;
			case 0:
			// End the loop and quits
			stop_assign=true;
			break;
			default:
			printf("NO SUCH ASSIGNMENT!\n");
			break;
		}
	}
	return 0;
}// End of main

/*********************
* function name: firstMission
* The Input: None
* The output: Does mission number 1
* The Function operation: Gets 2 integers, swaps them if needed
  and then calls printMultTable to print their table
**********************/

void FirstMission()
{
	// The input numbers
	int small,big;
	// To swap the number if needed
	int temp;

	printf("Please enter two numbers for the multiplication table:\n");
	scanf("%d %d", &small,&big);
	// If big is smaller, swap them
	if(small>big)
	{
		temp=big;
		big=small;
		small=temp;
	}
	// Print the table
	printMultTable(small, big);
}// End of the first mission

/*********************
* function name: printMultTable
* The Input: Two integers, small is smaller or equal to big
* The output: Print their mult table
* The Function operation: Go through it as it was a matrix 
  and print the mult of the indexes (nested loops).
**********************/

void PrintMultTable(int small, int big)
{
	// Indexes to use with the nested loops
	int i,j;
	for(i = small; i <= big; i++)
	{
		// For each row, print the each mult of the row
		for (j = small; j <= big; j++)
		{
			// Print the exact mult, with 4 spaces pressed left
			printf("%-4d", i*j);
		}
		// End of the row, go down a line
		printf("\n");
	}
}// End of function

/*********************
* function name: secondMission
* The Input: None
* The output: Does mission number 2
* The Function operation: Gets all the inputs needed
  checks if the key is ok, if he's ok it calls printDivided.
**********************/

void SecondMission()
{
	// The total amount of numbers (1 to n)
	int n;
	// The dividers
	int div1,div2;
	// Determine which task to do
	char key;
	// Dummy used to recieve the end-of-line char
	char dummy;

	printf("Please enter n:\n");
	scanf("%d", &n);
	printf("Please enter two dividers:\n");
	scanf("%d %d", &div1, &div2);
	printf("Please enter the key:\n");
	// Dummy used to recieve the end-of-line char
	scanf("%c", &dummy);
	scanf("%c", &key);
	// Checks if the key is acceptable
	if((key=='O')||(key=='o')||(key=='A')||(key=='a'))
	{
		// Key ok, procceed
		printDivided(n, div1, div2, key);
	}
	else
	{
		// Bad key, print error
		printf("ERROR IN KEY\n");
	}
}// End of the second mission

/*********************
* function name: printDivided
* The Input: n- total amount of numbers. div1/div2- integer dividers
  key- char the determine what numbers to print(only o,O,a,A chars).
* The output: Print divided numbers from 1 to n according to the key
* The Function operation: A for loop, inside it is checket
  if the current number is divided by div1,div2 and then it calls
  determine_Operator with the key to do the right operator.
**********************/

void PrintDivided(int n, int div1, int div2, char key)
{
	// Index for the for loop
	int i;
	// Conditions to use- is divided by div1 and is divided by div2
	bool cond1,cond2;

	for(i=1; i<=n; i++)
	{
		cond1=((i%div1)==0);
		cond2=((i%div2)==0);
		// Checks if those conditions are ok with the key
		if(determine_Operator(cond1, cond2, key))
		{
			// The number is good, print it
			printf("%d ", i);
		}
	}
	// We need to go down a line now
	// End of the line
	printf("\n");
}// End of function

/*********************
* function name: determine_Operator
* The Input: Two boolean conditions and a char key
* The output: If the key is A,a- use and operator
  if the key is O,o- use or operator
* The Function operation: A simple double if
**********************/

bool Determine_Operator(bool cond1, bool cond2, char key)
{
	if((key=='O')||(key=='o'))
		return (cond1||cond2);
	if((key=='A')||(key=='a'))
		return ((cond1)&&(cond2));
	// Its not supposed to get here
	printf("BUG- WRONG KEY\n");
	return false;
}// End of function

/*********************
* function name: thirdMission
* The Input: None
* The output: Does mission number 3
* The Function operation: Gets a number, checks if hes not smaller than 1
  then calls printFibonacci to do the job.
**********************/

void ThirdMission()
{
	// To recieve the number
	int n;
	printf("Please enter n:\n");
	scanf("%d",&n);
	// Checks if n is smaller than 1
	if(n<1)
	{
		// Bad input
		printf("INPUT ERROR\n");
	}
	else
	{
		// Calculate and print the serie
		printFibonacci(n);
	}
}// End of mission 3

/*********************
* function name: printFibonacci
* The Input: integer n- not smaller than 1
* The output: Prints the fibonacci serie until n
* The Function operation: It does a for loop and uses 3 integers
  to remember the last 2 members of the serie to calculate the new one.
  Then it rotates their values to find the next member and so on.
**********************/

void PrintFibonacci(int n)
{
	// Index used in the for loop
	int i;
	// These are used to remember i-2 and i-1 in the serie
	int last_old=0, last_new=0;
	// Result of each calculation of the next member of the serie
	int result;
	// Here we calculate result each time and print him
	for (i = 1; i <= n; i++)
	{
		if(i==1)
		{
			// First result is 1
			result=1;
		}
		else
		{
			// Else, we calculate result with the formula
			result=last_old+last_new;
		}
		// Printing the new number in the serie
		printf("%d ", result);
		// Switching places-last_new moves to last_old, result to last_new
		last_old=last_new;
		last_new=result;
	}
	// Go down a line at the end
	printf("\n");
}// End of function

/*********************
* function name: fourthMission
* The Input: None
* The output: Does mission number 4
* The Function operation: Creates the new num loop and filter out non
  positive numbers (unless its -1).
**********************/

void FourthMission()
{
	// To recieve the new numbers
	int new_num;
	// To know when to stop the while loop
	bool stop_fourth=false;

	printf("Please enter your sequence:\n");
	while(stop_fourth==false)
	{
		// Expected format
		scanf("%d", &new_num);
		// 0 is NOT a positive number
		if(new_num>0)
		{
			// Good number, proceed with the calculation
			findSmalls(new_num);
		}
		else
		{
			if(new_num==-1)
			{
				// Time to finish, call findSmalls with -1 to print
				findSmalls(new_num);
				// And stop the loop
				stop_fourth=true;
			}
		}
	}// End of while
}// End of mission 4

/*********************
* function name: find Smalls
* The Input: A new number to see if it's small or not
* The output: updates the static integer inside
  and prints them if the new num is -1.
* The Function operation: Checks all the cases that could happen and
  updates smallest and almost_smallest if needed.
**********************/

void FindSmalls(int new_num)
{
	// These are static in order to save the changes we make with new_num
	static int smallest=-1, almost_smallest=-1;

	if(new_num==-1)
	{
		// Printing time!
		printf("%d %d\n", smallest, almost_smallest);
		// Also, restarting statics
		smallest=-1;
		almost_smallest=-1;
	}
	else
	{
		if(smallest==-1)
		{
			// There is not a single small number!
			smallest=new_num;
			almost_smallest=new_num;
		}
		else
		{
			// We need to see if there's even 2 smallest numners or just 1
			if(smallest==almost_smallest)
			{
				// There is only one small number, checks if new_num is smaller
				if(new_num<smallest)
				{
					smallest=new_num;
				}
				if(new_num>smallest)
				{
					almost_smallest=new_num;
				}
			}
			else
			{
				// Regular check
				if(new_num<smallest)
				{
					// A swap between smallest and almost_smallest
					almost_smallest=smallest;
					smallest=new_num;
				}
				else if(new_num<almost_smallest)
				{
					if(new_num!=smallest)
					{
						// smallest < new num < almost_smallest
						almost_smallest=new_num;
					}
				}
			}//else smallest==almost
		}// else smallest==-1
	}// else new_num!=-1
}// End of the function

/*********************
* function name: fifthMission
* The Input: None
* The output: Does mission number 5
* The Function operation: Creates the new num loop and filter out non
  positive numbers (unless its -1).
**********************/

void FifthMission()
{
	// To recieve to number
	unsigned long number;
	// To sum the digits
	int sum=0;
	printf("Please enter your number:\n");
	scanf("%lu", &number);
	// while there is still digits to collect
	while(number!=0)
	{
		// Add the last digit
		sum+=number%10;
		// Throw the last digit
		number=number/10;
	}
	printf("%d\n", sum);
}// end of mission 5