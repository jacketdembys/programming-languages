all: mainLinkedList

mainLinkedList: mainLinkedList.o linkedList.o
	g++ -std=c++11 mainLinkedList.o linkedList.o -o mainLinkedList

mainLinkedList.o:	mainLinkedList.cpp
					@echo "Compiling mainLinkedList ..."
					g++ -c mainLinkedList.cpp
					

linkedList.o:	linkedList.cpp linkedList.h
				g++ -c linkedList.cpp

clean:
		rm -rf *.o mainLinkedList