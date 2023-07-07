
#include "pch.h"
#include <iostream>


class StringFunction {
public:
	const char *array;
	int *indexArray;
	int indexCount;
	StringFunction(const char* initString): array(initString),
											indexArray(new int[strlen(initString)]) {

	}

	void printString(const char *str) {
		for (size_t i = 0; i < strlen(str); i++) {
			std::cout << str[i];
		}
		std::cout << std::endl;
	}

	int countString(const char *subStr) {
		int mainStrLen = strlen(array);
		int subStrLen = strlen(subStr);
		int count = 0;
		int subStrIndex = 0;
		for (int i = 0; i<mainStrLen; i++) {
			if (array[i] == subStr[subStrIndex]) {
				subStrIndex++;
				if (subStrIndex == subStrLen) {
					indexArray[count] = i - subStrLen + 1;
					count++;
					subStrIndex = 0;
				}

			}

		}
		indexCount = count;
		return count; 
	}


	char *replaceString(const char* stringRemoved, const char* stringAdded) {
		countString(stringRemoved);
		int diffLen = strlen(stringAdded) - strlen(stringRemoved);
		int finalLen = strlen(array) + (diffLen) * countString(stringRemoved);
		char *newString = (char *)malloc(sizeof(char)*finalLen);
		int mainIndex = 0;
		int index = 0;
		for (int i = 0; i < finalLen; i++) {
			if (i == (indexArray[index] + (index*diffLen))) {
				for (int j = 0; j < strlen(stringAdded); j++) {
					newString[i + j] = stringAdded[j];

				}
				index++;
				i = i + strlen(stringAdded);
				mainIndex = mainIndex + strlen(stringRemoved);
			}
			newString[i] = array[mainIndex++];
		}
		return newString;
	}
};


int main(int argc , char argv[])
{
	StringFunction strClass("Mary had a little lamb, lamb was little, Mary was little");
	std::cout << strClass.replaceString("little", "huge") << std::endl;

}