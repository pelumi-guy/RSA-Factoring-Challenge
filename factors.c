#include "main.h"

/**
* main - main block
* Description:
* Return: 0
*/

int main(int argc, char **argv)
{
	int i, r;
	uintmax_t num;
	char *endptr;
	
	data.fd = open(argv[1], O_RDONLY);
	if (data.fd == -1)
		file_err(argv[1]);

	for (i = 1; ; i++)
	{
		r = read_line(&(data.fd));
		if (r == 0)
			break;
		num = strtoumax(data.line, &endptr, 10);
		printf("line [%d]: %ju\n", i, num);
		free(data.line);
	}

	return(0);
}
