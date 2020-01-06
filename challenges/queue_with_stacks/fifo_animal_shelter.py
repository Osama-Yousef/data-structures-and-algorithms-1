from stacks_and_queues import Queue

class AnimalShelter:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()

    def fifo_dequeue(self, preference):
        '''Method, where a cat or dog is selected, removed their respective queues, and returned'''

        if preference == 'cat':
            return self.cats.dequeue()

        if preference == 'dog':
            return self.dogs.dequeue()
            
        else:
            return None

    def fifo_enqueue(self, animal):
        '''Method, takes in animal as an argument, if cat or dog assigns to that animal's queue'''

        if animal.get('type') == 'cat': 
            self.cats.enqueue(animal)

        if animal.get('type') == 'dog':
            self.dogs.enqueue(animal)