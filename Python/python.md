 



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

```python
numbers = ['hi', 1, 2, 3] 
# ['hi', 1, 2, 3] 
pop_number = numbers.pop() 
print(pop_number)
#3
print(numbers)
# ['hi', 1, 2]

numbers = ['hi', 1, 2, 3] 
# ['hi', 1, 2, 3] 
pop_number = numbers.pop(0) 
print(pop_number)
# 'hi'
print(numbers)
# [1, 2, 3]
```

### clear() 모든 항목을 삭제함

```python
 numbers = [1, 2, 3] 
 print(numbers)
# [1, 2, 3] 
print(numbers.clear()) 
# []
```

### .index(x) x값을 찾아 해당 index 값을 반환

````python
numbers = [1, 2, 3, 4] 
print(numbers)
# [1, 2, 3, 4] 
print(numbers.index(3)) 
#2 
````

### .count(x) 원하는 값의 개수를 반환함

```python
numbers = [1, 2, 3, 1, 1] 
print(numbers.count(1)) 
#3 
print(numbers.count(100)) 
#0
```

### .sort() 원본 리스트를 정렬함 None 반환 sorted 함수와 비교할 것

```python
numbers = [3, 2, 5, 1] 
result = numbers.sort() 
print(numbers, result) 
# [1, 2, 3, 5] None

numbers = [3, 2, 5, 1] 
result = sorted(numbers) 
print(numbers, result)
# [3, 2, 5, 1][1, 2, 3, 5]
```

### .reverse() 순서를 반대로 뒤집음(정렬하는 것이 아님). None 반환

```python
numbers = [3, 2, 5, 1] 
result = numbers.reverse() 
print(numbers, result)
# [1, 5, 2, 3] None
```



## 80. 컬렉션(순서가 없는 데이터 구조)

### 세트(set) - 유일한 값들의 모음(collection) 순서가 없고 중복된 값이 없음 수학에서의 집합과 동일한 구조를 가지며 집합 연산도 가능 변경 가능하며(mutable) 반복 가능함(iterable) 단 세트는 순서가 없어 반복의 결과가 정의한 순서와 다를 수 있음



## 81. 세트 메서드

### s.copy() 세트의 얕은 복사본을 반환

### s.add(x) 항목 x가 세트 s에 없다면 추가

### s.pop() 세트s에서 랜덤하게 항목을 반환하고, 해당 항목을 제거 세트가 비어 있을 경우, KeyError

### s.remove(s) 항목 x를 세트 s에서 삭제 항목이 존재하지 않을 경우, KeyError
### s.discard(x) 항목 x가 세트 s에 있는 경우, 항목 x를 세트s에서 삭제

### s.update(t) 세트 t에 있는 모든 항목 중 세트 s에 없는 항목을 추가

### s.clear() 모든 항목을 제거

### s.isdisjoint(t) 세트 s가 세트 t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우, True반환

### s.issubset(t) 세트 s가 세트 t의 하위 세트인 경우, True반환

### s.issuperset(t) 세트 s가 세트 t의 상위 세트인 경우, True반환



## 82. 딕셔너리(dictionary)

### 키-값(key-value) 쌍으로 이뤄진 모음(collection)

### key(불변 자료형만 가능(리스트, 딕셔너리 등은 불가능함))

### values(어떠한 형태든 관계 없음)

### 키와 값은 :로 구분 됩니다. 개별 요소는 ,로 구분됩니다

## 변경 가능하며(mutable), 반복 가능함(iterable)

### 딕셔너리는 반복하면 키가 반환됨

```python
students = {'홍길동': 30, '김철수': 25} 
students['홍길동']
# 30
```



## 83. 딕셔너리(dictionary)

### d.clear() 모든 항목을 제거

### d.keys() 딕셔너리 d의 모든 키를 담은 뷰를 반환

### d.values() 딕셔너리 d의 모든 값를 담은 뷰를 반환

### d.items() 딕셔너리 d의 모든 키-값의 쌍을 담은 뷰를 반환

### d.get(k) 키 k의 값을 반환하는데, 키 k가 딕셔너리 d에 없을 경우 None을 반환

### d.get(k, v) 키 k의 값을 반환하는데, 키 k가 딕셔너리 d에 없을 경우 v을 반환

### d.pop(k) 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제하는데, 키 k가 딕셔너리 d에 없을 경우 KeyError를 발생

### d.pop(k, v) 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제하는데, 키 k가 딕셔너리 d에 없을 경우 v를 반환

### d.update([*other*]) 딕셔너리 d의 값을 매핑하여 업데이트



## 84. 조회

### .get(key[,default]) key를 통해 value를 가져옴 keyerror가 발생하지 않으며 default값을 설정할 수 있음(기본: none)

```python
my_dict = {'apple': '사과', 'banana': '바나나'} print(my_dict.get('pineapple'))
# None
print(my_dict.get('apple'))
# 사과 
print(my_dict.get('pineapple', 0)) 
#0
```

## 85. 추가 및 삭제

### .pop(key[,default]) key가 딕셔너리에 있으면 제거하고 해당 값을 반환 그렇지 않으면 default를 반환 default값이 없으면 keyerror

```python
my_dict = {'apple': '사과', 'banana': '바나나'} 
data = my_dict.pop('apple')
print(data, my_dict)
# 사과 {'banana': '바나나'}
```

### .update([other]) 값을 제공하는 key value로 덮어씁니다

```python
my_dict = {'apple': '사', 'banana': '바나나'} 
my_dict.update(apple='사과')
print(my_dict)
# {‘apple’: ‘사과’, 'banana': '바나나'}
```

## 86. 에러 예외 처리(Error/exception handling)

## 87. 디버깅 

## 제어가 되는 시점 조건 반복, 함수

### branches 모든 조건이 원하는대로 동작하는지

### for loops 반복문이 진입하는지. 원하는 횟수만큼 실행되는지

### while loops for loops와 동일, 종료조건이 제대로 동작하는지

### function 함수 호출시 함수 파라미터 함수 결과

### 코드의 상태를 신중하게 출력해가며 심사숙고하는 것보다 효과적인 디버깅 도구는 없습니다.” — 브라이언 커니핸, Unix for Beginners.

### print 함수 활용 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각

### 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용 breakpoint, 변수 조회 등

### Python tutor 활용 (단순 파이썬 코드인 경우) 뇌컴파일, 눈디버깅

### 코드를 작성하다가 에러 메시지시가 발생하는 경우 해당 하는 위치를 찾아 메시지를 해결

### 로직 에러가 발생하는 경우 명시적인 에러 메시지 없이 예상과 다른 결과가 나온 경우 정상적으로 동작하였던 코드 이후 작성된 코드를 생각해봄 전체 코드를 살펴봄 휴식을 가져봄 누군가에게 설명해봄



## 88. 문법 에러(syntax error)

### syntax error가 발생하면 파이썬 프로그램은 실행이 되지 않음

### 파일이름, 줄번호, ^ 문자를 통해 파이썬이 코드를 읽어 나갈 때(parser) 문제가 발생한 위치를 표현

### 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret)기호(^)를 표시

### EOL (End of Line)

### EOF (End of File)

### invalid syntax

### assign to literal



## 89. 예외(exception)

### 실행 도줄 예상치 못한 상황을 맞이하면 프로그램 실행을 멈춤

### 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러

### 실행 중에 감지되는 에러들을 예외(Exception)라고 부름

### 예외는 여러 타입(type)으로 나타나고 타입이 메시지의 일부로 출력됨 nameerror, type error 등은 발생한 예외 타입의 종류(이름)

### 모든 내장 예외는 exception class를 상속받아 이뤄짐

### 사용자 정의 예외를 만들어 관리할 수 있음

### ZerodivisionError(0으로 나누고자 할 때 발생), NameError(namespace 상에 이름이 없는 경우)

### TypeError, TypeError 타입 불일치, TypeError argument 개수 초과, 타입은 올바르나 값이 적절하지 않거나 없는 경우, indexerror, keyerror, modulenotfounderror, 존재하지 않는 모듈을 import 하는 경우, import error

### importerror module은 있으나 존재하지않는 클래스/함수를 가져오는 경우

### indentationerror indentation이 적절하지 않는 경우

### keyboardinterrupt 임의로 프로그램을 종료하였을 때



## 90. 파이썬 내장 예외 (built-in-exceptions)

## 91. 예외처리

### try 문(statement) / except 절(clause)을 이용하여 예외 처리를 할 수 있음

### try문 오류가 발생할 가능성이 있는 코드를 실행, 예외가 발생되지 않으면 except 없이 실행 종료

### except문 예외가 발생하면 except 절이 실행 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함

```python
num = input('숫자입력 :') 
print(int(num))
# 숫자입력 :3
# 3

try:
	num = input('숫자입력 :') 
	print(int(num))
except ValueError: 
  print('숫자가 아닙니다')
```



## 92. 복수의 예외처리 실습

### 100을 사용자가 입력한 값으로 나누고 출력하는 코드를 작성

```python
try:
	num = input('값을 입력하시오: ') 
  100/int(num)
except ValueError: 
  print('숫자를 넣어주세요.')
except ZeroDivisionError: 
  print('0으로 나눌 수 없습니다.')
except:
	print('에러는 모르지만 에러가 발생하였습니다.')
```

## 93. 정리

### try 코드를 실행함

### except try 문에서 예외가 발생 시 실행함

### else try 문에서 예외가 발생하지 않으면 실행함

### finally 예외 발생 여부와 관계없이 항상 실행함



## 94. 예외처리 예시

### 파일을 열고 읽는 코드를 작성하는 경우 

### 파일 열기 시도 해당 파일 읽기 작업 종료 메시지 출력

### 파일을 열고 읽는 코드를 작성하는 경우 파일 열기 시도 '해당 파일이 없습니다' 출력 (except)

### 파일이 있는 경우 파일 내용을 출력 (else)

### 해당 파일 읽기 작업 종료 메시지 출력(finally)



## 95. 예외 발생 시키기

### raise statement raise를 통해 예외를 강제로 발생

### raise <표현식>(메시지) 예외 타입 지정(주어지지 않을 경우 현재 스코프에서 활성화된 마지막 예외를 다시 일으킴)



## 96. 객체

### 123, 900, 5는 모두 int의 인스턴스

### 'hello', 'bye'는 모두 string의 인스턴스

### [232, 89, 1], []은 모두 list의 인스턴스

### 객체(object)의 특징  

### 타입(type) 어떤 연산자(operator)와 조작(method)이 가능한가?

### 속성(attribute)  어떤 상태(데이터)를 가지는가?

### 조작법(method) 어떤 행위(함수)를 할 수 있는가?

### 객체지향 프로그래밍이란? 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법

## 97. 절차지향 프로그래밍

### 절차지향 프로그래밍 데이터와 함수로 인한 변화  

## 98. 객체지향 프로그래밍

### 데이터와 기능(메소드) 분리, 추상화된 구조(인터페이스) 현실 세계를 프로그램 설계에 반영(추상화)



## 99. 객체 지향 프로그래밍

### 현실 세계를 프로그램 설계에 반영(추상화) 사각형 넓이 구하기 코드



## 100. 예시 절차지향 프로그래밍

```python
def area(x, y):
  return x * y
def circumference(x, y):
  return 2 * (x + y)

a = 10
b = 30
square1_area = a * b
square1_circumference = 2 * (a + b)

c = 300
d = 20
square2_area = c * d
square2_circumference = 2 * (c + d)
```

## 101. 예시 객체지향 프로그래밍

```python
class Rectangle:
	def __init__(self, x, y):
    self.x = y
    self.y = y
    
  def area(self):
    return self.x * self.y
  
  def circumference(self):
    return 2 * (self.x + self.y)
  
r1 = Rectangle(10, 30)
r1.area()
r1.circumference()

r2 = Rectangle(300, 20)
r2.area()
r2.circumference()
```



