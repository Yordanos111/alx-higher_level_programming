#include "lists.h"
#include <stdlib.h>
#include <unistd.h>

/**
 * insert_node - inserts a number in an ordered linked list
 * @head: double pointer to the linked list
 * @number: number to insert in the new node
 *
 * Return: address of the new node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *c = *head;
	listint_t *nw = NULL;
	listint_t *t = NULL;

	if (!head)
		return (NULL);

	nw = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	nw->n = number;
	nw->next = NULL;

	if (!*head || (*head)->n > number)
	{
		nw->next = *head;
		return (*head = nw);
	}
	else
	{
		while (current && current->n < number)
		{
			t = c;
			c = c->next;
		}
		t->next = nw;
		nw->next = c;
	}

	return (new);
}
