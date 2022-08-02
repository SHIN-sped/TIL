 



# 매일 배운 내용 정리하기

---

## 1. Python 기초

### 프로그래밍(programming) - 명령어의 모음(집합)

### 언어 - 자신의 생각을 나타내고 전달하기 위해 사용하는 체계 문법적으로 맞는 말의 집합

### declarative knowledge - 사실에 대한 내용

### imperative knowledge - How-to



## 2. 파이썬 이란?

### 문법이 간단하면서도 엄격하지 않음 ex)변수에 별도의 타입 지정이 필요 없음

### 문법 표현이 매우 간결  ex) 문장 구분할 때  들여쓰기를 사용

### Expressive language - 같은 작업에 대해서도 더 간결하게 작성 가능

### 크로스 플랫폼 언어 - 윈도우즈, 리눅스 유닉스 다양한 운영체제 실행 가능



## 3. 파이썬의 특징

### 인터프리터 언어(interpreter), 객체 지향 프로그래밍(Object Oriented programming) 객체(object): 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것



## 4. 파이썬 기본 인터프리터 IDLE

### Integrated development and learning environment >>> code 실행됨



## 5. 코드 스타일 가이드



```python
print('hello')
print('world')

a = 'apple'

if True:
				print(True)
else:
  					print(False)
b = 'banana'

print('hello')
print('world')

a = 'apple'

if True:
		print(True)
else:
  	print(False)
b = 'banana'
```



## 6. 들여쓰기(Identation)

### Space Sensitive - 들여쓰기, 4번 space , 1탭, 한 코드 안에서 한 종류의 들여쓰기



## 7. 변수(variable)

### 변수- 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름, 파이썬은 객체 지향 언어이며, 모든 것이 객체로 구현되어 있음

### 동일 변수에 다른 객체를 언제든 할당할 수 있기 떄문에, 즉 참조하는 객체가 바뀔 수 있기 때문에 '변수' 라고 불림

### 할당 연산자(=)을 통해 값을 할당

## type() - 변수에 할당된 값의 타입

## id() - 변수에 할당된 값(객체)의 고유한 아이덴티티 값이며 메모리주소



```python
i = 5
j = 3
s = '파이썬'
print(i + j)
print(i - j)
print(i * j)
'안녕' + s
s * 3
s = 'Python'
s + ' is fun'

```



## 8. 변수 할당

### 같은 값을 동시에 할당할 수 있는

### 다른 값을 동시에 할당 할 수 있음(multiple assignment)

<code>x, y = 1, 2		

print(x, y)</code>



## 9. 식별자(identifiers)

### 파이썬 객체(변수, 함수, 모듈, 클래스 등)를 식별하는데 사용하는 이름(name)

### 규칙 - 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성

### 첫 글자에 숫자가 올 수 없음

### 길이제한이 없고, 대소문자를 구별

### 다음의 키워드(keywords)는 예약어(reserved words)로 사용할 수 없음

### 내장함수나 모듈 등의 이름으로도 만들면 안됨

### 기존의 이름에 다른 값을 할당하게 되므로 더 이상 동작하지 않음



## 10. 사용자 입력

### input([prompt]) - 값을 즉시 입력 받을 수 있는 내장 함수, 대괄호 부분에 문자열을 넣으면 입력 시, 해당 문자열을 출력, 반환값은 항상 문자열의 형태로 반환



## 11. 주석(comment)

###	코드에 대한 설명 - 중요한 점이나 다시 확인하여야 하는 부분 # 표시

### 가장 중요한 습관



# 파이썬 자료형

## 자료형 분류

### 불린형(boolean type) - True / False 값을 가진 타입 bool, 비교/논리 연산나을 수행함에 있어서 활용됨, 0 0.0 () [] '' none false로 변환됨

### 수치형(numeric type)- int(정수, integer) float(부동소수점, 실수, floating point number) complex(복소수, complex number)

