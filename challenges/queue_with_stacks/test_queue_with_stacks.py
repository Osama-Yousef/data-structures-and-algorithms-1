from queue_with_stacks import psueodoQueue
import pytest

q = psueodoQueue()

def test_enqueue():
    q.enqueue('apple')
    q.enqueue('banana')
    actual = q.stack.peek()
    assert actual == 'banana'

def test_dequeue():
    q.enqueue('apple')
    q.enqueue('banana')
    actual = q.dequeue()
    assert actual == 'apple'