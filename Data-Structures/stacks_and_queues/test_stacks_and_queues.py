from stacks_and_queues import Node, Stack, Queue

# Can successfully empty a stack after multiple pops
# Can successfully peek the next item on the stack
# Can successfully enqueue into a queue
# Can successfully enqueue multiple values into a queue
# Can successfully dequeue out of a queue the expected value
# Can successfully peek into a queue, seeing the expected value
# Can successfully empty a queue after multiple dequeues
# Can successfully instantiate an empty queue

def create_stack(nodes):
    '''Helper function to create a stack'''

    stack = Stack()
    for node in nodes:
        stack.push(node)

    return stack

def test_create_node():
    '''Can successfully create node'''
    node = Node('aaron')
    assert node.data == 'aaron'

def test_create_empty_stack():
    '''Can successfully instantiate an empty stack'''
    stack = Stack()
    assert stack.top == None

def test_stack_push():
    '''Can successfully push onto a stack'''
    stack = Stack()
    stack.push('value')
    assert stack.top.data == 'value'

def test_stack_push_multiple():
    '''Can successfully push multiple values onto a stack'''
    stack = Stack()
    assert stack.top == None
    stack.push(5)
    assert stack.top.data == 5
    stack.push(1)
    assert stack.top.data == 1
    stack.push(2)
    assert stack.top.data == 2

def test_stack_pop_multiple():
    '''Can successfully pop off the stack'''
    stack = create_stack([1,2,3,4,5])
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.top.next_node == None

def test_instantiate_queue():
    '''Can successfully instantiate an empty queue'''
    queue = Queue()
    assert queue

def test_enqueue_to_queue():
    '''Can successfully enqueue into a queue'''
    queue = Queue()
    queue.enqueue(1)
    actual = queue.front.data
    expected = 1
    assert actual == expected

def test_queue_peek():
    '''Can successfull peek into a queue'''
    queue = Queue()
    queue.enqueue(1)
    assert queue.peek() == 1
