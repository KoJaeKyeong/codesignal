def sortByHeight(a):
    plus = sorted([i for i in a if i>0])            #0보다 큰 값을 정렬
    minus = [i for i in range(len(a)) if a[i]==-1]  #-1의 index 값을 리스트에 저장

    for k in minus:
        plus.insert(k,-1)   #정렬된 0보다 큰 값에 원래 -1이 있던 자리에 -1 삽입
    return plus