### 문자열(string type)

### None - 값이 없음을 표현



## 12. 논리 연산자(logical operator)

### 논리식을 판단하여 참과 거짓를 반환함 - Not(true를 false로, false를 true로)

### and 모두 참인 경우 참, 그렇지 않으면 거짓

### or 둘 중 하나만 참이라도 참, 그렇지 않으면 거짓

### not 참 거짓의 반대의 결과



## 13. 수치형 (numeric type)

### 모든 정수의 타입은 int

### 매우 큰 수를 나타낼 때 오버플로우가 발생하지 않음



## 14.산술 연산자(arithmetic operator)

## 15. 비교 연산자(comparison operator) - ==(같음) !=(같지않음)



## 16. 문자열(string type)

### 모든 문자는 str 타입, 문자열은 작은 따옴표(')나 큰 따옴표(")를 활용하여 표기

### 작은 따옴표나 큰 따옴표를 삼중으로 사용 - 따옴표 안에 따옴표를 넣을 때, 여러줄을 나눠 입력할 때 편리



## 17. 인덱싱

### 인덱스를 통해 특정 값에 접근할 수 이씀 s[1] => 'b'

### 문자열 슬라이싱(Slicing) 예제 s[2:5] = 'cde', s[2:5:2] = 'ce', s[5:2:-1] = 'fed', s[:3] = 'abc', s[5:] = 'fghi', s[::] = 'abcdefghi' =>s[0:len(s):1]과 동일, s[::-1] = 'ihgfedcba' => s[-1:-(len(s)+1):-1]



## 18. 기타

### 결합(concatenation)

### 반복(Repetition)

### 포함(membership)

## 문자열의 활용

### Escape sequence - 문자열 내에서 특정 문자나 조작을 위해서 역슬래시( \ ) 를 활용하여 구분 \n줄바꿈 \t탭 \r캐리지리턴 \0널(null) \\\=\  ( \' )=단일인용부호 (\")=이중인용부호

### 문자열 내에서 특정 문자나 조작을 위해서 역슬래시( \ )를 활용하여 구분 

## 19. String interpolation

### 문자열을 변수를 활용하여 만드는 법 - %-formatting

### 문자열을 변수를 활용하여 만드는 법 - f-string



## 20. 문자열 특징

### immutable : 변경 불가능함

### iterable : 반복 가능함

```python
print('철수 \'안녕\'') # 철수 '안녕'
print('이 다음은 엔터. \n그리고 탭\t탭')
# 이 다음은 엔터.
# 그리고 탭	탭

name = 'Kim'
score = 4.5

print('Hello, %s' % name)
print('내 성적은 %d' % score)
print('내 성적은 %f' % score)
# Hello, Kim
# 내 성적은 4
# 내 성적은 4.500000

name = 'Kim'
score = 4.5
print(f'Hello, {name}! 성적은 {score}')
# Hello, Kim! 성저은 4.5

pi = 3.141592
print(f'원주율은 {pi:.3} 반지름이 2일때 원의 넓이는 {pi*2*2}')
# '원주율은 3.14. 반지름이 2일때 원의 넓이는 12.566368'

a = 'my string?'
a[-1] = '!'

a = '123'
for char in a:
  	print(char)
```



## 암시적 형 변환(implicit typecasting)

### 사용자가 의도하지 않고, 파이썬 내부적으로 자료형으로 변환 하는 경우 - bool, numeric type (int, float, complex)

### 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환 하는 경우 - bool, numeric(int, float, complex)

## 명시적 형 변환(implicit typecasting)

### int- str*, float = int

### float- str*, int = float

### Str- int, float, list, tuple, dict = str

#### 형식에 맞는 문자열만 가능

 

```python
int('3') + 4 # 7
float('3.5') + 5 # 8.5
```



## 21. 컨테이너 정의

