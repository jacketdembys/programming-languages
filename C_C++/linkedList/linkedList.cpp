/*
 * File: linkedList.cpp
 * Author: Jacket Demby's
 * Creation date: 12/20/2018
 */

// Import the necessary libraries
#include <cstdlib>
#include <iostream>
#include "linkedList.h"


// as soon as the linkedList object is created, it sets the pointers to NULL (nothing)
LinkedList::LinkedList()
{
	head_node = NULL;					// set a null pointer
	current_node = NULL;				// set a null pointer
	temporary_node = NULL;				// set a null pointer

}

// this function adds a new node to the linked list
void LinkedList::addNode(int addData)
{
	nodePtr new_node = new node;	// declare a new node
	new_node->next = NULL;			// access the next element and make that point to nothing
	new_node->data = addData;		// fill the new node with some data


	// if a list is already created
	if(head_node != NULL)
	{
		current_node = head_node;

		// check if this is the last node
		while(current_node->next != NULL)
		{
			current_node = current_node->next;
		}
		current_node->next = new_node;
	} 
	else
	{
		// put the new node in the frond of the list if the list is not already created
		head_node = new_node;
	} 
}

// this function deletes a node from the linked list
void LinkedList::deleteNode(int deleteData)
{
	nodePtr delete_node = NULL;
	temporary_node = head_node;
	current_node = head_node;

	// until the current node is the one to be deleted
	while(current_node != NULL && current_node->data != deleteData)
	{
		temporary_node = current_node;
		current_node = current_node->next;
	}

	// if the data to be deleted was not in the list
	if(current_node == NULL)
	{
		std::cout << deleteData << " was not in the linked list\n";
		delete delete_node;
	}
	else
	{
		// if the node to be deleted is found
		delete_node = current_node;
		current_node = current_node->next;
		temporary_node->next = current_node;
		delete delete_node;
		std::cout << "The value " << deleteData << " was deleted\n";
	}

}

// this function prints the linked list
void LinkedList::printLinkedList()
{
	current_node = head_node;			// make the current node point to the head node

	while(current_node != NULL)
	{
		std::cout << current_node->data << std::endl;
		current_node = current_node->next;
	}
}