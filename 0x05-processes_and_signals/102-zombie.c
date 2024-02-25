#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
/**
 * infinite_while - infinite loop
 * Return: Always 0
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
 * main - makes zombie  processess
 * Return: 0
 */
int main(void)
{
	char i = 0;
	pid_t pid;

	while (i < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: &d\n", pid);
			sleep(1);
			i++;
		}
		else
			exit(0);
	}
	infinite_while();
	return (EXIT_SUCCESS);
}