### 여러 개의 값을 담을 수 있는 것(객체)으로, 서로 다른 자료형을 저장할 수 있음 ex) List, tuple

### 컨테이너의 분류 - 순서가 있는 데이터(ordered) vs 순서가 없는 데이터 (unordered)

### 순서가 있다 != 정렬되어 있다.



## 22. 컨테이너 분류

### 시퀀스 - 문자열(문자들의 나열), 리스트(번경 가능한 값들의 나열), 튜플(변경 불가능한 값들의 나열), 레인지(숫자의 나열)

### 컬렉션/비시퀀스 - 세트(유일한 값들의 모음), 딕셔너리(키-값들의 모음)



## 23. 시퀀스형 컨테이너

### 시퀀스형 주요 공통 연산자

## s[i] = s의 i 번째 항목, 0에서 시작합니다

## s[i:j] = s의 i 에서 j 까지의 슬라이스

## s[i:j:k] = s의 i 에서 j 까지 스텝 k 의 슬라이스

## s + t = s 와 t의 이어 붙이기

## s * n 또는 n * s = s 를 그 자신에 n 번 더하는 것

## x in s = s 의 항목 중 하나가 x 와 같으면 True, 그렇지 않으면 false

## x not in s = s 의 항목 중 하나가 x 와 같으면 false, 그렇지 않으면 True

## len(s) = s 의 길이

## min(s) = s 의 가장 작은 항목

## max(s) = s 의 가장 큰 항목



## 24. 리스트(List)

### 리스트(List) 정의 

- ### 변경 가능한 값들의 나열된 자료형

- ### 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음

- ### 변경 가능하며 반복가능함

- ### 항상 대괄호 형태로 정의하며 요소는 콤마로 구분



### 생성과 접근

### 리스트는 대괄호([ ]), 혹은 리스트() 를 통해 생성, 순서가 있는 시퀀스로 인덱스를 통해 접근 가능(값에 대한 접근은 list[i] )

## 리스트 생성, 리스트 접근과 변경, 리스트 값 추가/삭제, 예제





```python
# 생성
# 접근과 변경
# 값 추가
# 값 삭제
# 예제1
# 예제2
```



## 25. 튜플

- ### 불변한 값들의 나열

- ### 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음

- ### 변경 불가능하며, 반복 가능함

- ### 항상 소괄호 형태로 정의 요소는 콤마로 구분

### 생성과 접근 - 소괄호(()) 혹은 tuple()을 통해 생성, 값에 대한 접근은 리스트와 동일하게 인덱스로 접근(값 변경은 불가능하여 추가/삭제도 불가능 함)



## 26. 레인지

### 숫자 시퀀스를 나타내기 위해 사용 - 기본형 range(n), 범위 지정 range(n, m), 범위 및 스텝 지정 range(n, m, s)

### 변경 불가능하며, 반복 가능함

## range는 숫자의 시퀀스를 나타내기 위해 사용



## 27. 비시퀀스형 컨테이너

## 28. 세트(Set)

### 유일한 값들의 모음(collection)

### 순서가 없고 중복된 값이 없음

### 수학에서의 집합과 동일한 구조를 가지며, 집합 연산도 가능

### 변경 가능하며(mutable), 반복 가능함(iterable)

### 단, 셋은 순서가 없어 반복의 결과가 정의한 순서와 다를 수 있음



## 29. 세트(set) 생성

### 중괄호({}) 혹은 set()을 통해 생성, 빈 set를 만들기 위해서는 set()을 반드시 활용해야 함

### 순서가 없어 별도의 값에 접근할 수 없음

### 순서가 없어 인덱스 접근 등 특정 값에 접근할 수 없음



## 30. 세트(set) 추가/삭제

### 값 추가는 .add()를 활용하여 추가하고자 하는 값을 전달

### 값 삭제는 .remove()를 활용하여 삭제하고자 하는 값을 전달



## 31. 셋(set) 활용

