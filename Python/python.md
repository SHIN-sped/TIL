

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



