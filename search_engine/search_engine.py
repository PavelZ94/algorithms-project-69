import re

doc1 = "I can't shoot straight unless I've had a pint!"
doc2 = "Don't shoot shoot shoot that thing at me."
doc3 = "I'm your shooter."

docs = [
    {'id': 'doc1', 'text': doc1},
    {'id': 'doc2', 'text': doc2},
    {'id': 'doc3', 'text': doc3},
]


def search(array, found):
    word_counts = {}

    found_words = word_processing(found.split(' '))
    index_list = []

    for doc in array:
        new_doc = word_processing(doc['text'].split(' '))
        for elem in new_doc:
            index_list.append(elem)
        unique_word_count = 0
        total_occurrences = 0


        for word in found_words:
            count = new_doc.count(word)
            if count > 0:
                unique_word_count += 1
                total_occurrences += count

        if unique_word_count > 0:
            word_counts[doc['id']] = (unique_word_count, total_occurrences)

    sorted_docs = sort_by_relevance(word_counts)
    index = make_index(array, index_list)
    print(index)

    return sorted_docs


def word_processing(raw_doc):
    new_doc = []
    for token in raw_doc:
        token = re.findall(r'\w+', token)
        result = ''.join(token).lower()
        new_doc.append(result)
    return new_doc


def sort_by_relevance(word_counts):
    sorted_docs = sorted(word_counts.items(), key=lambda item: (item[1][0], item[1][1]), reverse=True)
    return [k for k, v in sorted_docs]


def make_index(array, index_list):
    res_set = set(index_list)
    index = {word: [] for word in res_set}
    for doc in array:
        doc_id = doc['id']
        text = word_processing(doc['text'].split(' '))
        for word in res_set:
            if word in text:
                index[word].append(doc_id)

    return index


print(search(docs, 'shoot'))  # ['doc2', 'doc1']
print(search([], 'shoot'))  # []
print(search(docs, 'pint'))  # ['doc1']
print(search(docs, 'shoot at me'))  # ['doc2']

