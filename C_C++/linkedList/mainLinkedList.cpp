/*
 * File: mainLinkedList.h
 * Author: Jacket Demby's
 * Creation date: 12/20/2018
 */

// Import the necessary libraries
#include <cstdlib>
#include <iostream>
#include "linkedList.h"

// Main program
int main(int argc, char** argv)
{
	LinkedList list;		// initialize a linked list called list
	list.addNode(1);		// Add a node with a value 1
	list.addNode(2);		// Add a node with a value 2
	list.addNode(3);		// Add a node with a value 3	
	list.addNode(4);		// Add a node with a value 4	
	list.addNode(5);		// Add a node with a value 5

	list.printLinkedList();	// test the print function

	list.deleteNode(3);		// test the delete function
	list.printLinkedList();	// print to see if the delete function worked

	list.deleteNode(5);		// test the delete function
	list.printLinkedList();	// print to see if the delete function worked

	list.deleteNode(6);		// test the delete function
	list.printLinkedList();	// print to see if the delete function worked



	return 0;
}
