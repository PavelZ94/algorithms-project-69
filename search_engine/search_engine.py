import re

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
    word_counts = {}

    for doc in array:
        raw_doc = doc['text'].split(' ')
        new_doc = word_processing(raw_doc)
        count = new_doc.count(found)
        if count > 0:
            word_counts[doc['id']] = count

    sorted_docs = sort_by_word_count(word_counts)

    return sorted_docs


def word_processing(raw_doc):
    new_doc = []
    for token in raw_doc:
        token = re.findall(r'\w+', token)
        result = ''.join(token).lower()
        new_doc.append(result)
    return new_doc


def sort_by_word_count(word_counts):
    sorted_docs = [k for k, v in sorted(word_counts.items(), key=lambda item: item[1], reverse=True)]
    return sorted_docs


print(search(docs, 'shoot'))
print(search([], 'shoot'))
print(search(docs, 'pint'))
