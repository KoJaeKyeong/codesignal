def isLucky(n):
    new_L=list(str(n))              #list에 넣기위해 스트링으로 변환 ex) n=1230일 때, new_L=['1','2','3','0']
    new_L=[int(i) for i in new_L]   #각 요소를 int형으로 변환
    std = int(len(new_L)/2)         #중간의 인덱스값
    h1=new_L[:std]
    h2=new_L[std:]
    return sum(h1)==sum(h2)
