

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res=''
        if len(strs)>0:
            for index,i in enumerate(strs[0]):
                for j in strs:
                    if j[index]!=i:
                        return res
                res=res+i
        else:
            return res


def test(input: list[str],output:str):
    print('Testing for input: '+str(input))
    
    s=Solution()
    value=s.longestCommonPrefix(input)
    print(value)
    if value==output:
        print('Test successfull!')
    else:
        print ('Test unsuccessfull!')


if __name__=="__main__":
    test([""],"")
    test(["dog","racecar","car"],"")
    test(["flower","flow","flight"],"fl")
