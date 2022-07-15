

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

### 불린형(boolean type) - True / False 값을 가진 타입 bool, 비교/논리 연ㅅ나을 수행함에 있어서 활용됨, 0 0.0 () [] '' none false로 변환됨

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





