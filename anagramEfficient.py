

def isAnagram(s1, s2):
    c1=[0]*26
    c2=[0]*26
    
    for i in range(len(s1)):
        pos=ord(s1[i])-ord('a')
        c1[pos]+=1
    for i in range(len(s2)):
        pos=ord(s2[i])-ord('a')
        c2[pos]+=1
    
    j=0
    stillOk=True
    
    while j<26 and stillOk:
        if c1[j]==c2[j]:
            j+=1
        else:
            stillOk=False
    return stillOk
    
if __name__=='__main__':
    s1=input('Enter a string:')
    s2=input('Enter another string:')
    
    if isAnagram(s1, s2)==True:
        print('Anagram')
    else:
        print('Not anagram')
