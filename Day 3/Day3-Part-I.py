
sum = 0
def RemainingCheck(start, content):
        
        End = start + 8 

        FirstInt = ""
        SecondInt = ""
        CommaFound = False
        BracketClose = False
        Error = False

        while start < len(content) and start < End:
            if not content[start].isdigit() and content[start] != "," and content[start] != ")":
                return -1
            
            if content[start] == ',' and not CommaFound:
                CommaFound = True
        
            elif content[start] == ',' and CommaFound:
                Error = True

            if content[start].isdigit() and not CommaFound:
                FirstInt += content[start]
            
            elif content[start].isdigit() and CommaFound:
                SecondInt += content[start]
            
            if content[start] == ')':
                BracketClose = True
                break
            
            start += 1
        
        if CommaFound and not Error and len(FirstInt) <= 3 and len(SecondInt) <= 3 and BracketClose:
            res = int(FirstInt) * int(SecondInt)
            return res
        else:
            return "DF"

            
with open(r'D:\CodingJourney\Google Advent of Code\Day 3\Inputs.txt', 'r') as file:

    content = file.readline().strip()

    print(content)

    for i in range(len(content)):
        if content[i:i+4] == "mul(":

            res = RemainingCheck(i+4, content)
            if res == "DF":
                continue
            else:
                sum += res


    

print(sum)




        

