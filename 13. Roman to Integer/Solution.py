

class Solution:
    def romanToInt(self, s: str) -> int:
        valueStack={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        value=0
        skip=False
        for index,i in enumerate(s):
            if skip==True:
                skip=False
                continue
            try:
                if i=='I':
                    if s[index+1]=='V':
                        value=value+4
                        
                        skip=True
                        continue
                    elif s[index+1]=='X':
                        value=value+9
                        skip=True
                        continue

                elif i == 'X':
                    if s[index+1]=='L':
                        value=value+40
                        skip=True
                        continue
                    elif s[index+1]=='C':
                        value=value+90
                        skip=True
                        continue

                elif i=='C':
                    if s[index+1]=='D':
                        value=value+400
                        skip=True
                        continue
                    elif s[index+1]=='M':
                        value=value+900
                        skip=True
                        continue
                        
                
            except IndexError:      
                pass
            value=value+valueStack[i]

        return value
        
def test(input: str,output: int):
    print('Test for input: '+input)
    s=Solution()
    solution=s.romanToInt(input)
    if solution == output:
        print('Test successfull')
    else:
        print('Test failed!')

if __name__=='__main__':
    #test('III',3)
    #test('LVIII',58)
    test('MCMXCIV',1994)