### 세트를 활용하면 다른 컨테이너에서 중복된 값을 쉽게 제거할 수 있음

### 단, 이후 순서가 무시되므로 순서가 중요한 경우 사용할 수 없음

## 리스트에서 고유한 지역의 개수는?  len(set(my_list))

## 고유한 리스트? set(my_list)



## 32. 딕셔너리

### 키-값(key-value) 쌍으로 이뤄진 모음(collection)

### key(불변 자료형만 가능(리스트, 딕셔너리 등은 불가능함))

### values(어떠한 형태든 관계 없음)

### 키와 값은 :로 구분 됩니다. 개별 요소는 ,로 구분됩니다

## 변경 가능하며(mutable), 반복 가능함(iterable)

### 딕셔너리는 반복하면 키가 반환됨



## 33. 딕셔너리(dictionary) 생성

### key와 value가 쌍으로 이뤄진 자료구조

### key는 변경 불가능한 데이터(immutable)만 활용 가능

- #### string integer float boolean tuple range

### value는 모든 값으로 설정 가능(list, dictionary 등)



## 34. 딕셔너리(dictionary) 접근



```python
movie = {
'title': '설국열차',
'genres': ['SF', '액션', '드라마'], 'open_date': '2013-08-01', 'time': 126,
'adult': False,
}

movie['genres']
# ['SF', '액션', '드라마']

movie['actors’]
Traceback (most recent call last): File "<stdin>", line 1, in <module> KeyError: 'actors'
```



\# ['SF', '액션', '드라마']

