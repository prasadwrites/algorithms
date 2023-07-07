 #! /usr/env/path python

def helper(string, result, index , slate):
    if (len(string) == len(slate)):
        result.append(slate)
        return

    if(string[index].isdigit()):
        slate = slate + str(string[index])
        helper(string, result, index+1, slate)
        slate = slate[:-1]
    else:
        slate= slate + str(string[index].upper());
        helper(string, result, index+1, slate)
        slate = slate[:-1]
        slate = slate + str(string[index].lower())
        helper( string, result, index+1, slate)


result =[]
helper("a1b2",result, 0 , "")
print(result)