#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
/*
    Finds the smallest divisor, if any, of a given number `n`
    Returns:
        smallest divisor if found
        1 if n is prime
*/
int fast_factor(long int n){
	uintmax_t f;

	if (n%2 == 0){
		/* printf("%lu=%lu*%i\n", n, n/2, 2); */
		return 2;
	}

	f = 3;
	while (f*f <= n)
	{
		if (n%f == 0){
			/* printf("%lu=%lu*%lu\n", n, n/f, f); */
			return f;
		}
		else{
			f += 2;
		}
	}
	/* printf("%lu=%lu*%i\n", n, n, 1); */
	return 1;
}