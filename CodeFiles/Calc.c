///////////////////////////////////////////////////////////////////////////////////////////
////////////////                                                           ////////////////
///////////////////////////////////////////////////////////////////////////////////////////

/*
Name: Christian Quintana
ID#:034789311
Project Description: This is a calculator that has 6 mathematical operations: add, subtract, divide, multiply, exponentiate, and discombobulate.
TrueCQ keeps the calculator continuously running by maintaining the master while loop.
repetitionsCQ is a number that is used to track the repetition in the discombobulate while loop.
xCQ and yCQ are the inputs, zCQ is the output.
continueCQ is the input for determining whether or not you want to continue.
*/

#include <stdio.h>
#include <windows.h>
#include <math.h>

#define piCQ 3.141592
#define NameOFCREatorCQ "Christian Quintana" // ME

int trueCQ = 1;
int repetitionsCQ = 0;
char operationCQ = '+';
char continueCQ = 'Y';
float xCQ, yCQ, zCQ;

int ContinueLogic(char InputCQ) // This unlatches the primary loop if the user chooses not to continue 
{
	if (InputCQ == 'N')
	{
		printf("Understood, shutting down program... \n");
		Sleep(1000);
		printf("Have a VERY good day. \n");
		Sleep(1000);
		trueCQ = 0;
	}
	else
	{
		printf("Restarting program. \n");
	}
	return 0;
}

int discombobulate(float num1CQ, float num2CQ) // secret hidden 6th function
{
	float zedCQ = 0;
	repetitionsCQ = 0;
	while (repetitionsCQ <= 999)
	{
		zedCQ += num1CQ;
		num1CQ += num2CQ;
		printf("%f \n", zedCQ);
		printf("DISCOMBOBULATING! \n");
		repetitionsCQ++;
		Sleep(rand() % 10);
	}
	return 0;
}

float calculate(num1CQ, num2CQ) // This handles all mathematical operations
{
	float ZedCQ = 0;
	if (operationCQ == '+')
	{
		ZedCQ = xCQ + yCQ;
	}
	else if (operationCQ == '-')
	{
		ZedCQ = xCQ - yCQ;
	}
	else if (operationCQ == '*')
	{
		ZedCQ = xCQ * yCQ;
	}
	else if (operationCQ == '/')
	{
		ZedCQ = xCQ / yCQ;
	}
	else if (operationCQ == '?')
	{
		discombobulate(xCQ, yCQ);
		return 0;
	}
	else if (operationCQ == '^')
	{
		ZedCQ = pow(xCQ, yCQ);
	}

	return ZedCQ;
}

int calculatormain() // The main calculator interface
{
	printf("Enter two decimal numbers rounded to two decimal places to perform the MATHEMATICAL operation. \n");
	scanf_s("%f%f", &xCQ, &yCQ);
	printf("Enter + to add. \n Enter - to subtract. \n Enter * to multiply. \n Enter / to divide. \n Enter ^ to raise a number to a power. \n Enter ? to discombobulate. \n");
	scanf_s(" %c", &operationCQ, 1);

	zCQ = calculate(xCQ, yCQ); // The calculate function is taken out so that the interface remains ucluttered and distinct with the inputs.
	
	printf("PROCESSING.\n");
	Sleep(500);
	printf("PROCESSING..\n");
	Sleep(750);
	printf("PROCESSING...\n");
	Sleep(1000);

	printf("%.2f %c %.2f = %.2f \n", xCQ, operationCQ, yCQ, zCQ);

	return 0;
}


main() // Main loop that runs the calculator again after calculations are peformed, so that the calculator can be run multiple times per isntance.
{
	printf("WELCOME TO THE CALCULATOR 9000 \n");
	while (trueCQ == 1)
	{
		calculatormain();
		printf("Would you like to perform another operation? Y/N \n");
		scanf_s(" %c", &continueCQ, 1);
		ContinueLogic(continueCQ);
	}

	return 0;
}
