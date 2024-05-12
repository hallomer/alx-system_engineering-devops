#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

/**
 * infinite_while - Infinite loop for zombie processes
 *
 * Return: 0 (Success)
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point
 *
 * Return: Always 0 (Success)
*/
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();

		if (pid == 0)
			exit(0);

		else if (pid > 0)
			printf("Zombie process created, PID: %d\n", pid);

		else
			return (1);
	}

	infinite_while();
	return (0);
}
