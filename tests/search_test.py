from lwdsa.algo.search import binary_search


def test_binary_search():

    assert binary_search([], 5) == False
    assert binary_search([1, 2, 3, 4, 5], 5) == True
    assert binary_search([1, 2, 3, 4, 6], 5) == False
    assert binary_search([1, 200, 5000, 6000], 5000) == True
