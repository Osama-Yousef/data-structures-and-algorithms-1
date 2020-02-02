import pytest
from repeated_word import repeated_word


string_a = "Once upon a time, there was a brave princess who.."
string_b = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
string_c = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."

def test_empty_repeated_word():
    '''Empty string will result in returning None'''
    assert repeated_word('') == None

def test_single_word():
    '''Single word should return None'''
    assert repeated_word('Blah') == None

def test_no_repeated_words():
    '''No repeated words returns None'''
    assert repeated_word('hello world how are you?') == None

def test_repeated_word_found():
    '''Repeated word in string returns correctly'''
    assert repeated_word('hello are world how are you?') == 'are'

def test_repeated_word_found_with_non_ascii():
    '''Repeated word in string returns correctly'''
    assert repeated_word('hello how are you are?') == 'are'