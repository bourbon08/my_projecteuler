
#ifndef SIEVEE_H_26122011
#define SEIVEE_H_26122011
/* This will fill seive with a table of primes between 1 and number
use seive[x] == '1' to see if prime, or 0 for notprime */
void SeiveE(char seive[], int number)
{
	/* Declare our variables */
	int x, y;

	/* Loop for every number, set evens to 0 and odds to 1 */
	for (x = 1; x <= number; ++x)
		seive[x] = (x % 2 == 0 && x != 2) ? 0 : 1;

	/* Loop for every odd number and set every number divisible by a
	previous number to 0 */
	for (x = 3; x <= number; x += 2)
		if (seive[x] == 1)
			for (y = x * 2; y <= number; y += x)
				seive[y] = 0;

	return;
}

#endif