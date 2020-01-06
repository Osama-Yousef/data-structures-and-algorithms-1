import pytest
from stacks_and_queues import Queue
from fifo_animal_shelter import AnimalShelter


def test_enqueue_dog_to_dog_queue():
    shelter = AnimalShelter()
    shelter.fifo_enqueue({'type': 'dog', 'name': 'Rex'})
    expected = {'type': 'dog', 'name': 'Rex'}
    assert expected == shelter.dogs.peek()

def test_enqueue_cat_to_cat_queue():
    shelter = AnimalShelter()
    shelter.fifo_enqueue({'type': 'cat', 'name': 'Diamond'})
    expected = {'type': 'cat', 'name': 'Diamond'}
    assert expected == shelter.cats.peek()

def test_dequeue_dog_to_dog_queue():
    shelter = AnimalShelter()
    shelter.fifo_enqueue({'type': 'dog', 'name': 'Rex'})
    expected = {'type': 'dog', 'name': 'Rex'}
    assert expected == shelter.fifo_dequeue('dog')

def test_dequeue_cat_to_cat_queue():
    shelter = AnimalShelter()
    shelter.fifo_enqueue({'type': 'cat', 'name': 'Diamond'})
    expected = {'type': 'cat', 'name': 'Diamond'}
    assert expected == shelter.fifo_dequeue('cat')