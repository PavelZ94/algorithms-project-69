import re
import json
doc1 = "I can't shoot straight unless I've had a pint!"
doc2 = "Don't shoot shoot shoot that thing at me."
doc3 = "I'm your shooter."
doc4 = "I can't shoot straight unless I've had a pint!"


docs = [
    {'id': 'doc1', 'text': doc1},
    {'id': 'doc2', 'text': doc2},
    {'id': 'doc3', 'text': doc3},
    {'id': 'doc4', 'text': doc4},
]


def search(array, found):
    res = []
    for doc in array:
        raw_doc = doc['text'].split(' ')
        new_doc = word_processing(raw_doc)
        if found in new_doc:
            res.append(doc['id'])
    return res


def word_processing(raw_doc):
    new_doc = []
    for token in raw_doc:
        token = re.findall(r'\w+', token)
        result = ''.join(token).lower()
        new_doc.append(result)
    return new_doc


print(search(docs, 'shoot'))
print(search([], 'shoot'))
print(search(docs, 'pint'))