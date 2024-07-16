doc1 = "I can't shoot straight unless I've had a pint!"
doc2 = "Don't shoot shoot shoot that thing at me."
doc3 = "I'm your shooter."

docs = [
    {'id': 'doc1', 'text': doc1},
    {'id': 'doc2', 'text': doc2},
    {'id': 'doc3', 'text': doc3},
]


def search(array, found):
    res = []
    for doc in array:
        new_doc = doc['text'].split(' ')
        if found in new_doc:
            res.append(doc['id'])
    return res


print(search(docs, 'shoot'))
print(search([], 'shoot'))
