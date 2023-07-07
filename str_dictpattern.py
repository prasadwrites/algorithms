#! /usr/bin/env python


dictionary = {'1':['A','B','C'],
              '2':['D','E'],
              '12': ['X'],
              '3':['P','Q']}

str = "123"


stack = list()


def get_possible_patters(start_index):
    results = list()
    if start_index >= strlen:
        return results
    end_index = start_index


    while(end_index < strlen):
        substring = str[start_index:end_index+1]
        if substring in dictionary:
            for element in dictionary[substring]:
                stack.append(element)

                if end_index == strlen-1:
                    results.append(''.join(stack))

                else:
                    result = get_possible_patters(end_index+1)
                    if len(result) == 0:
                        #there is a dead end, stop the for loop
                        break
                    else:
                        results += result
                stack.pop()
        end_index += 1
    return results

strlen = len(str)
print get_possible_patters(0)
