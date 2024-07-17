import pytest
from search_engine.search_engine import search


@pytest.mark.parametrize('file, res', [
    ('tests/fixtures/docs.json', "['doc1', 'doc2', 'doc4']")
])
def test(file, res):
    with open(file, 'r') as file1:
        check = search(file1, 'shoot')
        assert check == res