movie['actors’]
 Traceback (most recent call last): File "<stdin>", line 1, in <module> KeyError: 'actors'

</code>

## 35. 딕셔너리(dictionary) 키-값 추가 및 변경

### 이미 해당하는 키가 있다면 기존 값이 변경됩니다

```python
 students = {'홍길동': 100, '김철수': 90} students['홍길동'] = 80
# {'홍길동': 80, '김철수': 90} students['박영희'] = 95
# {'홍길동': 80, '김철수': 90, '박영희': 95}
```



## 36. 딕셔너리(Dictionary) 키-값 삭제

### 키를 삭제하고자하면 .pop()를 활용하여 삭제하고자 하는 키를 전달

```python
students = {'홍길동': 30, '김철수': 25} students.pop('홍길동')
students
# {'김철수': 25}
```

### 키가 없는 경우는 KeyError 발생

```python
 students = {'홍길동': 30, '김철수': 25} students.pop('jane')
Traceback (most recent call last):
File "<stdin>", line 1, in <module> KeyError: 'jane'
```



## 37. 제어문

### 컴퓨터(computer) caculation + remember

### 위에서 아래로 순차적으로 명령을 수행, 특정 상황에 따라 코드를 선택적으로 실행(분기/조건하거나 계속하여 실행(반복)하는 제어가 필요함

### 제어문은 순서도(flow chart)로 표현이 가능



## 38. 조건문

### 참/거짓을 판단할 수 있는 조건식과 함께 사용

### expression에는 참/거짓에 대한 조건식 - 조건이 참인 경우 이후 들여쓰기 되어있는 코드 블럭을 실행

### 이외의 경우 else 이후 들여쓰기 되어있는 코드 블럭을 실행 - else는 선택적으로 활용 가능함 

<code>if num % 2 == 1:</code> number를 2로 나누어서 나온 나머지 값이 1과 같은가?

## bool(자료형으로 참,거짓)을 유추



## 39. 복수 조건문

### 복수의 조건식을 활용할 경우 elif를 활용하여 표현함

### 복수 조건문

### 

```python
 if <expression>: # Code block
	elif <expression>:
    # Code block
	elif <expression>:
    # Code block
	else:
		# Code block
    
 dust = 80
if dust > 150: 
  print('매우 나쁨')
elif dust > 80: 
  print('나쁨')
elif dust > 30: 
  print('보통')
else: 
  print('좋음')
print('미세먼지 확인 완료')

dust = -10
if dust > 150: 
  print('매우 나쁨') 
  if dust > 300:
		print('실외 활동을 자제하세요.') 
elif dust > 80:
	print('나쁨') 
elif dust > 30:
	print('보통') 
else:
		if dust >= 0: 
      print('좋음')
		else:
			print('값이 잘못되었습니다.')
```



## 40. 중첩 조건문

## 조건문은 다른 조건문에 중첩되어 사용될 수 있음

### 들여쓰기를 유의하여 작성할 것



## 41. 조건표현식(conditional expression)

### 

```python
<true인 경우 값> if <expression> else <false인 경우 값>

value = num if num >= 0 else -num

value = num if num >= 0 else -num
			참일 경우 <expression> 	 거짓일 경우
  

value = num if num >= 0 else -num 
			참일 경우 <expression>   거짓일 경우
  
 num = int(input())
	value = num if num >= 0 else -num 
	print(value)
  
 num = int(input())
	value = num if num >= 0 else -num 
  print(value)
  
 num = 2
if num % 2:
		result = '홀' 
else:
		result = '짝' 
print(result)

num = 2
result = '홀' if num % 2 else '짝' 
print(result)

 num = -5
value = num if num >= 0 else 0 
print(value)

 num = -5
if num >= 0:
    value = num
else:
    value = 0
print(value)
```

## 42. 반복문

### 특정 조건을 도달할 때까지, 계속 반복되는 일련의 문장



## 43. 반복문의 종류

### while 문 - 종료조건에 해당하는 코드를 통해 반복문을 종료시켜야 함

### for 문 - 반복가능한 객체를 모두 순회하면 종료

### 반복 제어 - break continue for-else



## 44. while

### while문은 조건식이 참인 경우 반복적으로 코드를 실행 

### 조건이 참 - 들여쓰기 되어있는 코드 블록이 실행됨 - 코드 블록이 모두 실행되고 다시 조거식을 검사하며 반복적으로 실행됨 - 종료조건이 반드시 필요

```python
a = 0
while a < 5:
  print(a)
  a += 1
print('끝')
ㅡㅡ
# 1부터 사용자가 입력한 양의 정수까지의 총합을 구하는 코드를 작성하시오
# 값 초기화
n = 0
total = 0
user_input = int(input())

while n <= user_input:
  total += n
  n += 1
print(total)

```

## 45.  for

### for문은 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable) 요소를 모두 순회함, 처음부터 끝까지 모두 순회하므로 별도의 종료조건이 필요하지 않음



## 46. for문 일반 형식

### iterable, 순회할 수 있는 자료형(str, list, dict) 순회형 함수(range, enumerate)



## 47. 문자열 순회

### 사용자가 입력한 문자를 한 글자씩 세로로 출력하시오

```python
chars = input()

for char in chars:
  print(char)

# 사용자가 입력한 문자를 range를 활용하여 한 글자씩 출력하시오
chars = input()

for idx in range(len(chars)):
  print(chars[idx])
  
```



## 48. enumerate 순회

### enumerate() 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환, (index, value) 형태의 tuple로 구성된 열거 객체를 반환

```python
members = ['민수', '영희', '철수']

for i in range(len(members)):
  print(f'{i} {members[1]}')
  
for i, member in enumerate(members):
  print(i, member)
 
enumerate(members)
list(enumerate(members)) # 숫자와 값의 tuple
list(enumerate(members, start=1)) # 기본값 0, start를 지정하면 해당 값부터 순차적으로 증가
  
```



## 49. 딕셔너리 순회

### 딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용

```python
grades = {'john': 80, 'eric': 90}
for name in grades:
  print(name)
  
grades = {'john': 80, 'eric': 90}
for name in grades:
  print(name)
```



## 50. 반복문 제어

### break 반복문을 종료 continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행 for-else 끝까지 반복문을 실행한 이후에 else문 실행(break를 통해 중간에 종료되는 경우 else 문은 실행되지 않음)

```python
for i in range(10):
	if i > 1:
		print('0과 1만 필요해!')
		break
print(i)
# 0
# 1
# 0과 1만 필요해!

n = 0
while True:
  if n == 3:
    break
  print(n)
  n += 1
# 0
# 1
# 2

for i in range(6):
  if i % 2 == 0;
  	continue
  print(i)
# 1
# 3
# 5

for char in 'apple':
  if char == 'b':
    print('b!')
    break
else:
  print('b가 없습니다.')
# b가 없습니다.

for char in 'banana':
  if char == 'b':
    print('b!')
    break
else:
  print('b가 없습니다.')
# b!
```

## 51. 함수의 정의

### 함수(function) 특정한 기능을 하는 코드의 조각(묶음) 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에만 호출하여 간편히 사용

### 사용자 함수 구현되어 있는 함수가 없는 경우, 사용자가 직접 함수를 작성 가능



## 52. 함수를 사용해야 하는 이유

### 초기 값 설정 표준편차 계산 재사용이 가능한가?

### 내장함수(built-in function) 활용

### pstdev 함수 (파이썬 표준 라이브러리 - statistics)

### keyword name parameters return docstring function body



## 53. 함수 기본 구조

### 선언과 호출 (define & call) 입력 (input) 범위 (scope) 결과값(output)



## 54. 선언과 호출

### 함수의 선언은 def 키워드를 활용함 들여쓰기를 통해 function body(실행될 코드 블록)를 작성함 함수는 parameter를 넘겨줄 수 있음 함수는 동작 후에 return을 통해 결과값을 전달함



## 55. 선언 및 호출

### 함수는 함수명()으로 호출 parameter가 있는 경우, 함수명(값1, 값2, ...)로 호출



## 56. 함수의 결과값 (output)

### 함수는 반드시 값을 하나만 return한다. 명시적인 return이 없는 경우에도 none을 반환한다.

### 함수는 return과 동시에 실행이 종료된다.

```python
# 튜플 반환
def minus_and_product(x, y):
  return x - y, x * y

minus_and_product(4, 5)
```

## 57. return vs print

### return은 함수 안에서 값을 반환하기 위해 사용되는 키워드 print는 출력을 위해 사용되는 함수



## 58. parameter vs argument

### parameter: 함수를 실행할 때, 함수 내부에서 사용되는 식별자

### argument: 함수를 호출 할 때, 넣어주는 값 함수 호출 시 함수의 parameter를 통해 전달되는 값 argument는 소괄호 안에 할당 func_name(argument)

### 필수 argument(반드시 전달되어야 하는 argument), 선택 argument(값을 전달하지 않아도 되는 경우는 기본 값이 전달)



## 59. positional arguments

### 기본적으로 함수 호출 시 Argument는 위치에 따라 함수 내에 전달됨

```
def add(x, y):		add(2, 3)
		return x + y
		
def add(x, y):		add(x=2, y=5)
		return x + y	add(2, y=5)
		
def add(x, y=0):  add(2)
		return x + y

def add(*args):		add(2)
		for arg in args:	add(2, 3, 4, 5)
		print(arg)

def family(**kwargs):
		for key, value in kwargs:
			print(key, ":", value)
family(father='John', mother='Jane', me='John Jr.')
```



## 60. keyword arguments

### 직접 변수의 이름으로 특정 Argument를 전달할 수 있음 keyword argument 다음에 positional argument를 활용할 수 없음



## 61. Default arguments values

### 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함, 정의된 것 보다 더 적은 개수의 argument들로 호출 될 수 있음



## 62. 정해지지 않은 개수의 arguments

### 여러 개의 positional argument를 하나의 필수 parameter로 받아서 사용, 몇 개의 positional argument를 받을지 모르는 함수를 정의할 때 유용

### argument들은 튜플로 묶여 처리되며, parameter에 *를 붙여 표현

### 함수가 임의의 개수 argument를 keyword argument로 호출될 수 있도록 지정

### argument들은 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현



## 63. 함수의 scope

### 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분

### scope(global scope 코드 어디에서든 참조할 수 있는 공간 local scope 함수가 만든 scope 함수 내부에서만 참조 가능)

### variable(global variable global scope에 정의된 변수 local variable local scope에 정의된 변수 )



## 64. 객체 수명주기

### 객체는 각자의 수명주기(lifecycle)가 존재 built-in scope 파이썬이 실행된 이후부터 영원히 유지 global scope 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지 local scope 함수가 호출될 때 생성되고 함수가 종료될 때까지 유지

```python
 def func(): 
    a = 20
    print('local', a)

func() 
print('global', a)
# local 20
```



## 65. 이름 검색 규칙(Name resolution)

### 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음

### 아래와 같은 순서로 이름을 찾아나가며, LEGB rule이라고 부름 (Local scope: 함수, enclosed scope: 특정 함수의 상위 함수, global scope: 함수 밖의 변수 import 모듈, built-in scope: 파이썬 안에 내장되어 있는 함수 또는 속성)

### 즉 함수 내에서는 바깥 scope의 변수에 접근 가능하나 수정은 할 수 없음

```python
print(sum) 
print(sum(range(2))) 
sum = 5
print(sum) 
print(sum(range(2)))
```



## 66. 내장 함수 응용

### 파이썬 인터프리터에는 사용할 수 있는 많은 함수와 형(type)이 내장되어 있음



## 67. map(function, iterable)

### 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)적용하고, 그 결과를 map object로 반환, 리스트 형변환을 통해 결과 직접 확인



## 68. map

### 알고리즘 문제 풀이시 input 값들을 숫자로 바로 활용하고 싶을 때



## 69. 선언적 지식(declarative knowledge), 명령적 지식(imperative knowledge)



## 70. 변수와 타입(int, float, complex, bool, str, list, tuple, range, set, dictionary)

```python
word = 'happy!'
cnt = 0
for char in word:
		cnt += 1
```



## 71. 시퀀스(순서가 있는 데이터 구조) - 문자열(string) 리스트(list)



## 72. 문자열(string type)

### 문자들의 나열(sequence of characters)- 모든 문자는 str 타입

### 문자열의 작은 따옴표(')나 큰 따옴표(")를 활용하여 표기- 문자열을 묶을 때 동일한 문장부호를 활용, PEP8에서는 소스코드 내에서 하나의 문장부호를 선택하여 유지하도록 함



## 73. 문자열 탐색/검증

### s.find(*x*)  x의 첫 번째 위치를 반환. 없으면, -1을 반환

### s.index(x) x의 첫 번째 위치를 반환. 없으면, 오류 발생

### s.isalpha() 알파벳 문자 여부 *단순 알파벳이 아닌 유니코드 상 Letter (한국어도 포함)
### s.isupper() 대문자 여부

### s.islower() 소문자 여부

### s.istitle() 타이틀 형식 여부



## 74. 문자열 탐색

### .find(x) x의 첫 번째 위치를 반환. 없으면, -1을 반환함

```python
print('apple'.find('p'))
# 1
print('apple'.find('k'))
# -1
```

### .index(x) x의 첫 번째 위치를 반환. 없으면, 오류 발생

```python
print('apple'.index('p'))
# 1
'apple'.index('k')
```



## 75. 문자열 관련 검증 메소드

```python
print('abc'.isalpha()) 
# True 
print('Ab'.isupper()) 
# False 
print('ab'.islower()) 
# True
print('Title Title!'.istitle())
# True
```



## 76. 문자열 변경

### s.replace(*old, new[,count]*) 바꿀 대상 글자를 새로운 글자로 바꿔서 반환 count를 지정하면 해당 개수만큼만 시행

```python
print('coone'.replace('o', 'a’))
# caane
print('wooooowoo'.replace('o', '!', 2)) 
# w!!ooowoo
```



### s.strip(*[chars]*) 공백이나 특정 문자를 제거 양쪽을 제거하거나(strip), 왼쪽을 제거하거나(lstrip) 오른쪽을 제거(rstrip) 문자열을 지정하지 않으면 공백을 제거함

```python
print(' 와우!\n'.strip())
# '와우!'
print(' 와우!\n'.lstrip())
# '와우!\n'
print(' 와우!\n'.rstrip())
#' 와우!'
print('안녕하세요????'.rstrip('?’))
# '안녕하세요'                         
```



### s.split(*sep=None, maxsplit=-1*) 공백이나 특정 문자를 기준으로 분리 문자열을 특정한 단위로 나눠 리스트로 반환 sep이 none이거나 지정되지 않으면 연속된 공백문자를 단일한 공백문자로 간주하고 선행/후행 공백은 빈 문자열에 포함시키지 않음 maxsplit이 -1인 경우에는 제한이 없음

```python
print('a,b,c'.split('_’))
# ['a,b,c']                    
print('a b c'.split())
# ['a', 'b', 'c']                    
```



### '*separator*'.join(*[iterable]*) 구분자로 iterable을 합침

```python
print(''.join(['3', '5']))
# 35
```

### s.capitalize() 가장 첫 번째 글자를 대문자로 변경

### s.title() '나 공백 이후를 대문자로 변경

### s.upper() 모두 대문자로 변경

### s.lower() 모두 소문자로 변경

### s.swapcase() 대↔ 소문자 서로 변경



## 77. 기타 변경

### 문자열 변경 예시

```python
msg = 'hI! Everyone.' 
print(msg) 
print(msg.capitalize()) 
print(msg.title()) 
print(msg.upper()) 
print(msg.lower()) 
print(msg.swapcase())
```



## 78. 리스트(List) 정의

### 변경 가능한 값들의 나열된 자료형 순서를 가지며 서로 다른 타입의 요소를 가질 수 있음 변경 가능하며(mutable)  반복 가능함(iterable) 항상 대괄호 형태로 정의하며 요소는 콤마로 구분 [0, 1, 2, 3, 4, 5]

### L.append(x)  리스트 마지막에 항목 x를 추가

### L.insert(i, x) 리스트 인덱스 i에 항목 x를 삽입

### L.remove(x) 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거 항목이 존재하지 않을 경우, ValueError

### L.pop() 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거

### L.pop(i) 리스트의 인덱스 i에 있는 항목을 반환 후 제거

### L.extend(m) 순회형 m의 모든 항목들의 리스트 끝에 추가 (+=과 같은 기능)

### L.index(x, start, end) 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환

### L.reverse() 리스트를 거꾸로 정렬

### L.sort() 리스트를 정렬 (매개변수 이용가능)

### L.count(x) 리스트에서 항목 x가 몇 개 존재하는지 갯수를 반환



## 79. 값 추가 및 삭제

### .append(x) 리스트에 값을 추가함

```python
cafe = ['starbucks', 'tomntoms', 'hollys']
print(cafe)
cafe.append('banapresso')
print(cafe)
```

### .extend(iterable) 리스트에 iterable의 항목을 추가함

```python
cafe = ['starbucks', 'tomntoms', 'hollys’]
print(cafe)
cafe.extend(['cafe', 'test’])
print(cafe)
```

### .insert(i, x) 정해진 위치 i에 값을 추가함

### .remove(x)  리스트에서 값이 x인 것 삭제

### .pop(i) 정해진 위치 i에 있는 값을 삭제하고 그 항목을 반환함 i가 지정되지 않으면 마지막 항목을 삭제하고 반환함