## 102. 객체 지향 프로그래밍

### 사각형 - 클래스(class)

### 각 사각형(R1, R2) - 인스턴스(instance)

### 사각형의 정보 - 속성(attribute) - 가로 길이, 세로 길이

### 사각형의 행동 기능 - 메소드(method) - 넓이를 구한다 높이를 구한다



## 103. 객체지향의 장점(위키디피아)

### 객체 지향 프로그래밍은 프로그램을 유연하고 변경이 용이하게 만들기 때문에 대규모 소프트웨어 개발에 많이 사용됩니다. 

### 또한, 프로그래밍을 더 배우기 쉽게 하고 소프트웨어 개발과 보수를 간편하게 하며, 보다 직관적인 코드 분석을 가능하게 하는 장점을 가지고 있습니다



## 104. OOP 기초

```python
# 클래스 정의 
class MyClass:
	pass
# 인스턴스 생성 
my_instance = MyClass() 
# 메서드 호출 
my_instance.my_method() 
# 속성 
my_instance.my_attribute
```

## 105.  OOP 기초 기본 문법

### 객체의 틀(클래스)을 가지고 객체(인스턴스)를 생성한다

### 클래스와 인스턴스 클래스 객체들의 분류(class) 인스턴스 하나하나의 실체 예(instance)

### 파이썬은 모든 것이 객체, 모든 객체는 특정 타입의 인스턴스

### 속성 특정 데이터 타입 클래스의 객체들이 가지게 될 상태 데이터를 의미

### 메소드 특정 데이터 타입 클래스의 객체에 공통적으로 적용 가능한 행위(함수)



### 객체 비교하기 

### == 동등한(equal) 변수가 참조하는 객체가 동등한(내용이 같은) 경우 true 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님

### is 동일한(identical) 두 변수가 동일한 객체를 가리키는 경우 true

### 객체 비교하기

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b, a is b)
# true false

a = [1, 2, 3]
b = a
print(a == b, a is b)
# true true
```

### 인스턴스 변수 인스턴스가 개인적으로 가지고 있는 속성(attribute) 각 인스턴스들의 고유한 변수

### 생성자 메소드에서 self.<name>으로 정의

### 인스턴스가 생성된 이후 <instance>.<name>으로 접근 및 할당



## 인스턴스 메소드

### 인스턴스 변수를 사용하거나 인스턴스 변수에 값을 설정하는 메소드

### 클래스 내부에 정의되는 메소드의 기본

### 호출 시 첫번째 인자로 인스턴스 자기자신(self)이 전달됨



### self 인스턴스 자기자신

### 파이썬에서 인스턴스 메소드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계

### 매개변수 이름으로 self를 첫번째 인자로 정의 다른 단어로 써도 작동하지만 파이썬의 암묵적인 규칙



### 생성자(constructor) 메소드  인스턴스 객체가 생성될 때 자동으로 호출되는 메소드 인스턴스 변수들의 초기값을 설정 

```python
class person:
  
  def __init__(self):
    print('인스턴스가 생성되었습니다.')
# person1 = person()    
    
class person:
  
  def __init__(self, name):
    print(f'인스턴스가 생성되었습니다. {name}')
# person1 = person('지민')
```

### 소멸자(destructor) 메소드 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메소드



## 106. 클래스

### 클래스 속성(attribute) 한 클래스의 모든 인스턴스라도 똑같은 값을 가지고 있는 속성 클래스 선언 내부에서 정의 <classname>.<name>으로 접근 및 할당

### 인스턴스와 클래스 간의 이름 공간(namespace) 

### 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성

### 인스턴스를 만들면 인스턴스 객체가 생성되고 이름 공간 생성

### 인스턴스에서 특정 속성에 접근하면 인스턴스-클래스 순으로 탐색



## 107. 클래스 메소드 

### 클래스가 사용할 메소드 

### @classmethod 데코레이터를 사용하여 정의  데코레이터 함수를 어떤 함수로 꾸며서 새로운 기능을 부여

### 호출 시 첫번째 인자로 클래스(cls)가 전달됨

### 스태틱 메소드 인스턴스 변수 클래스 변수를 전혀 다루지 않는 메소드

### 언제 사용하는가? 속성을 다루지 않고 단지 기능(행동)만을 하는 메소드를 정의할 때 사용

### @staticmethod 데코레이터를 사용하여 정의

### 호출 시 어떠한 인자도 전달되지 않음 (클래스 정보에 접근 수정 불가)



### 정리

### 클래스 구현 - 클래스 정의, 데이터 속성 정의(객체의 정보는 무엇인지), 메소드 정의 (객체를 어떻게 사용할 것인지)

### 클래스 활용 - 해당 객체 타입의 인스턴스 생성 및 조작



## 108. 메소드 정리

### 인스턴스 메소드 호출한 인스턴스를 의미하는 self 매개 변수를 통해 인스턴스를 조작

### 클래스 메소드 클래스를 의미하는 cls 매개 변수를 통해 클래스를 조작

### 스태틱 메소드 인스턴스나 클래스를 의미하는 매개변수는 사용하지 않음 즉 객체 상태나 클래스 상태를 수정할 수 없음 

### 일반 함수처럼 동작하지만 클래스의 이름공간에 귀속 됨 주로 해당 클래스로 한정하는 용도로 사용



## 109. 객체 지향의 핵심개념

### 객체지향의 핵심 4가지 추상화 상속 다형성 캡슐화

### 추상화

```python
class student:
	def __init__(self, name, age, gpa):
    self.name = name
    self.age = age
    self.gpa = gpa
    
  def talk(self):
    print(f'반갑습니다. {self.name}입니다.')
    
  def study(self):
    self.gpa += 0.1
    
    
class student:
  
  def __init__(self, name, age, department):
    self.name = name
    self.age = age
    self.department = department
    
  def talk(self):
    print(f'반갑습니다. {self.name}입니다.')
    
  def teach(self):
    self.age += 1
    
    
class person:
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def talk(self):
    print(f'반갑습니다. {self.name}입니다.')
    
    
```



### 상속 두 클래스 사이 부모 자식 관계를 정립하는 것 클래스는 상속이 가능함 모든 파이썬 클래스는 object를 상속 받음

### 하위 클래스는 상위 클래스에 정의된 속성 행동 관계 및 제약 조건을 모두 상속 받음

### 부모클래스의 속성 메소드가 자식 클래스에 상속되므로 코드 재사용성이 높아짐

### 상속 관련 함수와 메소드 issubclass(class, classinfo) 

### class가 classinfo의 subclass면 true classinfo는 클래스 객체의 튜플일 수 있으며 classinfo의 모든 항목을 검사

### 상속 관련 함수와 메소드 super() 자식클래스에서 부모클래스를 사용하고 싶은 경우



### 상속 정리 파이썬의 모든 클래스는 object로부터 상속됨

### 부모 클래스의 모든 요소(속성 메소드)가 상속됨

### super()를 통해 부모 클래스의 요소를 호출할 수 있음

### 메소드 오버라이딩을 통해 자식 클래스에서 재정의 가능함

### 상속관계에서의 이름 공간은 인스턴스 자식 클래스 부모 클래스 순으로 탐색



### 다중 상속 두개 이상의 클래스를 상속 받는 경우

### 상속 받은 모든 클래스의 요소를 활용 가능함

### 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨





## 110. 다형성(polymorphism) 이란

### 여러 모양을 뜻하는 그리스어

### 동일한 메소드가 클래스에 따라 다르게 행동할 수 있음을 의미

### 즉 서로 다른 클래스에 속해있는 객체들이 동일한 메시지에 의해 다른 방식으로 응답될 수 있음



### 메소드 오버라이딩 상속 받은 메소드를 재정의

### 클래스 상속 시 부모 클래스에서 정의한 메소드를 자식 클래스에서 변경

### 부모 클래스의 메소드 이름과 기본 기능은 그대로 사용하지만 특정 기능을 바꾸고 싶을 때 사용





## 111. 캡슐화

### 객체 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단

### 파이썬에서 기능상으로 존재하지 않지만 관용적으로 사용되는 표현이 있음



### 접근제어자 종류

### public access modifier 언더바 없이 시작하는 메소드나 속성

### 어디서나 호출이 가능 하위 클래스 override 허용

### protected access modifier 언더바 1개로 시작하는 메소드나 속성

### 암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능

### private access modifier 언더바 2개로 시작하는 메소드나 속성

### 본 클래스 내부에서만 사용이 가능



## 112. list comprehension

### 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

[<expression> for <변수> in <iterable>]

[<expression> for <변수> in <iterable> if <조건식>]



### 1~3의 세제곱의 결과가 담긴 리스트를 만드시오

```python
cubic_list = []
for number in range(1, 4):
  cubic_list.append(number**3)
print(cubic_list)

[number**3 for number in range(1, 4)]
# 특정한 원소(요소)로 구성된 리스트 만들 때
```



## 113. Dictionary comprehension

### 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

{key: value for <변수> in <iterable>}

{key: value for <변수> in <iterable> if <조건식>}



### 1~3의 세제곱의 결과가 담긴 딕셔너리를 만드시오

```python
cubic_dict = {}
for number in range(1, 4):
	cubic_dict[number] = number ** 3
print(cubic_dict)

{number: number**3 for number in range(1, 4)}
```



## 114. lambda [parameter] : 표현식

### 람다함수 표현식을 계산한 결과값을 반환하는 함수로 이름이 없는 함수여서 익명함수라고도 불림

### 특징 return문을 가질 수 없음 간편 조건문 외 조건문이나 반복문을 가질 수 없음

### 장점 함수를 정의해서 사용하는 것보다 간결하게 사용 가능 def를 사용할 수 없는 곳에서도 사용가능



## 115. filter

### filter(function, iterable)

### 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)적용하고 그 결과가 true인 것들을 filter object로 반환

```python
def odd(n):
	return n % 2
numbers = [1, 2, 3]
result = filter(odd, numbers)
print(result, type(result))

list(result)
# [1, 3] 리스트 형변환을 통해 결과 직접 확인
```



## 116. 파이썬 패키지 관리자(pip) 명령어

### 패키지 설치

### $ pip install SomePackage

### $ pip install SomePackage==1.0.5

### $ pip install 'SomePackage>=1.0.4'

### 모두 bash cmd 환경에서 사용되는 명령어



### 패키지 삭제 pip는 패키지를 업그레이드 하는 경우 과거 버전을 자동으로 지워줌

### $ pip uninstall SomePackage



### 패키지 활용 명령어 패키지 목록 및 특정 패키지 정보

### $ pip list

### $ pip show SomePackage



### 패키지 freeze 설치된 패키지의 비슷한 목록을 만들지만 pip install에서 활용되는 형식으로 출력

### 해당하는 목록을 requirements.txt(관습)으로 만들어 관리함

### $ pip freeze



### 패키지 활용 명령어

### 패키지 관리하기 아래의 명령어들을 통해 패키지 목록을 관리[1]하고 설치할 수 있음[2]

### 일반적으로 패키지를 기록하는 파일의 이름은 requirements.txt로 정의함

### $ pip freeze > requirements.txt

### $ pip install –r requirements.txt



### 패키지 활용 명령어

### $ pip freeze > requirements.txt

### $ pip install –r requirements.txt

### requirements.txt를 바탕으로 설치



## 117. 가상환경

### 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip를 통해 설치를 해야함

### 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음 과거 외주 프로젝트 신규 회사 프로젝트

### 이러한 경우 가상환경을 만들어 프로젝트별로 독립적인 패키지를 관리 할 수 있음



## 118. 파이썬 실행에 대한 이해

### python은 특정 경로에 있는 프로그램을 실행시키는 것

### venv 가상 환경을 만들고 관리하는데 사용되는 모듈  특정 디렉토리에 가상 환경을 만들고 고유한 파이썬 패키지 집합을 가질 수 있음

### 특정 폴더에 가상 환경이(패키지 집합 폴더 등) 있고 실행 환경(예 bash)에서 가상환경을 활성화 시켜 해당 폴더에 있는 패키지를 관리 사용함



### 가상환경 생성하면 해당 디렉토리에 별도의 파이썬 패키지가 설치됨

### $ python -m venv <폴더명>

### $ python –m venv venv



### 가상환경 활용 아래의 명령어를 통해 가상환경을 활성화 

### <venv>는 가상환경을 포함하는 디렉토리의 이름

### 가상환경 비상활성화는 $ deactivate 명령어를 사용



### cmd와 bash 환경  가상환경 활성화 비활성화

### $ source venv/Scripts/activate



### 동일 컴퓨터에서 별도의 가상환경 

### 동일컴퓨터 프로젝트별 가상환경 

### 각 프로젝트별 가상환경(venv 폴더별로 고유한 프로젝트가 설치됨)



## 119. 입력 활용 예시

### input()은 사용자의 입력 한 줄을 문자열로 받는 함수

```python
word = input()
>>> happyhacking
```



### input()과 map함수를 이용해 원하는 대로 입력 받기

```python
# 문자열 입력 받기
a = input()

