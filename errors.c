#include "main.h"

/**
 * file_err - a function that handles file opening error
 * Description:
 * @stack: stack
 * @fileName: Name of file passed as argumente
 * Return: EXIT_FAILURE
 */

int file_err(char *fileName)
{
	fprintf(stderr, "Error: Can't open file %s\n", fileName);
	exit(EXIT_FAILURE);
}

/**
 * malloc_err - a function that handles malloc errors
 * Description:
 * @stack: stack
 * Return: EXIT_FAILURE
 */

int malloc_err()
{
	fprintf(stderr, "Error: malloc failed\n");
	exit(EXIT_FAILURE);
}
