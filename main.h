#ifndef MAIN_H
#define MAIN_H

#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <inttypes.h>
#include <stdint.h>

/* Macros */
#define BUFSIZE 256
#define TOKSIZE 10
#define SUCCESS (1)
#define FAIL (-1)
#define NEUTRAL (0)

/**
* struct line_data - data from a line
* @num: positive integer on line
* @line: single line of file string
* @fd: file descriptor for file containing natural numbers to factor.
* Description: global variable to keep app state
*/
struct line_data
{
	char *line;
	int num;
	int fd;
} data;

/* utilities */
int _putchar(char c);
void *_realloc(void *ptr, unsigned int old_size, unsigned int new_size);
char *_memcpy(char *dest, char *src, unsigned int n);
void *fill_an_array(void *a, int el, unsigned int len);

/* read and parse line */
size_t read_line(int *fd);
void parse_line(void);

/* Error handlers */
int file_err(char *fileName);
int malloc_err();

#endif /* MAIN_H */