# 한 개 숫자 입력 받기
b = int(input())
c = float(input())

# 여러 개 숫자 입력 받기
d, e = map(int, input().split())
f, g, h = map(float, input().split())

```



## 120. 파이썬의 내장 함수 map(function, iterable)

```python
map(int, ["1", "2", "3"])
# 각 원소에 int를 적용
# 정수 1, 2, 3을 반환

map(float, [1, 2, 3])
# 각 원소에 float을 적용
# 부동소수점 1.0, 2.0, 3.0을 반환

map(int, "123")
# 각 원소에 int를 적용
# 리스트 뿐만 아니라 문자열에도 적용 가능 정수 1, 2, 3을 반환
```



### map으로 입력 받는 과정 

```python
a, b = map(int, input().split())
>>> 1 2

a, b = map(int, "1 2".split())
a, b = map(int, ["1", "2"])

a, b = 1, 2

a, b, c = map(int, input())
>>> 123
print(a + b + c)
>>> 6
```

### print()는 데이터를 출력할 수 있는 함수이며, 자동적으로 줄 바꿈 발생

```python
print("happy")
print("hacking")
>>> happy
>>> hacking
```

### 콤바(,)를 이용해 여러 인자를 넣으면 공백을 기준으로 출력

```python
a = "happy"
b = "hacking"

print(a, b)
>>> happy hacking
```

### end, sep 옵션을 사용하여 출력 조작하기

```python
a = "happy"
b = "hacking"

print(a, end="@")
print(b)
>>> happy@hacking

print(a, b, sep="/n")
>>> happy
>>> hacking

a, b, c = map(int, input().split())
>>> 1 2 3

print(a, b, c)
>>> 1 2 3

a, b, c = map(int, input().split())
>>> 1 2 3

print(a, b, c, end="&")
>>> 1 2 3&
```

## 121. 알고리즘의 시간 복잡도

### input을 넣은 후 output이 나오는 시간이 짧은 알고리즘!

### 알고리즘의 소요시간 측정하기 1

### 알고리즘의 소요시간 측정하기 2

### 기본연산 : 단위 시간 1이 소요되는 연산 ex)할당 산술 비교 반환

### 기본연산의 총 횟수 == 알고리즘의 소요 시간

### 아래와 같은 상황에서 몇 번의 기본연산이 일어날까? (== 알고리즘의 소요시간이 몇일까?)

```python
def count(word, char):
    total = 0
    for i in word:
        if i == char:
					total += 1 
return total

count("apple", "p")
>>> 2
```

### 기본연산의 횟수를 구하는 것은 환경에 영향을 받지 않는 객관적인 방법이지만, 입력의 개수에 따라 시간이 달라진다는 문제가 있다.

```python
def count(word, char):
    total = 0
    
    for i in word:
        if i == char:
					total += 1 
return total
```

### 따라서 성능을 측정할 때는 입력을 통일시킨다 가장 기본연산이 많이 일어나는 최악의 입력 n개가 들어온다고 가정한다. 매 반복 마다 total += 1연산 실행

```python
def count(word, char):
   total = 0
   
   for i in word:
      if i == char:
				total += 1 
return total

count("aaaa", "a")
```



### 따라서 성능을 측정할 때는 입력을 통일시킨다. 가장 기본연산이 많이 일어나는 최악의 입력 n개가 들어온다고 가정한다. 입력 n개에 따른 소요 시간을 수식으로 세울 수 있다. == 시간복잡도(time complexity)

```python
 def count(word, char):
    total = 0
    
    for i in word:
        if i == char:
          total += 1 
          
return total
```

## 122. 시간 복잡도(time complexity) 

### 계산 복잡도 이론에서 시간 복잡도는 문제를 해결하는데 걸리는 시간과 입력의 함수 관계를 가리킨다.

### 단순하게 알고리즘의 수행 시간을 의미한다고 시간 복잡도가 높다 -> 느린 알고리즘

### 시간 복잡도가 낮다 -> 빠른 알고리즘

### 선형 증가  제곱으로 증가



## 123. 빅오(big-O) 표기법이란 무엇일까?

### 입력 n이 무한대로 커진다고 가정하고 시간 복잡도를 간단하게 표시하는 것 최고차항만 남기고 계수와 상수 제거

### 매 입력에 따라 정확한 수식을 구하는 것은 불필요하다 정확한 수치보다는 증가율에 초점을 맞춘다

### 따라서 원래 둘의 소요시간은 2배 차이가 났지만 점근적 표기법에 의해 동일한 시간 복잡도를 나타냄



### O(1): 단순 산술 계산(덧셈, 뺄셈, 곱셉, 나눗셈) 

### O(logN): 크기 N인 리스트를 반절씩 순회/탐색 

### O(N): 크기 N인 리스트를 순회 

### O(NlogN): 크기 N인 리스트를 반절씩 탐색 * 순회 

### O(N^2): 크기 M, N인 2중 리스트를 순회 

### O(N^3): 3중 리스트를 순회

###  O(2^N): 크기 N 집합의 부분 집합

### O(N!): 크기 N 리스트의 순열

### O(1): 단순계산 -> a + b, 100 * 200
 ### O(logN): 이진탐색(Binary Search), 분할정복(Divide & Conquer) 

### O(N): 리스트 순회, 1중 for 문

### O(NlogN): 높은 성능의 정렬(Merge/Quick/Heap Sort) 

### O(N^2): 2중 리스트 순회, 2중 for 문

### O(N^3): 3중 리스트 순회, 3중 for 문

### O(2^N): 크기가 N인 집합의 부분 집합

### O(N!): 크기가 N인 순열



## 첫 번째 방법 – 1부터 n까지 일일히 더하기

### 문제 : 연속된 숫자 들의 합 구하기

### 제한 시간 : 1초

### 입력 : 자연수 N이 입력된다

### 출력 : 1부터 N까지의 연속된 수를 모두 더한 값을 반환한다

### 예제 입력: 10

### 예제 출력: 55

```python
def get_total(n):
  total = 0
  
  for i in range(1, n + 1):
    total += i
    
  return total
print(get_total(10))
>>> 55

print(get_total(1000000000)) 
>>> 제한 시간 1초 초과
```



## 두 번째 방법 – 가우스의 합 공식

### 문제 : 연속된 숫자 들의 합 구하기
 ### 제한 시간 : 1초
 ### 입력 : 자연수 N이 입력된다. (1 <= N <= 1,000,000,000) 

### 출력 : 1부터 N까지의 연속된 수를 모두 더한 값을 반환한다.

### 예제 입력 : 10 예제 출력 : 55

```python
def get_total(n):
return (n * (n + 1)) // 2

print(get_total(10))
>>> 55

print(get_total(1000000000))
>>> 500000000500000000
```

### 같은 output을 만드는 알고리즘이라도 시간 복잡도에 따라 성능이 달라질 수 있고 시험에서 정답 여부가 갈리는 포인트가 된다는 것이다.



## 124. 리스트

### 배열 (Array) 여러 데이터들이 연속된 메모리 공간에 저장되어 있는 자료구조

### 인덱스(index)를 통해 데이터에 빠르게 접근

### 배열의 길이는 변경 불가능 -> 길이를 변경하고 싶다면 새로 생성

### 데이터 타입은 고정

### int arr[5] = {70, 80, 20, 100, 90};



### 연결 리스트 (linked list) 데이터가 담긴 여러 노드들이 순차적으로 연결된 형태의 자료구조

### 맨 처음 노드부터 순차적으로 탐색

### 연결리스트의 길이 자유롭게 변경 가능 -> 삽입, 삭제가 편리

### 다양한 데이터 타입 저장

### 데이터가 메모리에 연속적으로 저장되지 않음



### 배열 vs 연결리스트

### 배열 인덱스 접근, 연결리스트 가변 길이 - 파이썬의 리스트 (list)



## 파이썬의 리스트

### .apped(원소) 리스트 맨 끝에 새로운 원소 삽입

```python
a = [1, 2, 3, 4, 5]
a.append(6)
print(a)
# [1, 2, 3, 4, 5, 6]

a = [1, 2, 3, 4, 5]
a.append(["a", "b"])
print(a)
# [1, 2, 3, 4, 5, ['a', 'b']]
```



### .pop(인덱스) 특정 인덱스에 있는 원소를 삭제 및 반환 

```python
a = [1, 2, 3, 4, 5]
b = a.pop()
print(a)
print(b)
# [1, 2, 3, 4, 5]

a = [1, 2, 3, 4, 5]
b = a.pop(2)
print(a)
print(b)
# [1, 2, 4, 5, 3]
```

### .count(원소) 리스트에 해당 원소의 개수를 반환

```python
a = [1, 2, 2, 3, 3, 3]
print(a.count(2))
# 2

a = [1, 2, 2, 3, 3, 3]
print(a.count(3))
# 3
```

### .index(원소) 리스트에서 처음으로 원소가 등장하는 인덱스 반환

```python
a = [1, 2, 3, 2, 5]
print(a.index(2))
# 1

a = [1, 2, 3, 2, 5]
print(a.index(8))
```

### .sort() 리스트를 오름차순으로 정렬 reverse=true 옵션을 통해 내림차순으로 정렬 가능

```python
a = [5, 2, 4, 0, -1]
a.sort()
print(a)
# [-1, 0, 2, 4, 5]

a = [5, 2, 4, 0, -1]
a.sort(reverse=true)
print(a)
# [5, 4, 2, 0, -1]
```

### .reverse() 리스트의 원소들의 순서를 거꾸로 뒤집기

```python
a = [1, 2, 3, 4, 5]
a.reverse()
print(a)
# [5, 4, 3, 2, 1]
```



## 자주 쓰이는 리스트 관련 내장 함수

### len(iterable) 리스트의 길이(원소의 개수)를 반환

```python
a = [1, 2, 3, 4, 5]
print(len(a))
# 5
```



### sum(iterable) 리스트의 모든 원소의 합을 반환

```python
a = [1, 2, 3, 4, 5]
print(sum(a))
# 15
```



### max(iterable) 리스트의 원소 중 최대값을 반환

```python
a = [1, 2, 3, 4, 5]
print(max(a))
# 5
```



### min(iterable) 리스트의 원소 중 최소값을 반환

```python
a = [1, 2, 3, 4, 5]
print(min(a))
# 1
```



### sorted(iterable) 오름차순으로 정렬된 새로운 리스트 반환 원본 리스트는 변화 없음

```python
a = [5, 2, -1, 0 , 1]
b = sorted(a)
c = sorted(a, reverse=true)

