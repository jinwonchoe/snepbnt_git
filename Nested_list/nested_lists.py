
# nested lists hacker Rank 파이썬 practice

score_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    score_list.append([name, score])
print(score_list)
'''
위의 for 문을 통해서 input이 들어가는 횟수를 지정해줄 수 있음
아래 name, score 을 통해 input 이 입력되는 범위를 지정해 줄수 있음
name 과 score 에 입력된 값을 은 최종적으로 score_list 에 append 를 시켜줌으로써 
순차적으로 축적됨
[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
--> 이런 순서로

특히 ' _ '(언더스코어) 는 값을 무시하고 싶은 경우 사용할 수 있다
더 깔끔하고 코드를 확인할 때 사용하지 않는 값임을 나타내기 때문에 직관적임

참고 url : https://doorbw.tistory.com/153
'''

second_highest = sorted(set([score for name, score in score_list]))[1]

'''
set([score for name, score in score_list]) 
이 코드의 결과 값은
{41.0, 37.2, 37.21, 39.0} 가 나옴
위 결과값을 sorted 함수를 사용하여 순차적으로 정렬한 후 2번째 인덱싱을 뽑아줌
'''

'''
sort 함수와 sorted 함수의 차이점
 sorted 함수는 정렬된 새로운 리스트를 리턴
 sort 메소드는 아무것도 리턴시켜주지 않음(None을 리턴시켜줌)
 
 sorted 함수는 값이 있는 변수 자체에 영향을 주지 않음 --> 새로운 리스트를 만들어 리턴
 sort 메소드는 값이 있는 변수 자체를 정렬해버림
 
참고 url : https://www.codeit.kr/questions/186
'''

print('\n'.join(sorted([name for name, score in score_list if score == second_highest])))

'''
[name for name, score in score_list if score == second_highest]
이 코드는 위에서 뽑은 score 와 second_highest 의 스코어가 같을 경우 
for 문을 통해 이름을 추출하여 정렬 후에 
join 함수를 통해 "\n" 하는 것이다

join 함수에 대한 설명 : https://wayhome25.github.io/python/2017/02/26/py-14-list/

위 과정을 통해서 촤종적으로 
Harry
Berry
값이 추출되는 것이다. 


오늘도 코테 하나를 꼼꼼하게 뜯어보면서 공부를 해보았다.
'''