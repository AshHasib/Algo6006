

def isAnagram(s1, s2):
    aList=list(s2)
    pos1=0
    stillOk=True
    
    while pos1<len(s1) and stillOk:
        pos2=0
        found=False
        
        while pos2<len(s2) and not found:
            if(s1[pos1]==aList[pos2]):
                found=True
            else:
                pos2+=1
        if found:
            aList[pos2]=None
        else:
            stillOk=False
        pos1+=1
    return stillOk


if __name__=='__main__':
    st1=input('Enter a string:')
    st2=input('Enter another string:')
    
    if isAnagram(st1, st2) == True:
        print('Both the strings are anagram')
    else:
        print('They are not anagram')