print(a) 
# 원본  [5, 2, -1, 0, 1]
print(b)
# 오름차순 정렬 [-1, 0, 1, 2, 5]
print(c)
# 내림차순 정렬 [5, 2, 1, 0, -1]
```

### reversed(iterable) 리스트의 순서를 거꾸로 뒤집은 새로운 객체 반환 원본 리스트는 변화 없음

```python
a = [1, 2, 3, 4, 5]
b = reversed(a)
c = list(reversed(a))

print(a) 
# 원본 [1, 2, 3, 4, 5]
print(b)
# reversed(a)
print(c)
# list(reversed(a)) [5, 4, 3, 2, 1]
```



## 125. 리스트 컴프리헨션(list comprehension)

### list comprehension(리스트 컴프리헨션 리스트 내포)란 코드 한 줄만으로 새로운 리스트를 만드는 방법이다.



## 126. 문자열(string)

### 문자열 immutable(변경 불가능한) 자료형!

```python
word = "apple" 
print(word) 
print(id(word))
>>> apple
>>> 1352749370800
word += " banana" 
print(word) 
print(id(word))
>>> apple banana 
>>> 1352749417520
```



## 127. 문자열 슬라이싱

## s = 'abcdefghi' s[2:5] 'cde'


## s = 'abcdefghi' s[2:5] 'cde' s[-6:-2] 'defg'

### s = 'abcdefghi' s[2:5] 'cde' s[-6:-2] 'defg' s[2:-4] 'cde'

### s = 'abcdefghi' s[2:5:2] 'ce'

### s = 'abcdefghi' s[2:5:2] 'ce' s[-6 -1:3]  'dg'

### s = 'abcdefghi' s[2:5:2] 'ce' s[-6 -1:3]  'dg' s[2:5:-1] ''



### s = 'abcdefghi'

### s[2:5:2] 'ce'

### s[-6 -1:3] 'dg'



### s = 'abcdefghi'

### s[2:5:2] 'ce'

### s[-6 -1:3] 'dg'

### s[2:5:-1] ''

### s[5:2:-1] 'fed'



### s = 'abcdefghi' s[:3] 'abc' s[5:] 'fghi'



### s = 'abcdefghi' s[:3] 'abc' s[5:] 'fghi' s[:] 'abcdefghi'



### s = 'abcdefghi' s[:3] 'abc' s[5:] 'fghi' s[:] 'abcdefghi' s[::-1] 'ihgfedcba' s[10:20] ''



## 128. 문자열 슬라이싱

### .split(기준문자) 문자열을 일정 기준으로 나누어 리스트로 반환 괄호 안에 아무것도 넣지 않으면 자동으로 공백을 기준으로 설정

```python
word = "I play the piano"
print(word.split())
# ['I', 'play', 'the', 'piano']

word = "apple, banana, orange, grape"
print(word.split(","))
# ['apple', 'banana', 'orange', 'grape']

word = "This_is_snake_case"
print(word.split("_"))
# ['This', 'is', 'snake', 'case']
```



### .strip(제거할 문자) 문자열의 양쪽 끝에 있는 특정 문자를 모두 제거한 새로운 문자열 반환 괄호 안에 아무것도 넣지 않으면 자동으로 공백을 제거 문자로 설정 제거할 문자를 여러 개 넣으면 해당하는 모든 문자들을 제거

```python
word = " Hello World"
print(word.strip())
# Hello World

word = "aHello Worlda"
print(word.strip("a"))
# Hello World

word = "Hello World"
print(word.strip("Hd"))
# ello Worl

word = "Hello Worldddddd"
print(word.strip("d"))
# Hello Worl
```



### .find(찾는 문자) 특정 문자가 처음으로 나타나는 위치(인덱스)를 반환 찾는 문자가 없다면 -1을 반환

```python
word = "apple"
print(word.find("p"))
# 1

word = "apple"
print(word.find("k"))
# -1
```



### .index(찾는 문자) 특정 문자가 처음으로 나타나는 위치(인덱스)를 반환 찾는 문자가 없다면 -1을 반환

```python
word = "apple"
print(word.find("p"))
# 1

word = "apple"
print(word.find("k"))
# valueerror
```



### .count(개수를 셀 문자) 문자열에서 특정 문자가 몇 개인지 반환 문자 뿐만 아니라 문자열의 개수도 확인 가능

```python
word = "banana"
print(word.count("a"))
# 3

word = "banana"
print(word.count("na"))
# 2

word = "banana"
print(word.count("ana"))
# 1
```



### .replace(기존 문자 새로운 문자) 문자열에서 기존 문자를 새로운 문자로 수정한 새로운 문자열 반환 특정 문자를 빈 문자열("")로 수정하여 마치 해당 문자를 삭제한 것 같은 효과 가능

```python
word = "happyhacking"
print(word.replace("happy", "angry"))
# angryhacking

word = "happyhacking"
print(word.replace("h", "H"))
# HappyHacking

word = "happyhacking"
print(word.replace("happy", ""))
# hacking
```



### 삽입할 문자.join(iterable) iterable의 각각 원소 사이에 특정 문자를 삽입한 새로운 문자열 반환 공백 출력, 콤마 출력 등 원하는 출력 형태를 위해 사용

```python
word = "happyhacking"
print("".join(word))
# h a p p y h a c k i n g

word = "happyhacking"
print(",".join(word))
# h,a,p,p,y,h,a,c,k,i,n,g

word = ["edu", "hphk.kr"]
print("@".join(word))
# edu@hphk.kr

word = ["h", "a", "p", "p", "y"]
print("",join(words))
# happy
```



### 아스키 (ASC2) 코드

### 컴퓨터는 숫자만 이해할 수 있다!

### 비트(bit) 0과 1 두 가지 정보만 표현

### 바이트(byte) 데이터를 저장하는 기본 단위 1 byte == 8 bits

### ord(문자) 문자 아스키코드로 변환하는 내장함수

### 아스키코드 문자로 변환하는 내장함수

```python
print(ord("A"))
print(ord("a"))
print(chr(65))
print(chr(97))
```



## 129. 딕셔너리(dictionary)

### 파이썬에서는 딕셔너리(dict) 자료구조가 내장 되어 있다

### Non-sequence & key-value

### key: value가 저장되는 원리가 무엇일까? 리스트를 이용해서 key: value를 저장해보자

### (Key, "Value") ( 210701, “haley” ) ( 211209, “alex” ) ( 210218, “justin” ) ( 210405, “kyle” )  List

### 순차 탐색 탐색이 많아질수록 오래 걸림

### 딕셔너리는 해시 테이블(hash table)을 이용하여 key: value를 저장

### 해시 함수: 임의 길이의 데이터를 고정 길이의 데이터로 매핑하는 함수

### 해시: 해시 함수를 통해 얻어진 값

### 파이썬의 딕셔너리(dictionary)는 해시 함수와 해시 테이블을 이용하여 삽입, 삭제, 수정, 조회 연산의 속도가 리스트보다 빠르다



## 130. 딕셔너리 기본 문법

### 기본적인 딕셔너리 사용법(선언) 변수 = {key1: value1, key2: value2 ...}

```python
a = {
		"name": "kyle"
		"gender": "male"
		"address": "Seoul"
}

print(a)
# {'name': 'kyle', 'gender': 'male', 'address': 'Seoul'}
```



### 기본적인 딕셔너리 사용법 (삽입/수정)

### 딕셔너리[key] = value 내부에 해당 key가 없으면 삽입, 있으면 수정

```python
a = {
		"name": "kyle"
  	"gender": "male"
  	"address": "Seoul"
}

a["job"] = "coach"
print(a)
# {'name': 'kyle', 'gender': 'male', 'address': 'Seoul', 'job': 'coach'} 삽입

a = {
  	"name": "kyle"
  	"gender": "male"
  	"address": "Seoul"
}

a["name"] = "justin"
print(a)
# {'name': 'justin', 'gender': 'male', 'address': 'Seoul'} 수정
```



### 기본적인 딕셔너리 사용법 (삭제) 

### 딕셔너리.pop(key) 내부에 존재하는 key에 대한 value 삭제 및 반환, 존재하지 않는 key에 대해서는 keyerror 발생

```python
a = {
		"name": "kyle"
  	"gender": "male"
  	"address": "Seoul"
}

gender = a.pop("gender")

print(a)
print(gender)
# {'name': 'kyle', 'address': 'Seoul'} male
```

### 딕셔너리.pop(key, default) 두 번째 인자로 default(기본)값을 지정하여 keyerror 방지 가능

```python
a = {
		"name": "kyle"
  	"gender": "male"
  	"address": "Seoul"
}

phone = a.pop("phone", "010-1234-5678")

print(a)
print(phone)
# {'name': 'kyle', 'gender': 'male', 'address': 'Seoul'} 010-1234-5678
```

### 기본적인 딕셔너리 사용법(조회)

### key에 해당하는 value 반환

```python
# 딕셔너리 [key]
a = {
  	"name": "kyle",
  	"gender": "male",
  	"address": "Seoul",
}

print(a["name"])
# kyle

# 딕셔너리.get(key)
a = {
  	"name": "kyle",
  	"gender": "male",
  	"address": "Seoul",
}

print(a.get("name"))
# kyle

# 딕셔너리.get(key, default)
a = {
  	"name": "kyle",
  	"gender": "male",
  	"address": "Seoul",
}

print(a.get("phone"))
# None

a = {
  	"name": "kyle",
  	"gender": "male",
  	"address": "Seoul",
}

print(a.get("phone", "없음"))
```



### 딕셔너리 기본 문법 정리

### 선언 변수 = {key1: value1, key2: value2 ...}

### 삽입/수정 딕셔너리[key]= value

### 삭제 딕셔너리.pop(key, default)

### 조회 딕셔너리[key] 딕셔너리.get(key, default)



## 131. 딕셔너리 메서드



### .keys() 딕셔너리의 key 목록이 담긴 dict_keys 객체 반환

```python
a = {
  	"name": "kyle",
  	"gender": "male",
  	"address": "Seoul",
}

print(a.keys())
# dict_keys(['name', 'gender', 'address'])

a = {
  	"name": "kyle"
  	"gender": "male"
  	"address": "Seoul"
}

for key in a.keys():
  print(key)
# name
# gender
# address

a = {
  	"name": "kyle"
  	"gender": "male"
  	"address": "Seoul"
}

for key in a:
  print(key)
```



### .values() 딕셔너리의 value 목록이 담긴 dict_values 객체 반환

```python
a = {
		"name": "kyle"
  	"gender": "male"
  	"address": "Seoul"
}

print(a.values())
# dict_values(['kyle', 'male', 'Seoul'])

a = {
  	"name": "kyle"
  	"gender": "male"
  	"address": "Seoul"
}

for value in a.values():
  print(value)
# kyle
# male
# Seoul
```



### .items() 딕셔너리의 (key, value) 쌍 목록이 담긴 dict_items 객체 반환

```python
a = {
  	"name": "kyle",
  	"gender": "male",
  	"address": "Seoul",
}

print(a.items())
# dict_items([('name', 'kyle'), ('gender', 'male'), ('address', 'Seoul')])

a = {
  	"name": "kyle",
  	"gender": "male",
  	"address": "Seoul",
}

for item in a.items():
  print(item)
# ('name', 'kyle')
# ('gender', 'male')
# ('address', 'Seoul')

a = {
  	"name": "kyle",
  	"gender": "male",
  	"address": "Seoul",
}

for key, value in a.items():
	print(key, value)
# name kyle
# gender male
# address Seoul

