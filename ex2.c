/******************************************
*Student name: Noah Gorny
*Student ID: 209399757
*Course Exercise Group: 02 Math
*Exercise name: ex2
******************************************/
#include <stdio.h>
#include <math.h>
// To have clear use of boolean values
#define FALSE 0
#define TRUE 1
typedef int bool;
int main(int argc, char const *argv[])
{
	// To determine what mission to do
	int missionChoice;
	// To get \n chars
	char dummy;
	// Mission 1 Vars

	// To receive grade
	int grade;
	// The rank of the grade
	char rank;

	// Mission 2 Vars

	// To receive the numbers
	int num1, num2, num3;
	// To calculate average
	double avg;
	// To find min/max
	int min, max;

	// Mission 3 Vars

	// To recieve 3 chars
	char char1, char2, char3;

	// Mission 4 vars

	// To recieve exam grades
	double stud1Exam, stud2Exam;
	// To recieve exercise grades
	double stud1Hw, stud2Hw;
	// To recieve the students' names
	char stud1Name, stud2Name;
	// To determine final grades
	double stud1Final, stud2Final;
	// To know if there was invalid inputs
	bool valid_grades;


	printf("Please enter your input:\n");
	scanf("%d", &missionChoice);
	switch(missionChoice)
	{
		case 1:
		// Mission 1
		// Geting the grade
		printf("Please enter your score:\n");
		scanf("%d", &grade);
		if((grade>100)||(grade<0))
		{
			// Not a valid grade
			printf("Error\n");
		}
		else
		{
			if(grade>=90)
			{
				rank='A';
			}
			else if (grade>=80)
			{
				rank='B';
			}
			else if (grade>=70)
			{
				rank='C';
			}
			else if (grade>=60)
			{
				rank='D';
			}
			else
			{
				// Below 60
				rank='E';
			}
			printf("The rank for %d is: %c\n", grade, rank);
		}
		break;

		case 2:
		// Mission 2
		printf("Please enter three numbers:\n");
		scanf("%d %d %d", &num1, &num2, &num3);

		/* 
		I do know that I don't need to check twice,
		and I can do this with one big if-else bracket.
		But I honestly think it's more readable this way.
		Also the most elegant way is to probably define min() and max()
		functions of my own, but it's not allowed currently.
		*/

		// Finding max
		if (num1>num2)
		{
			if(num1>num3)
			{
				max=num1;
			}
			else
			{
				max=num3;
			}
		}
		else
		{
			if(num2>num3)
			{
				max=num2;
			}
			else
			{
				max=num3;
			}
		}
		// Finding min
		if (num1<num2)
		{
			if(num1<num3)
			{
				min=num1;
			}
			else
			{
				min=num3;
			}
		}
		else
		{
			if(num2<num3)
			{
				min=num2;
			}
			else
			{
				min=num3;
			}
		}
		// Calculating average
		avg=num1+num2+num3;
		avg=avg/3;
		// Printing everything
		printf("The minimal value is: %d\n", min);
		printf("The maximal value is: %d\n", max);
		// Using .2 to print two digits after the point
		printf("The average is: %.2f\n", avg);
		break;

		case 3:
		// Mission 3
		printf("Please enter three chars:\n");
		// Dummy receievs the \n character
		scanf("%c", &dummy);
		scanf("%c %c %c", &char1, &char2, &char3);
		// Part A
		printf("%c\n", char1);
		// Part B
		printf("%c\n%c\n%c\n", char1, char2, char3);
		// Part C
		printf("%c@%c@%c\n", char1, char2, char3);
		// Part D
		printf("%c\n", char3);
		// Part E
		printf("%c#%c#%c\n", char3, char2, char1);
		break;

		case 4:
		// Mission 4
		valid_grades=TRUE;
		printf("Please enter two course details:\n");
		scanf("%lf %lf %c", &stud1Exam, &stud1Hw, &stud1Name);
		scanf("%lf %lf %c", &stud2Exam, &stud2Hw, &stud2Name);
		// Checking the inputs
		if((stud1Exam>100)||(stud1Exam<0)||(stud1Hw>100)||(stud1Hw<0))
		{
			valid_grades=FALSE;
		}
		else if ((stud2Exam>100)||(stud2Exam<0)||(stud2Hw>100)||(stud2Hw<0))
		{
			valid_grades=FALSE;
		}
		// Calculating final grade
		stud1Final=8*sqrt(stud1Exam)+stud1Hw/10;
		stud2Final=8*sqrt(stud2Exam)+stud2Hw/10;
		// Check if the final grades make sense, just to be sure
		if((stud1Final>100)||(stud1Final<0)||(stud2Final>100)||(stud2Final<0))
		{
			valid_grades=FALSE;
		}
		// Checks if grades were indeed valid
		if(valid_grades)
		{
			// Printing the final output
			printf("The final grade of %c is: %.2f\n", stud1Name, stud1Final);
			printf("The final grade of %c is: %.2f\n", stud2Name, stud2Final);
		}
		else
		{
			printf("Error\n");
		}
		break;

		case 0:
		// Does nothing and exits
		break;

		default:
		// Does nothing and exits
		break;
	}
	// Ends the program
	return 0;
}
