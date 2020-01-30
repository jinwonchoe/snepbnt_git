


n = input()
print(hash(tuple([int(i) for i in input().split(',')])))


# 이 코드에서는 hash 라는 개념이 중요

# n = input()
'''
이 부분은 다음 행의 parser 를 작성하는 데 사용할 수 있지만
유용하지는 않음
'''

#tuple([int(i) for i in input().split()])))
'''
input().split() 를 통해 입력 받은 수를 ' ' (공백)을 기준으로 분리하고 
i 함수를 for 문을 통해서 int 로 바꾸고 출력해서 tuple 형태로 담아줍니다
'''
# tuple
'''
tuple(튜플)은 불변한 순서가 있는 객체의 집합
list 형과 비슷하지만, 한 번 생성되면 값을 변경할 수 없음

참고 url : https://wikidocs.net/15
'''
# hash
'''
해시(hash)란 다양한 길이를 가진 데이터를 고정된 길이를 
가진 데이터로 매핑(mapping)한 값이다.
이를 이용해 특정한 배열의 인덱스나 위치나 위치를 입력하고자 하는 
데이터의 값을 이용해 저장하거나 찾을 수 있다. 
기존에 사용했던 자료 구조들은 탐색이나 삽입에 선형시간이 걸리기도 했던것에 비해, 
해시를 이용하면 즉시 저장하거나 찾고자 하는 위치를 참조할 수 있으므로 
더욱 빠른 속도로 처리할 수 있다. 해시값이라고도 한다.
 해시는 암호학에 있어서 매우 중요한 요소이며, 블록체인(blockchain)을 구현하기 위한 핵심 기술이다.
'''

# 입력된 값을 hash 를 통해서 특정 길이를 가진 데이터로 mapping 했다
# 그 값이 특정 위치로 메핑이 되는 것임.