```

### 딕셔너리 활용 연습 - 1

### 딕셔너리 활용 연습 - 2

### 딕셔너리 활용 연습 - 3



## 132. 디버깅

### branches 모든 조건이 원하는 대로 동작하는지

### for loops 반복문에 진입하는지, 원하는 횟수만큼 실행되는지

### while loops for loops와 동일, 동료조건이 제대로 동작하는지

### function 함수 호출시, 함수 파라미터, 함수 결과

### 코드의 상태를 신중하게 출력해가며 심사숙고하는 것보다 효과적인 디버깅 도구는 없습니다.

### print 함수 활용 - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각

### 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용 Python tutor 활용 (단순 파이썬 코드인 경우) 뇌컴파일, 눈디버깅



### 코드를 작성하다가

### 에러 메시지가 발생하는 경우 해당 하는 위치를 찾아 메시지를 해결

### 로적 에러가 발생하는 경우 -명시적인 에러 메시지 없이 예상과 다른 결과가 나온 경우, 정상적으로 동자하였던 코드 이후 작성된 코드를 생각해봄, 전체 코드를 살펴봄, 휴식을 가져봄, 누군가에게 설명해봄

###  

## 133. 에러와 예외

### 문법 에러(syntax error) syntaxerror가 발생하면 파이썬 프로그램은 실행이 되지 않음 파일이름, 줄번호, ^문자를 통해 파이썬이 코드를 읽어 나갈 때(parser)문제가 발생한 위치를 표현, 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret)기호(^)를 표시



## 134. 문법 에러 - EOL(End of Line) EOF(End of File) invalid syntax assign to literal



## 135. 예외(Exception)  

### 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러

### 실행 중에 감지되는 에러들을 예외(exception)라고 부름

### 예외는 여러 타입(type)으로 나타나고, 타입이 메시지의 일부로 출력됨  nameerror, typeerror 등은 발생한 예외 타입의 종류(이름)

### 모든 내장 예외는 exception class를 상속받아 이뤄짐

### 사용자 정의 예외를 만들어 관리할 수 있음



## 136. 파이썬 내장 예외의 클래스 계층 구조 (built-in-exceptions)



## 137. 예외 처리

### try 문(statement) except 절(clause)을 이용하여 예외 처리를 할 수 있음

### try문 오류가 발생할 가능성이 있는 코드를 실행 예외가 발생되지 않으면 except 없이 실행 종료

### except 문 예외가 발생하면 except 절이 실행 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함



## 138. 처리 순서

### 예외없는 정상종료, 예외처리 할 경우, 예외처리 하지 못한 경우

### 작성 방법 

### try: try 명령문

### except 예외그룹-1 as 변수-1 : 예외처리 명령문 1

### except 예외그룹-2 as 변수-2 : 예외처리 명령문 2

### finally: finally 명령문



```python
num = input('숫자입력 :')
print(int(num))
# 숫자입력 :3
# 3

try:
  num = input('숫자입력 :')
  print(int(num))
except:
  print('숫자가 아닙니다')
  
try:
  num = input('숫자입력 :')
  print(int(num))
except ValueError:
  print('숫자가 아닙니다')
  
  
num = input('100으로 나눌 값을 입력하시오 :')
print(100/int(num))

try:
	num = input('100으로 나눌 값을 입력하시오 :')
	print(100/int(num))
except (Valueerror, zerodivisionerror):
  print('제대로 입력해줘')
  
try:
  num = input('값을 입력하시오: ')
  100/int(num)
except valueerror:
  print('숫자를 넣어주세요')
except zerodivisionerror:
  print('0으로 나눌 수 없습니다.')
except:
  print('에러는 모르지만 에러가 발생하였습니다.')
  
```



## 139. 예외처리 정리

### try 코드를 실행함

### except try 문에서 예외가 발생 시 실행함

### else try 문에서 예외가 발생하지 않으면 실행함

### finally 예외 발생 여부와 관계없이 항상 실행함



## 140. 예외처리 예시

### 파일을 열고 읽는 코드를 작성하는 경우 

### 파일 열기 시도 파일 없는 경우 => '해당 파일이 없습니다' 출력

### 파일 있는 경우 => 파일 내용을 출력

### 해당 파일 읽기 작업 종료 메시지 출력



### 파일을 열고 읽는 코드를 작성하는 경우

```python
# 파일이 없는 경우
try:
  f = open('nooofile.txt')
except Filenotfounderror:
  	print('해당 파일이 없습니다.')
else:
  	print('파일을 읽기 시작합니다.')
    print(f.read())
    print('파일을 모두 읽었습니다.')
    f.close()
 finally:
  	print('파일 읽기를 종료합니다.')
    
# 파일이 있는 경우
try:
  f = open('file.txt')
except Filenotfounderror:
  print('해당 파일이 없습니다.')
else:
  print('파일을 읽기 시작합니다.')
  print(f.read())
  print('파일을 모두 읽었습니다.')
  f.close()
finally:
  print('파일 읽기를 종료합니다.')
```



## 141. raise statement

### raise를 통해 예외를 강제로 발생

### raise <표현식>(메시지)

### <표현식> 예외 타입 지정 (주어지지 않을 경우 현재 스코프에서 활성화된 마지막 예외를 다시 일으킴)



## 142.  파이썬의 기본 데이터 구조

### 컨테이너 시퀀스 리스트, 튜플, 레인지

### 컨테이너 비시퀀스 세트 딕셔너리



## 143. 스택(stack)

### stack은 쌓는다는 의미로써, 마치 접시를 쌓고 빼듯이 데이터를 한쪽에서만 넣고 빼는 자료구조 가장 마지막에 들어온 데이터가 가장 먼저 나가므로 LIFO(Last-in, First-out, 후입선출) 방식

### 스택 자료구조의 대표 동작

### push 스택에 새로운 데이터를 삽입하는 행위

### pop 스택의 가장 마지막 데이터를 가져오는 행위

### 가장 최신의 데이터(맨 위), 가장 오래된 데이터(맨 아래)

### Stack이 필요한 이유 == stack의 use case



### 스택 자료구조 쉽게 이해하기 1~8 (push push push push push pop pop push)



## 괄호 매칭 함수 호출 백트래킹 DFS(깊이 우선 탐색)

### 파이썬은 리스트(List)로 스택을 간편하게 사용할 수 있다(append pop)

### 10773 제로 풀이 (stack.append(3), stack.pop(), stack.append(4), stack.pop())

```python
stack = []

for _ in range(int(input())):
  number = int(input())
  
  if number == 0:
    stack.pop()
  else:
    stack.append(number)
    
print(sum(stack))
```



## 144. 큐(Queue)

### Queue는 한 쪽 끝에서 데이터를 넣고, 다른 한 쪽에서만 데이터를 뺄 수 있는 자료구조 가장 먼저 들어온 데이터가 가장 먼저 나가므로 FIFO(First-in, First-out, 선입선출) 방식

### 큐의 맨 앞 데이터를 가져오는 행위 dequeue

### 큐의 맨 뒤에 데이터를 삽입하는 행위 enqueue



### 큐 자료구조도 파이썬 리스트(List)로 간편하게 사용할 수 있다

### dequeue enqueue queue

### pop(0) list append



### 2161 카드1 풀이

### queue = list(range(1, n+1))

### Queue = [1, 2, 3, 4, 5, 6, 7]



### 제일 위에 있는 카드를 바닥에 버리기 queue.pop(0)

### queue = [1, 2, 3, 4, 5, 6, 7]

### queue = [2, 3, 4, 5, 6, 7]



### 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮기기 queue.pop(0)

### queue = [2, 3, 4, 5, 6, 7]



### 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮기기 queue.append()

### queue = [3, 4, 5, 6, 7]



### 제일 위에 있는 카드를 바닥에 버리기 queue.pop(0)

### queue = [3, 4, 5, 6, 7, 2]



### queue = [4, 5, 6, 7, 2]



### 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮기기 queue.pop(0)

### queue = [4, 5, 6, 7, 2]



### 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮기기 queue.append()

### queue = [5, 6, 7, 2]

### queue = [5, 6, 7, 2, 4]



### 카드가 1개 남았을 때 종료 queue = [6]

### queue = [] 마지막 남은 카드도 출력



### 리스트를 이용한 큐 자료구조의 단점

### pop(0) 가장 오래된 데이터, append() 가장 최신의 데이터

### 데이터를 뺄 때 큐 안에 있는 데이터가 많은 경우 비효율적이다. 맨 앞 데이터가 빠지면서, 리스트의 인덱스가 하나씩 당겨 지기 때문이다



### 덱 (duque, double-ended queue) 자료구조 == 양 방향으로 삽입과 삭제가 자유로운 큐



### 덱은 양 방향 삽입, 추출이 모두 큐보다 훨씬 빠르다

### 따라서 데이터의 삽입, 추출이 많은 경우, 시간을 크게 단축 시킬 수 있다

### 삽입 append left() append()

### popleft() pop()



### 덱은 양 방향 삽입, 추출이 모두 큐보다 훨씬 빠르다

```python
# 큐를 이용한 풀이
n = int(input())
queue = list(range(1, n+1))

while len(queue) > 1:
  print(queue.pop(0), end=" ")
  queue.append(queue.pop(0))
  
print(queue[0]) 


# 덱을 이용한 풀이
from collections import deque

n = int(input())
queue = deque(range(1, n+1))

while len(queue) > 1:
  print(queue.popleft(), end=" ")
  queue.append(queue.popleft())
  
print(queue[0])

```



## 145. 힙(heap) 셋(set)

## 146. 힙(heap)

### 일반적인 큐(queue)는 순서를 기준으로 가장 먼저 들어온 데이터가 가장 먼저 나가므로 FIFO(First-in First-out, 선입선출) 방식

### (일반) 큐의 동작 과정



### 우선순위 큐(priority queue)는 우선순위(중요도, 크기 등 순서 이외의 기준)를 기준으로 가장 우선순위가 높은 데이터가 가장 먼저 나가는 방식

### 우선순위 큐의 동작 과정(가장 최신의 데이터 - - - 가장 중요한/급한 데이터)



### 우선순위 큐(priority queue) 순서가 아닌 우선순위를 기준으로 가져올 요소를 결정(dequeue)하는 큐

### 1가중치가 있는 데이터 2작업 스케줄링 3네트워크



### 큐의 맨 앞 데이터를 가져오는 행위 dequeue

### 큐의 맨 뒤에 데이터를 삽입하는 행위 enqueue



### 우선순위 큐(priority queue)를 구현하는 방법

### 1배열(array) 2연결 리스트(linked list) 3힙(heap)



### 힙(heap)의 특징 최대값 또는 최소값을 빠르게 찾아내도록 만들어진 데이터구조 완전 이진 트리의 형태로 느슨한 정렬 상태를 지속적으로 유지 한다. 힙 트리에서는 중복 값을 허용한다.

### heap이 필요한 경우 == heap의 use case

### heap은 언제 사용해야할까 1데이터가 지속적으로 정렬되야 하는 경우 2데이터에 삽입/삭제가 빈번할 때



### 파이썬의 heapq 모듈 minheap(최소 힙)으로 구현되어 있음(가장 작은 값이 먼저 옴) 삽입, 삭제, 수정, 조회 연산의 속도가 리스트보다 빠르다. (배열, 연결리스트, 힙으로 구현 가능)



### 큐와 힙의 사용법 비교

### 가장 오래된 데이터dequeue 가장 최신의 데이터enqueue -queue

### 가장 작은 데이터heapq.heappop() 가장 큰 데이터heapq.heappush() -heap(min)



### 딕셔너리 메서드

### heapq.heapify(), heaps.heappop(heap), heaps.heappush(heap, item)





## 147. 셋(set)

### 셋(set)은 수학에서의 '집합'을 나타내는 데이터 구조로 python에서는 기본적으로 제공되는 데이터 구조이다.



### .add() .remove() +(합) -(차) &(교) ^(대칭차)



### Set은 언제 사용해야할까?

### 1데이터의 중복이 없어야 할 때 (고유값들로 이루어진 데이터가 필요할 때)

### 2정수가 아닌 데이터의 삽입/삭제/탐색이 빈번히 필요할 때



### 셋(set) 연산의 시간 복잡도





## 148. 순회

### 이차원 리스트를 단순히 출력하면 아래와 같이 나온다.

```python

matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 0, 1, 2]
]

print(matrix)
>>> [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]


# 이차원 리스트에 담긴 모든 원소를 아래와 같이 출력하고 싶다면 어떻게 할까?
matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 0, 1, 2]
]

>>>1 2 3 4
>>>5 6 7 8
>>>9 0 1 2

# 인덱스를 통해 각각 출력하면 가능하다!
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 0, 1, 2]
]

print(matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3])
print(matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3])
print(matrix[1][0], matrix[2][1], matrix[2][2], matrix[2][3])

>>>1 2 3 4
>>>5 6 7 8
>>>9 0 1 2
# 따라서 이중 반복문을 통해 순회하며 이차원 리스트를 출력한다.

```

## 이중 for문을 이용한 행 우선 순회

```python
# 이중 for문을 이용한 행 우선 순회
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 0, 1, 2]
]

for i in range(3):
  for j in range(4):
    print(matrix[i][j], end=" ")
  print()

>>>1 2 3 4
>>>5 6 7 8
>>>9 0 1 2

matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 0, 1, 2]
]

for i in range(3): # 행
  for j in range(4): # 열
    print(matrix[i][j], end=" ")
  print()

>>>1 2 3 4
>>>5 6 7 8
>>>9 0 1 2


```

## 이중 for문을 이용한 열 우선 순회

```python
matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9. 0, 1, 2]
]

for i in range(4): # 열
  for j in range(3): # 행
    print(matrix[j][i], end=" ")
  print()
  
>>>1 5 9
>>>2 6 0
>>>3 7 1
>>>4 8 2




```

## 행 우선 순회 vs  열 우선 순회

```python
#
matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 0, 1, 2] 
]
for i in range(3):
    for j in range(4):
        print(matrix[i][j], end=" ")
    print()
    
>>> 1 2 3 4
>>> 5 6 7 8
>>> 9 0 1 2


matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 0, 1, 2] 
]

for i in range(4):
    for j in range(3):
        print(matrix[j][i], end=" ")
    print()
    
>>> 1 5 9
>>> 2 6 0
>>> 3 7 1
>>> 4 8 2


```



### 행 우선 순회를 이용해 이차원 리스트의 총합 구하기

```python
matrix = [
	[1, 1, 1, 1],
	[1, 1, 1, 1],
	[1, 1, 1, 1]
]

total = 0

for i in range(3):
  for j in range(4):
    total += matrix[i][j]
    
print(total)
>>> 12
```



### pythonic한 방법으로 이차원 리스트의 총합 구하기

```python
matrix = [
	[1, 1, 1, 1]
	[1, 1, 1, 1]
	[1, 1, 1, 1]
]

total = sum(map(sum, matrix))

print(total)
>>> 12

```

### 행 우선 순회를 이용해 이차원 리스트의 최대값 최소값 구하기

```python
# 최대값
matrix = [
	[0, 5, 3, 1]
  [4, 6, 10, 8]
  [9, -1, 1, 5]
]

max_value = 0

for i in range(3):
  for j in range(4):
    if matrix[i][j] > max_value:
      max_value = matrix[i][j]
      
print(max_value)
>>> 10


# 최소값
matrix = [
	[0, 5, 3, 1]
  [4, 6, 10, 8]
  [9, -1, 1, 5]
]

max_value = 99999999

for i in range(3):
  for j in range(4):
    if matrix[i][j] > min_value:
      min_value = matrix[i][j]
      
print(min_value)
>>> -1
```

### pythonic한 방법으로 이차원 리스트의 최대값 최소값 구하기

```python
 matrix = [
  [0, 5, 3, 1],
	[4, 6, 10, 8],
	[9, -1, 1, 5] 
]
max_value = max(map(max, matrix)) 
min_value = min(map(min, matrix))

print(max_value)
>>> 10
print(min_value) 
>>> -1
```

### 이차원 리스트 순회 연습 정담

```python
list_a = [list(map(int, input().split())) for i in range(2)] 
list_b = [list(map(int, input().split())) for i in range(2)] 
list_c = [[0] * 3 for _ in range(2)]

# 두 배열의 같은 위치끼리 곱하여 새로운 이차원 리스트에 저장
for i in range(2):
    for j in range(3):
        list_c[i][j] = list_a[i][j] * list_b[i][j]
# 결과 출력
for i in range(2):
	for j in range(3):
     	 print(list_c[i][j], end=" ")
  print()
```



## 149. 전치 

### 전치(transpose)란 행렬의 행과 열을 서로 맞바꾸는 것을 의미한다.

```python
matrix = [
	[1, 2, 3, 4]
	[5, 6, 7, 8]
	[9, 0, 1, 2]
]

transposed_matrix = [[0] * 3 for _ in range(4)]
# 전치 행렬을 담을 이차원 리스트 초기화 (행과 열의 크기가 반대)

for i in range(4):
	for j in range(3):
    transposed_matrix[i][j] = matrix[j][i] # 행, 열 맞바꾸기
    
"""
transposed_matrix = [
	[1, 5, 9]
	[2, 6, 0]
	[3, 7, 1]
	[4, 8, 2]
]
"""
```



## 150. 회전

### 문제에서 이차원 리스트를 왼쪽, 오른쪽으로 90도 회전하는 경우가 존재한다.

### 왼쪽으로 90도 회전하기

```python
matrix = [
    [1, 2, 3],
[4, 5, 6],
[7, 8, 9] ]
n=3
rotated_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        rotated_matrix[i][j] = matrix[j][n-i-1]
```

### 오른쪽으로 90도 회전하기

```python
matrix = [
    [1, 2, 3],
[4, 5, 6],
[7, 8, 9] ]
n=3
rotated_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        rotated_matrix[i][j] = matrix[n-j-1][i]
```



### 왼쪽으로 90도 회전하기

```python
matrix = [
    [1, 2, 3],
		[4, 5, 6],
		[7, 8, 9] 
]
n=3
rotated_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        rotated_matrix[i][j] = matrix[j][n-i-1]
        
"""
rotated_matrix = [
[3, 6, 9], [2, 5, 8], [1, 4, 7]
]
"""
```



### 오른쪽으로 90도 회전하기

```python
matrix = [
    [1, 2, 3],
		[4, 5, 6],
		[7, 8, 9] 
]
n=3
rotated_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        rotated_matrix[i][j] = matrix[n-j-1][i]
        
"""
rotated_matrix = [
[7, 4, 1], [8, 5, 2], [9, 6, 3]
]
"""

# 직접 작성해보면서 왼쪽 오른쪽 회전이 각각 어떻게 동작하는지 파악해보자

```



## 150. 완전탐색 1 (exhaustive search)

### 무식하게 다해보기 (brute-force)

### brute-force는 모든 경우의 수를 탐색하여 문제를 해결하는 방식이다. 브루트포스(brute-force)라고도 하며 무식하게 밀어붙인다는 뜻이다 가장 단순한 풀이 기법이며 단순 조건문과 반복문을 이용해서 풀 수 있다 복잡한 알고리즘 보다는 아이디어를 어떻게 코드로 구현할 것인지가 중요하다

### 블랙잭 문제를 통해 brute-force 이해하기 특별한 알고리즘 기법 없이 모든 경우의 수를 탐색해봅니다



## 151. 델다 탐색(Delta search)

### 지금까지는 모든 경우의 수를 따지는 일반적인 완전탐색을 알아보았다 이차원 리스트의 완저남색에서 많이 등장하는 유형인 델타 탐색(상하좌우 탐색)을 알아보자

### (0, 0)에서부터 이차원 리스트의 모든 원소를 순회하며 (완전탐색) 각 지점에서 상하좌우에 위치한 다른 지점을 조회하거나 이동하는 방식이다

### 이차원 리스트의 인덱스(좌표)의 조작을 통해서 상하좌우 탐색을 한다. 이때 행과 열의 변량인 -1, +1을 델타(delta)값이라 한다.



### 델타(delta)값을 이용해 상하좌우로 이동하기

### 행은 x 혹은 r로 나타내고 열은 y 혹은 c로 나타낸다

```python
# 1) 행을 x, 열을 y로 표현 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
#.   상  하  좌   우

# 2) 행을 r, 열을 c로 표현 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 상(x-1, y) nx = x + dx[0] ny = y + dy[0]
# 하(x+1, y) nx = x + dx[1] ny = y + dy[1]
# 좌(x, y-1) nx = x + dx[2] ny = y + dy[2]
# 우(x, y+1) nx = x + dx[3] ny = y + dy[3]


```

### 델타 (delta)값을 이용해 상하좌우로 이동하기

```python
# 상하좌우
for i in range(4):
	nx = x + dx[i]
	ny = y + dy[i]
	
# for 문을 이용해서 상하좌우 이동을 간단히 표현할 수 있다
```



### 상하좌우로 이동 후 범위를 벗어나지 않는지 확인 및 갱신하기

```python
# 1. 델타값을 이용해 상하좌우 이동 
for i in range(4):
	nx = x + dx[i] 
	ny = y + dy[i]
# 2. 범위를 벗어나지 않으면 갱신 
if 0 <= nx < 3 and 0 <= ny < 3:
x = nx 
y = ny
```



### 이차원 리스트의 상하좌우 탐색 정리

```python
# 1.델타값 정의(상하좌우) 
 dx = [-1, 1, 0, 0]
 dy = [0, 0, -1, 1]
# 2.이차원 리스트 순회 
for x in range(n):
	for y in range(m):
# 3.델타값을 이용해 상하좌우 이동 
for i in range(4):
nx = x + dx[i] 
ny = y + dy[i]
# 4.범위를 벗어나지 않으면 갱신 
if 0 <= nx < n and 0 <= ny < m:
x = nx 
y = ny
```



### 상하좌우 + 대각선의 8방향 델타값

```python
#	 	상, 하, 좌, 우, 좌상, 좌하, 우상, 우하
dx =[-1, 1, 0, 0, -1, 1, -1, 1]
dy =[0, 0, -1, 1, -1, -1, 1, 1]
```



## 152. 그래프 (Graph)

### 정점(vertex)과 이를 연결하는 간선(edge)들의 집합으로 이루어진 비선형 자료구조

### 소셜 네트워크와 지하철 노선도 같이, 현실에 있는 개체 간의 관계를 나타내기 위해 사용한다.



### 그래프 관련 용어

### 정점(vertex): 간선으로 연결되는 객체이며 노드(node)라고도 한다

### 간선(edge): 정점 간의 관계(연결)를 표현하는 선을 의미한다

### 경로(path): 시작 정점부터 도착 정점까지 거치는 정점을 나열한 것을 의미한다 0번 정점부터 6번 정점까지의 경로 0 - 2 - 4 - 6

### 인접(adjacency): 두 개의 정점이 하나의 간선으로 직접 연결된 상태를 의미한다 0번 정점과 2번 정점은 인접하 0번 정점과 5번 정점은 인접하지 않다



### 직접 그래프를 보면서 용어를 이해해보자.





### 그래프의 종류

### 무방향 그래프(undirected graph) 간선의 방향이 없는 가장 일반적인 그래프

### 간선을 통해 양방향의 정점 이동 가능

### 차수(degree): 하나의 정점에 연결된 간선의 개수

### 모든 정점의 차수의 합 = 간선 수 x 2



### 유방향 그래프(directed graph) 간선의 방향이 있는 그래프

### 간선의 방향이 가리키는 정점으로 이동 가능

### 차수(degree): 진입 차수와 진출 차수로 나누어짐

### 전입 차수(on-degree): 외부 정점에서 한 정점으로 들어오는 간선의 수

### 진출 차수(out-degree): 한 정점에서 외부 정점으로 나가는 간선의 수



### 그림으로만 살펴보았던 그래프를 실제 문제에서 어떻게 코드로 표현할까?

### 문제에서는 그래프를 아래와 같이 간선이 연결하는 두 정점의 목록으로 제공한다.

### 인접한 두 정점 == 서로 직접 연결된 정점

### 따라서 해당 입력을 통해 그래프를 인접 행렬 또는 인접 리스트 방식으로 표현할 수 있다.



## 인접 행렬(adjacent matrix)

### 두 정점을 연결하는 간선이 없으면 0, 있으면 1을 가지는 행렬로 표현하는 방식

```python
# 입력
0 1
0 2
1 3
1 4
2 4
2 5
4 6

