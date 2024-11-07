import pytest
from io import StringIO
import sys

class Node:
    pass

class CircularIterator:
    def __init__(self, h: Node):
        self.header = h
        self.prev = h
        self.cur = h.next

    def atEnd(self) -> bool:
        return self.cur is self.header

    def getData(self) -> int:
        if self.atEnd():
            return -1
        return self.cur.data

    def next(self):
        self.prev = self.cur
        self.cur = self.cur.next

    def insertAfter(self, x: int):
        newnode = Node()
        newnode.data = x
        newnode.next = self.cur.next
        self.cur.next = newnode


class Pioneer(CircularIterator):
    def atlasttown(self) -> bool:
        return self.cur.next is self.header
    
    def move(self):
        if not self.atlasttown():
            self.prev = self.cur
            self.cur = self.cur.next

    def build(self, x: int):
        newnode = Node()
        newnode.owner = x
        newnode.next = self.cur.next
        self.cur.next = newnode


class CircularLinkedList:
    def __init__(self):
        newnode = Node()
        newnode.next = newnode
        self.header = newnode

    def isEmpty(self) -> bool:
        return self.header.next is self.header

    def getIterator(self) -> Pioneer:
        return Pioneer(self.header)

def main():
    Towns = CircularLinkedList()

    k, n = input().split()
    k = int(k)
    n = int(n)

    pioneers = []

    list_for_n = []

    for i in range(k):
        pioneer = Towns.getIterator()
        pioneers.append(pioneer)

    for i in range(n):
        p , w = input().split()
        p = int(p)
        pioneer = pioneers[p]
        if w == "build" :
            pioneer.build(p)
        else :
            pioneer.move()
        


    iterator = Towns.getIterator()
    count = 0
    while not iterator.atEnd():
        count += 1
        iterator.next()

    print(count)


    iterator = Towns.getIterator()
    while not iterator.atEnd():
        print(iterator.cur.owner)
        iterator.next()


def run_test(input_data, expected_output):
    # 표준 입력을 대체 (input_data 사용)
    sys.stdin = StringIO(input_data)

    # 표준 출력을 캡처
    captured_output = StringIO()
    sys.stdout = captured_output

    # 메인 함수 호출 (여기서는 `main` 함수가 실행될 거라고 가정합니다)
    main()

    # 캡처한 출력을 기대 출력과 비교
    output = captured_output.getvalue().strip()

    # 출력이 기대한 값과 일치하는지 확인
    assert output == expected_output.strip()


@pytest.mark.timeout(2)  # 각 테스트는 2초 이내에 완료되어야 함
def test_basic_case():
    input_data = "2 2\n0 build\n1 build"
    expected_output = "2\n1\n0"
    run_test(input_data, expected_output)

@pytest.mark.timeout(2)
def test_max_build_case():
    input_data = "30000 30000\n" + "\n".join(f"{i} build" for i in range(30000))
    expected_output = "30000\n" + "\n".join(str(i) for i in reversed(range(30000)))
    run_test(input_data, expected_output)

@pytest.mark.timeout(2)
def test_max_move_case():
    input_data = "30000 30000\n" + "\n".join(f"{i} move" for i in range(30000))
    expected_output = "0"
    run_test(input_data, expected_output)

@pytest.mark.timeout(2)
def test_min_case():
    input_data = "1 1\n0 build"
    expected_output = "1\n0"
    run_test(input_data, expected_output)

@pytest.mark.timeout(2)
def test_mixed_case():
    # 수정된 테스트 케이스: build와 move가 교대로 일어남
    # build는 p=0,2,4,...,29998 이 수행
    input_data = "30000 30000\n" + "\n".join(f"{i} {'build' if i % 2 == 0 else 'move'}" for i in range(30000))
    # build는 15000번 수행, p는 0,2,4,...,29998
    expected_builders = [str(i) for i in reversed(range(0, 30000, 2))]
    expected_output = f"15000\n" + "\n".join(expected_builders)
    run_test(input_data, expected_output)

@pytest.mark.timeout(2)
def test_single_pioneer_builds_all():
    input_data = "1 30000\n" + "\n".join("0 build" for _ in range(30000))
    expected_output = "30000\n" + "\n".join("0" for _ in range(30000))
    run_test(input_data, expected_output)

@pytest.mark.timeout(2)
def test_multiple_pioneers_with_moves():
    # 추가된 엣지 케이스: 여러 개척자가 build와 move를 번갈아가며 수행
    input_data = "3 6\n0 build\n1 build\n2 build\n0 move\n1 move\n2 move"
    expected_output = "3\n2\n1\n0"
    run_test(input_data, expected_output)

@pytest.mark.timeout(2)
def test_no_actions():
    input_data = "1 0\n"
    expected_output = "0"
    run_test(input_data, expected_output)

@pytest.mark.timeout(2)
def test_all_moves_no_builds():
    input_data = "5 5\n0 move\n1 move\n2 move\n3 move\n4 move"
    expected_output = "0"
    run_test(input_data, expected_output)

@pytest.mark.timeout(2)
def test_all_builds_single_pioneer():
    input_data = "1 5\n0 build\n0 build\n0 build\n0 build\n0 build"
    expected_output = "5\n0\n0\n0\n0\n0"
    run_test(input_data, expected_output)