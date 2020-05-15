def commonCharacterCount(s1, s2):
    count=0
    for i in s1:
        for j in s2:
            if i==j:
                s1=s1.replace(i,'0',1)
                s2=s2.replace(i,'0',1)
                print(s1,s2)
                count=s1.count('0')

    return count