# 인접 행렬 만들기
n = 7 # 정점 개수
m = 7 # 간선 개수

graph = [[0] * n for _ in range(n)]

for _ in range(m):
  v1, v2 = map(int, input().split())
  graph[v1][v2] = 1
  graph[v2][v1] = 1
  
  # 인접 행렬 결과
  graph = [
[0, 1, 1, 0, 0, 0, 0],
[1, 0, 0, 1, 1, 0, 0], 
[1, 0, 0, 0, 1, 1, 0], 
[0, 1, 0, 0, 0, 0, 0], 
[0, 1, 1, 0, 0, 0, 1], 
[0, 0, 1, 0, 0, 0, 0], 
[0, 0, 0, 0, 1, 0, 0]
]
```



## 인접 리스트(adjacent list)

### 리스트를 통해 각 정점에 대한 인접 정점들을 순차적으로 표현하는 방식

```python
# 입력
0 1 
0 2 
1 3 
1 4 
2 4 
2 5 
4 6

# 인접 리스트 만들기
n=7 #정점개수
m=7 #간선개수
graph = [[] for _ in range(n)]
for _ in range(m):
	v1, v2 = map(int, input().split()) 
  graph[v1].append(v2) 
  graph[v2].append(v1)
  
  
# 인접 리스트 결과
graph = [
[1, 2],
[0, 3, 4], 
[0, 4, 5], 
[1],
[1, 2, 6], 
[2],
[4] 
]
```



## 인접 행렬 vs 인접 리스트

### 인접 행렬은 직관적이고 만들기 편하지만, 불필요하게 공간이 낭비된다 인접 리스트는 연결된 정점만 저장하여 효율적이므로 자주 사용된다.

```python
# 인접 행렬
graph = [
[0, 1, 1, 0, 0, 0, 0],
[1, 0, 0, 1, 1, 0, 0], 
[1, 0, 0, 0, 1, 1, 0], 
[0, 1, 0, 0, 0, 0, 0], 
[0, 1, 1, 0, 0, 0, 1], 
[0, 0, 1, 0, 0, 0, 0], 
[0, 0, 0, 0, 1, 0, 0]
]

# 인접 리스트
graph = [
[1, 2],
[0, 3, 4], 
[0, 4, 5], 
[1],
[1, 2, 6], 
[2],
[4] 
]
```



## 153. 깊이우선 탐색 (DFS)



## 154. 그래프 탐색 알고리즘

### 데이터 구조는 알고리즘의 재료가 되어 문제를 해결하는데 사용된다.

### 그래프 자료구조는 탐색 알고리즘에 활용된다.

### 그래프 탐색 알고리즘이란? 시자 정점에서 간선을 타고 이동할 수 있는 모든 정점을 찾는 알고리즘

### 그래프 탐색 알고리즘에는 깊이우선탐색과 너비우선탐색이 있다 이전에 학습했던 스택과 큐 자료구조의 개념을 함께 활용한다

### 그래프 탐색 알고리즘에는 깊이우선탐색과 너비우선탐색이 있다. 이전에 학습했던 스택과 자료구조의 개념을 함께 활용한다



### 깊이우선탐색(depth-first search, DFS) 그래프의 깊이를 우선으로 탐색하기 위해 스택의 개념을 활용한다

### 너비우선탐색(breadth-first search, BFS) 그래프의 너비를 우선으로 탐색하기 위해 큐의 개념을 활용한다



### 깊이우선탐색(Depth-first search, DFS) 시작 정점으로부터 갈 수 있는 하위 정점까지 가장 깊게 탐색하고, 더 이상 갈 곳이 없다면 마지막 갈림길로 돌아와서 다른 정점을 탐색하여 결국 모든 정점을 방문하는 순회 방법

### 깊이우선탐색(DFS)을 미로 탈출로 생각하면 이해하기 쉽다. 어느 한 쪽 길로 가장 깊게 들어갔다가 막히면 다시 돌아와서 다른 길을 탐색한다. 어느 한 쪽 길로 가장 깊게 들어갔다가 막히면 다시 돌아와서 다른 길을 탐색한다.



## 깊이우선탐색(DFS)의 특징

### 모든 정점을 방문할 때 유리하다. 따라서 경우의 수, 순열과 조합 문제에서 많이 사용한다. 너비우선탐색(BFS)에 비해 코드 구현이 간단하다.

### 단, 모든 정점을 방문할 필요가 없거나 최단 거리를 구하는 경우에는 너비우선탐색(BFS)이 유리하다



## DFS의 동작 과정

### DFS를 하기 전에, 일단 탐색을 진행할 그래프가 필요하다 그래프는 인접 행렬 혹은 인접 리스트 방식으로 표현할 수 있다

### 각 정점을 방문했는지 여부를 판별할 방문 체크 리스트가 필요하다. 사람과 달리 컴퓨터는 각 정점에 방문했는지 여부를 알 수 없다. 따라서 visited 리스트를 따로 선언하여 각 정점을 방문했는지 체크한다.

```python
visited = [false] * n 
# n은 정점의 개수
```

### 인덱스는 각 정점의 번호

### 방문한 정점은 true 방문하지 않은 정점은 false



### [DFS의 사이클] 현재 정점 방문처리, 인접한 모든 정점 확인, 방문하지 않은 인접 정점 이동

### 이동할 정점이 없으므로 마지막 갈림길로 돌아감

### 모든 장점을 방문했으므로 탐색 종료, 방문 정점 순서 0-1-3-4-2-5-6



## 155. DFS의 구현 방식

### 지금까지 살펴본 DFS를 코드로 구현해보자 여기에서는 인접 리스트로 표현한 그래프를 기준으로 설명한다

### 반복문을 이용한 DFS, DFS는 직전에 방문한 정점으로 차례로 돌아가야 하므로, 후입선출(LIFO)구조의 스택을 사용한다

```python
visited = [False] * n # 방문 처리 리스트 만들기

def dfs(start):
stack = [start] # 돌아갈 곳을 기록 
visited[start] = True # 시작 정점 방문 처리
while stack: # 스택이 빌 때까지(돌아갈 곳이 없을때까지) 반복 
  cur = stack.pop() # 현재 방문 정점(후입선출)
for adj in graph[cur]: # 인접한 모든 정점에 대해 
  if not visited[adj]: # 아직 방문하지 않았다면
		visited[adj] = True # 방문 처리 
    	stack.append(adj) # 스택에 넣기
      
dfs(0) # 0번 정점에서 시작
```



### 2606 바이러스

### [단계 1] 입력 값을 받아 인접 리스트 생성

### [단계 2] 1번 컴퓨터를 시작 정점으로 DFS진행

### == 1번 컴퓨터에서 방문 가능한 컴퓨터의 수



```python
# 단계 1
n = int(input()) # 정점 개수(컴퓨터)
m = int(input()) # 간선 개수(네트워크) 
graph = [[] for _ in range(n + 1)] 
visited = [False] * (n + 1)
total = 0

# 인접 리스트 만들기 
for _ in range(m):
v1, v2 = map(int, input().split()) 
graph[v1].append(v2) 
graph[v2].append(v1)

# 단계 2 dfs(1)을 호출하며 1번 컴퓨터에서 DFS 시작
visited = [False] * n

def dfs(start):
stack = [start] 
visited[start] = True

while stack:
	cur = stack.pop()

  for adj in graph[cur]: 
    if not visited[adj]:
			visited[adj] = True
			stack.append(adj) 
dfs(1) # 1번 정점에서 시작

# 1번 컴퓨터 방문처리
visited = [False] * n

def dfs(start):
stack = [start] 
visited[start] = True

while stack:
	cur = stack.pop()

  for adj in graph[cur]: 
    if not visited[adj]:
			visited[adj] = True
			stack.append(adj) 
dfs(1) # 1번 정점에서 시작

# 1번 컴퓨터와 인접한 컴퓨터 중 아직 방문하지 않은 곳 조회
visited = [False] * n

def dfs(start):
stack = [start] 
visited[start] = True

while stack:
	cur = stack.pop()

  for adj in graph[cur]: 
    if not visited[adj]:
			visited[adj] = True
			stack.append(adj) 
dfs(1) # 1번 정점에서 시작

# 2번 컴퓨터로 이동
visited = [False] * n

def dfs(start):
stack = [start] 
visited[start] = True

while stack:
	cur = stack.pop()

  for adj in graph[cur]: 
    if not visited[adj]:
			visited[adj] = True
			stack.append(adj) 
dfs(1) # 1번 정점에서 시작

# 2번 컴퓨터 방문처리
visited = [False] * n

def dfs(start):
stack = [start] 
visited[start] = True

while stack:
	cur = stack.pop()

  for adj in graph[cur]: 
    if not visited[adj]:
			visited[adj] = True
			stack.append(adj) 
dfs(1)

# 2번 컴퓨터와 인접한 컴퓨터 중 아직 방문하지 않은 곳 조회
visited = [False] * n

def dfs(start):
stack = [start] 
visited[start] = True

while stack:
	cur = stack.pop()

  for adj in graph[cur]: 
    if not visited[adj]:
			visited[adj] = True
			stack.append(adj) 
dfs(1)

# 3번 컴퓨터로 이동
# 3번 컴퓨터 방문처리
# 3번 컴퓨터와 인접한 컴퓨터 중 아직 방문하지 않은 곳 조회
# 3번 컴퓨터에서 갈 곳이 없으므로 이전 정점으로 돌아감
# 방문하지 않은 인접 컴퓨터 조회
# 5번 컴퓨터로 이동
# 5번 컴퓨터 방문처리
# 5번 컴퓨터와 인접한 컴퓨터 중 아직 방문하지 않은 곳 조회
# 6번 컴퓨터로 이동
# 6번 컴퓨터 방문처리
# 6번 컴퓨터와 인접한 컴퓨터 중 아직 방문하지 않은 곳 조회
# 6번 컴퓨터에서 갈 곳이 없으므로 이전 정점으로 돌아감
# 5번 컴퓨터에서 갈 곳이 없으므로 이전 정점으로 돌아감
# 2번 컴퓨터에서 갈 곳이 없으므로 이전 정점으로 돌아감
# 1번 컴퓨터에서 갈 곳이 없으므로 dfs(1)이 종료되고 탐색 종료
# 최종적으로 1번 컴퓨터에 의해 감염되는 컴퓨터는 2, 3, 5, 6 (총 4대)

```



## 156. 코딩 테스트 준비 2 (기본)

### 단순 구현 (implementation)은 문제에 제시된 풀이 과정을 그대로 구현하는 유형이다

### 시뮬레이션의 경우 완전탐색 유형 중 하나로써, 모든 경우의 수를 탐색하여 풀이한다

### 아이디어나 알고리즘을 요구하기 보다는 문제에 제시된 과정을 그대로 구현할 수 있는가가 핵심이다

### 삼성 SW 역량테스트 IM A형에서 주로 출제된다.



### 단순 구현 연습 1063 킹 문제의 경우 델타값을 이용한 탐색과 아스키코드를 사용한다 



### 상하좌우 + 대각선의 8방향 델타값을 이용한다

### 방향이 알파벳으로 입력되므로 딕셔너리를 사용한다

### 아스키코드를 이용해 체스판 위치(A1, A2 ...)를 좌표로 변환한다.

```python
k, s, n = input().split()
 
