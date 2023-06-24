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

