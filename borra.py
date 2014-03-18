animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''

    #Setting variables
    Count = 0

    #Setting function body
    for key in aDict.values():
    	for palabra in key:
    		Count += 1

    return Count

print biggest(animals)