kx, ky = 8 - int(k[1]), ord(k[0]) - 65 # king x, y 
sx, sy = 8 - int(s[1]), ord(s[0]) - 65 # stone x, y
```



### ord()는 특정 문자를 아스키코드로 변환하는 파이썬 내장 함수이다. 65는 아스키코드에서 "A"를 나타내므로, 이를 빼서 열의 좌표값을 구한다

### DFS를 이용해 이차원 격자를 탐색하는 문제가 자주 출제된다

### 미로는 통로는 0, 벽은 1인 이차원 격자



## 이차원 격자에서의 DFS

### DFS 방식으로 출발점부터 도착점까지의 경로를 찾아보자!

```python
# 입력
5 5 
0 0 0 0 0 
1 0 1 1 1 
0 0 1 1 1 
1 0 0 0 0 
1 1 1 1 0

# 출력 (출발점 -> 도착점 경로)
>>> [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (4, 4)]
```

### 그런데 DFS는 그래프 탐색 알고리즘 아닌가요? 이건 그래프가 아니라 격자인데...

### 격자의 각 칸에 번호를 붙여볼까요?

### 이제 각 칸이 하나의 정점이고, 번호는 정점의 번호라고 생각해봅시다!

### 이차원 격자는 결국 상하좌우로 연결된 그래프와 같다

### 결국 1번 정점에서 DFS를 시작하여 25번 정점에 도착하는 경로는 찾는 문제다

### 이를 위해 방문 체크 리스트도 이차원의 형태로 선언한다

```python
visited = [[false] * m for _ in range(n)]
```

### 인접 정점은 델타값을 이용한 상하좌우 이동으로 갈 수 있다



## 157. 상속과 연산자 중복

### 상속 어떤 클래스가 다른 클래스로부터 특성과 기능을 물려 받는 것

### 정의되어 있는 데이터 공간이나 매서드 재정의 또는 확장 가능(overriding)

### 코드 재 사용성(code reusability) 증가.

### 논리성 유사성을 일반화 함으로써 이해가 쉽다

### 상속하는 원본 클래스: base class, super class, parent class

### 상속받아 만들어진 클래스: derived class, sub class, child class

```python
class parent: 내용
class child (parent):
 	내 용
 	
# Car 클래스
class Car:
  def _init_(self name, weight, size, cylinder):
    self.name=name
    self.weight=weight
    self.size=size
    self.cylinder=cylinder
  def showspec(self):
    print('/n이 름: {}').format(self.name)
    print('무 게: {}t'.format(self.weight))
    print('길 이: {}m'.format(self.size))
    print('배기량: {}cc'.format(self.cylinder))1
    
# Truck 클래스
class Truck(car):
  pass

t1=Truck("타이탄",2.5, 4.8, 2200)
t2=Truck("볼보FMX", 5, 5.5, 3300)
t1.showspec()
t2.showspec()
```



### 메서드 확장과 치환 

### 세단 차종을 표현할 수 있도록 sedan 클래스 만들기(color 속성을 추가로 설계)

### 상위 클래스인 car에 접근하는 방법

### super()함수 이용 super()._init_(name, weight, size, cylinder)

### 상위 클래스이름사용

### Car._init_(self, name, weight, size, cylinder)

```python
class Car:
  def _init_(self name, weight, size, cylinder):
    self.name=name
    self.weight=weight
    self.size=size
    self.cylinder=cylinder
  def showspec(self):
    print('/n이 름: {}').format(self.name)
    print('무 게: {}t'.format(self.weight))
    print('길 이: {}m'.format(self.size))
    print('배기량: {}cc'.format(self.cylinder))1
class Sedan(Car):
  def _init_(self, name, weight, size, cylinder, color):
    super()._init_(name, weight, size, cylinder)
    self.color=color
  
  def showspec(self):
    super().showspec()
    print('색 상: {}'.format(self.color))
s1=sedan("쏘나타", 1.6, 1.9, 2600, "blue")
s1.showspec()

```



### 이차상속 SUV 클래스 설계(sedan 클래스처럼 색상이 중요 요소라고 가정)

```python
class SUV(Sedan):
	pass
	
sv1=SUV("렉서스", 2.0, 2.1, 2400, "gold")
sv1.showspec()
```



### Car클래스 예문정리

```python
class Car:
  def _init_(self name, weight, size, cylinder):
    self.name=name
    self.weight=weight
    self.size=size
    self.cylinder=cylinder
  def showspec(self):
    print('/n이 름: {}').format(self.name)
    print('무 게: {}t'.format(self.weight))
    print('길 이: {}m'.format(self.size))
    print('배기량: {}cc'.format(self.cylinder))1

class Truck(car):
  pass
  
class Sedan(Car):
  def _init_(self, name, weight, size, cylinder, color):
    super()._init_(name, weight, size, cylinder)
    self.color=color
  
  def showspec(self):
    super().showspec()
    print('색 상: {}'.format(self.color))

class SUV(Sedan):
	pass

t1=Truck("타이탄",2.5, 4.8, 2200)
t2=Truck("볼보FMX", 5, 5.5, 3300)
t1.showspec()
t2.showspec()

s1=sedan("쏘나타", 1.6, 1.9, 2600, "blue")
s1.showspec()
sv1=SUV("렉서스", 2.0, 2.1, 2400, "gold")
sv1.showspec()
```



### 상속(inheritance)

### 클래스 정체성 확인(_bases_,_class_, isinstance())

```
print(Car._bases_)
print(Car)
print(Truck._bases_)
print(Truck)
print(t1)
print(t1._class_)
print(isinstance(t1, Truck))
print(help(Truck))

print(t1)

_repr_
```



### 파이썬 내장클래스 상속

### list, dict 등 파이썬 내장클래스를 상속 받아 특정 메서드만 재 정의 해서 사용

```python
class MyDict(dict):
	def keys(self):
		k=super().keys()
		return sorted(k)
		
data=MyDict({'japan': 26,
			'china': 28,
			'america': 34,
			'korea': 33})
print(data.keys())

['america', 'china', 'japan', 'korea']
>>>

class MyDict(dict):
  def items(self):
    k=super().items()
    return sorted(k, key=lambda a:a[1])

data=MyDict({'japan': 26, 'china': 28, 'america':34, 'korea': 33})

print(data.items())
for k, v in data.items():
  print(k, v)
  
[('japan',26), ('china', 28), ('korea', 33), ('america', 34)]
japan 26
china 28
korea 33
america 34
>>>

```



### GUI 상속 활용 예제

```python
from tkinter import

class MyDialog:
  def _init_(self, parent):
    label(parent, text="값입력").pack()
    self.e = Entry(parent)
    self.e.pack(padx=5)
    self.b = Button(parent, text="확인", command=self.ok_click)
    self.b.pack(pady=5)
  def ok_click(self):
    print("value is", self.e.get())
    
class BranchDialog(MyDialog):
  def _init_(self,parent):
    super()._init_(parent)
    self.b2 = button(parent, text="취소",command=self.cancel_click)
    self.b2.pack(pady=5)
  
  def cancel_click(self):
    print("취소를 눌렀습니다.")
    
root = Tk()
a=MyDialog(root)
b=BranchDialog(Tk())
root.mainloop()
```



## 158. Magic method 연산자 중복(operator overloading)

### 연산자 중복이란?

### 언어에서 미리 정의되어 있는 일부 연산자나 메서드들에 대해 개발자 의도를 담아 처리할 수 있도록 클래스에서 재정의를 허용하는 것

### Special method, magic method, dunder method

### class 작성을 통해 재정의 한다

### 이름 앞뒤에 더블언드스코어(__)가 붙어있다

### 대표적인 예로 __Init__ __str__ __add__ __it__ 등

```
>>> a=255
>>> type(a)
<class 'int'>

>>> a2=a.__dir__()
>>> a2.sort()
>>> a2
```



### magic method 구분

### 연산의 관리

```
- 산술연산자, 확장산술연산자, 비교연산자 등에 대한 정의 가능
(+,-, <, <= 등사용시호출된다)
__add__(self, oth), __sub__(self, oth), __mul__(self, oth), __eq__(self, oth),
__lt__(self, oth) 등
```



### 객체의 생성, 초기화, 소멸

```
- 객체의 생성 또는 소멸 시 호출, __new__(cls[,..]) __init__(self[,...]) __del__(self)
```



### 객체의 표현

```
- print(), str(), repr() 함수 사용시 호출(가령 __str__은 인스턴스가 문자열로 어떻게 표현될지 정의 __repr__ (self) __str__ (self 등
```



### 속성의 관리

```
- __getattr__ (self, name) : 객체에 존재하지 않는 속성에 참조 시도가 있을 때 호출됨.
- __setattr__ (self) : 객체의 속성 변경 발생시 호출 (재귀호출 주의)
- __getattribute__ (self, name) : 객체의 속성 참조 시 무조건 호출. 이 메서드를 재정의 하면 __getattr__은 불통
- __delattr__ (self, name) : 객체의 속성을 del 키워드로 삭제 시 - __dir__ (self) : 객체의 속성을 꺼내보는 dir() 함수 사용 시
- __slots__ (변수명) : 사용할 변수를 미리 등록
```



### 디스크립터(Descriptor) 관리

```
- __get__(self, instance, owner) : 디스크립터의 값이 회수될 때 호출됨 instance는 소유자 객체 인스턴스, owner는 소유자 클래스 자체
- _set__(self, instance, value) : 디스크립터의 값이 변경될 때 호출된다. • instance는 소유자 인스턴스, value는 디스크립터에 설정하는 값
- __delete__(self, instance) : 디스크립터의 값이 삭제될 때 호출
```



### 컨테이너 관리

```
- 컨텐이너 : 집단형 자료(즉 list와 tuple같은 시퀀스, dictionary같은 맵핑형 등) 의 보관소
• __len__(self) : 객체의 길이를 반환. len()함수 사용시 호출
• __getitem__(self, key) : 객체에서 [ ] 연산자를 사용하여 조회 시 호출(list[0]은
list.__getitem__(0)
• __missing__(self, key) : 키가 dictionary에 없을 시 호출
• __setitem__(self, key, value): 객체에서 [ ] 연산자를 사용하여 변수에 값을 넣을 때 호출
( list[0] = 'korea' 는 list.__setitme__(0, 'korea')로 동작 • __delitem__(self, key): del object[]를 사용시 호출
• __iter__(self): 컨테이너의 iterator를 반환
• __reversed__(self): reversed() 함수 사용시 호출
• __contains__(self, item): in 연산자 사용하여 특정아이템의 존재여부를 확인 시 호출 이 메서드를 정의 하지 않았을 시는 __iter__를 통해 이터레이션을 돌며 확
```



### Magic method 구현 예

### 문자와 숫자의 덧셈연산 시도

### 해결방법: + 연산기호를 재 정의 -> __add__에서 정의

### 리스트 + 연산에 활용한 예

### magic method 구현 예

```
- __getatter__ , __setatter
 - __getattr__ (self, name) : 객체에 존재하지 않는 속성에 참조 시도가 있을 때 호출됨.
 - __setattr__ (self) : 객체의 속성 변경 발생시 호출 (재귀호출 주의)
```



### descriptor 객체

### 어떤객체의속성변화를백그라운드에서추적및관리하기위한객체 소유자(owner) 디스크립터

### 디스크립터 클래스에 소유자 관리대상 속성을 정의하고 __get__, __set__, __del__ 등 메서드 정의

### 소유자 클래스 정의 시 중요 속성을 속성으로 정의하고, 디스크립터의 인스턴스 할당

### 사용자쪽에서 소유자의 중요속성에 접근하면 __set__, __get__ 처리 됨



### descriptor(set, get)

### descriptor 대신 decorator 활용도 가능

### __getitem__ __setitem__

### 컨테이너 자료에 a[3] = 20 과 같이 넣거나 print[3]과 같이 뺄 때 호출

