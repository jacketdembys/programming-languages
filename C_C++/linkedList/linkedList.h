/*
 * File: linkedList.h
 * Author: Jacket Demby's
 * Creation date: 12/20/2018
 */

#ifndef LINKEDLIST_H
#define LINKEDLIST_H

class LinkedList
{
private: 								// This private section accessed by functions defined in the public section
	struct node
	{
		int data;						// variable holding an integer value
		node* next; 					// create a node pointer
	};

	typedef struct node* nodePtr;		// define the struct with another name by using nodePtr instead of node*

	nodePtr head_node; 						// head node pointer
	nodePtr current_node;					// current node pointer
	nodePtr temporary_node;					// temporary node pointer

public: 								// This public section allows to access private section
	LinkedList();						// constructor function sets default values for head, current and temporary
	void addNode(int addData);			// adds a node and place a certain value inside of it
	void deleteNode(int deleteData); 	// deletes a node
	void printLinkedList();				// print the linked list

};

#endif