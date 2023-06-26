# 타입 힌트
- python 3.5부터 타입 선언 가능

```python
a: str = "1"
b: int = 1
```
```python
def fn(a: int) -> bool
# fn() 함수의 파라미터 a는 int, 리턴값은 boolean
```

- mypy를 이용해 타입 힌트가 잘못되었는지 체크 가능
```
$ mypy python.py
```

# 람다식과 리스트 컴프리헨션
- 1부터 5까지의 제곱 구하기
```python
# 람다식
list(map(lambda x: x ** 2, range(1, 6)))

# 결과 [1, 4, 9, 16, 25]
```
```python
# 리스트 컴프리헨션
[n ** 2 for n in range(1, 6)]

# 결과 [1, 4, 9, 16, 25]
```
```python
# 리스트 컴프리헨션(딕셔너리)
{n: n ** 2 for n in range(1, 6)}

# 결과 {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

# 제너레이터
- 반복 가능한 객체를 생성하는 것
- 리스트 컴프리헨션과 비슷하지만, 모든 값을 메모리에 미리 로드하지 않고 `.next()` 함수를 호출할 때 순차적으로 값을 생성함

```python
# 예시
generator = (i ** 2 for i in range(10))

next(generator)  # 결과: 0
next(generator)  # 결과: 1
next(generator)  # 결과: 4
# 9 ** 2까지 반복 후
next(generator)  # StopIteration 예외 발생
```

```python
# for 활용
generator = (i ** 2 for i in range(10))

for num in generator:
    print(num)
# 제너레이터에 저장된 모든 값을 출력한 뒤 for문을 빠져나감
```

```python
# 함수를 이용한 제너레이터 생성

# 1부터 max까지의 숫자를 생성하는 제너레이터 함수
def count_up_to(max):
    count = 1
    while count <= max:
        yield count # 값 생성
        count += 1

for number in count_up_to(5):
    print(number)
    # 1부터 5까지 출력한 뒤 for문을 빠져나감
```

```python
# yield의 특징
def simple_generator():
    yield 1
    print("After 1st yield")
    yield 2
    print("After 2nd yield")
    yield 3

gen = simple_generator()

print(next(gen))  # 결과: 1
print(next(gen))  # 결과: "After 1st yield", then 2
print(next(gen))  # 결과: "After 2nd yield", then 3

# yield는 이전 yield로 반환한 지점을 기억하기 때문에, 다음 호출 시 이전에 중단됐던 부분부터 다시 시작됨
```

# enumarate
- 반복 가능한 객체(list, set, tuple, 문자열 등의 자료형)을 입력받아 인덱스와 함께 튜플로 반환하는 객체

```python
# 리스트 예시
fruits = ['apple', 'banana', 'mango', 'grape', 'orange']

print(enumerate(fruits))
# 결과: <enumerate object at 0x000002AA24710D80>

print(list(enumerate(fruits)))
# 결과: [(0, 'apple'), (1, 'banana'), (2, 'mango'), (3, 'grape'), (4, 'orange')]
```

```python
# 튜플 예시
fruits = ('apple', 'banana', 'mango', 'grape', 'orange')

print(enumerate(fruits))
# 결과: <enumerate object at 0x000001205A536DC0>
print(tuple(enumerate(fruits)))
# 결과: ((0, 'apple'), (1, 'banana'), (2, 'mango'), (3, 'grape'), (4, 'orange'))
```

```python
# 셋 예시
fruits = ('apple', 'banana', 'mango', 'grape', 'orange')

print(enumerate(fruits))
# 결과: <enumerate object at 0x000001F0367E6DC0>
print(set(enumerate(fruits)))
# 결과: {(1, 'mango'), (3, 'orange'), (4, 'banana'), (0, 'apple'), (2, 'grape')}
```

```python
# 문자열 예시
string = "hello"

print(enumerate(string))
# 결과: <enumerate object at 0x0000022ECA16AA80>
print(list(enumerate(string)))
# 결과: [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]
```

# print
- print() 함수의 문자열 포맷팅 방법
```python
idx = 0
fruit = 'mango'

# 위치 지정자를 사용한 포맷팅
print('{0}: {1}'.format(idx + 1, fruit))

# 암시적 위치 지정자를 사용한 포맷팅
print('{}: {}'.format(idx + 1, fruit))

# f-string 포맷팅(python 3.6 이상부터 사용 가능)
print(f'{idx + 1}: {fruit}')
```

# pass
- 아무것도 하지 않는 제어문
- 문법적으로 문장이 필요하지만 아직 구현하지 않았을 때 사용

```python
# 함수 예시
def my_function():
    pass  # TODO: implement this function later
```

```python
# if문 예시
for i in range(10):
    if i < 5:
        print(f"{i} is less than 5")
    else:
        pass  # do nothing for numbers >= 5
```

# locals
- 현재 스코프 내 모든 지역변수를 포함하는 딕셔너리 반환
- 딕셔너리의 키는 변수 이름, 밸류는 변수에 할당된 값으로 나타남
- 해당 딕셔너리는 읽기 전용으로 이를 통해 변수 값을 변경할 수는 없음

```python
def first_function():
    x = 30
    y = 40
    print(locals())

def second_function():
    x = 10
    y = 20
    print(locals())

first_function()
second_function()

# 결과
# {'x': 30, 'y': 40}
# {'x': 10, 'y': 20}
```

# 구글 파이썬 스타일 가이드
- 좋은 파이썬 코드를 작성하기 위한 가이드

```python
# no
def foo(a, b=[]): ...
def foo(a, b: Mapping = {}): ...
# 파이썬에서는 함수 기본 인자가 한 번만 평가되고 동일 객체가 함수 호출 간에 공유됨
# 여러 번 함수를 호출할 경우, 매번 빈 리스트나 딕셔너리가 생성되는 것이 아니라 기존에 호출해 사용했던 리스트와 딕셔너리를 사용함

# yes
def foo(a, b=None):
    if b is None:
        b = []
def foo(a, b: Optional[Sequence] = None):
    if b is None:
        b = []
# 때문에 디폴트값을 None으로 설정한 후, 새로운 자료형을 생성해주어야 함
```

```python
# no
if len(users) == 0:
    print('no users')

# yes
if not users:
    print('no users')

# 보다 간결하고 파이써닉한 방식으로, 리스트 뿐만 아니라 다른 반복 가능 객체에서도 동작함
```
```python
# no
if foo is not None and not foo:
    self.handle_zero()

# yes
if foo == 0:
    self.handle_zero()

# 보다 간결하고 직관적이기 때문에 이해가 쉬움
```
```python
# no
if not 1 % 10:
    self.handle_mutiple_of_ten()

# yes
if 1 % 10 == 0:
    self.handle_mutiple_of_ten()

# not은 보통 boolean에 사용되므로 숫자에 사용하면 혼동이 생길 수 있음
```

# is와 ==
- `is`는 id() 값을 비교하며, `==`는 값을 비교함

```python
# no
if a == None:

# yes
if a is None:

# None은 값이 없는 null이므로 ==로 비교 불가능
```
```python
a = [1, 2, 3]

a == a # True

a == list(a) # True

a is a # True

a is list(a) # False

# list()로 묶을 경우 같은 값을 가지는 별도의 객체가 새로 생성되므로 ID 값이 달라짐
```
```python
a = [1, 2, 3]

a == copy.deepcopy(a) # True

a is copy.deepcopy(a) # False

# copy.deepcopy() 역시 같은 값을 가지는 별도의 객체가 새로 생성되므로 ID 값을 비교하는 is에서는 False
```