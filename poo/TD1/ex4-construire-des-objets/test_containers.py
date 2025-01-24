from custom_array import Array
from stack import Stack
from queue import Queue
from exceptions import ArrayError, StackError, QueueError


def test_array():
    print("\n=== Testing Array ===")
    arr = Array(3, "test")
    print("Initial array:")
    for i in range(len(arr)):
        print(f"- {arr[i]}")

    arr[1] = "modified"
    print("\nAfter modification:")
    for i in range(len(arr)):
        print(f"- {arr[i]}")

    try:
        arr[3] = "error"
    except ArrayError as e:
        print(f"\nCaught expected error: {e}")


def test_stack():
    print("\n=== Testing Stack ===")
    stack = Stack(5)

    print("Testing push:")
    for i in range(3):
        stack.push(f"item{i}")
    stack.afficher()

    print("\nTesting pop:")
    print(f"Popped: {stack.pop()}")
    stack.afficher()

    print("\nTesting reverse:")
    stack.reverse()
    stack.afficher()


def test_queue():
    print("\n=== Testing Queue ===")
    queue = Queue(5)

    print("Testing enqueue:")
    for i in range(3):
        queue.enqueue(f"item{i}")
    queue.afficher()

    print("\nTesting dequeue:")
    print(f"Dequeued: {queue.dequeue()}")
    queue.afficher()


if __name__ == "__main__":
    test_array()
    test_stack()
    test_queue()