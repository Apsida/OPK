from BST_tree import *
from random import randint

def test_cmp(a,b):
    if a > b:
        return -1
    elif a == b:
        return 0
    else: return 1

def TEST_SIZE_CORRECT():
    r = Tree(test_cmp)
    r.insert(1)
    r.insert(2)
    r.insert(3)
    r.insert(2)
    r.insert(1)
    return size(r.root) == 5

def TEST_DEL_EXIST():
    r = Tree(test_cmp)
    for i in range(11, 100, 10):
        r.insert(i)
    r.del_knot(21)
    return not(r.search(21))

def TEST_DEL_NOT_EXIST():
    r = Tree(test_cmp)
    was_exept = False
    for i in range(11, 100, 10):
        r.insert(i)
    try:
        r.del_knot(22)
    except Exception:
        was_exept = True
    return was_exept

def TEST_SEARCH_EXIST_KNOT():
    r = Tree(test_cmp)
    for i in range(0,10,2):
        r.insert(i)
    return r.search(8)

def TEST_SEARCH_NOT_EXIST_KNOT():
    r = Tree(test_cmp)
    for i in range(0, 10, 2):
        r.insert(i)
    return not(r.search(7))

def _check(root, cmp_func):
    is_corr = []
    if root is None:
        return True
    if (not(root.left is None) and not(root.right is None) and
        cmp_func(root.left.data,root.data) >= 0 and cmp_func(root.left.data,root.data) <= 0):
        return True
    is_corr.append(_check(root.right, cmp_func))
    is_corr.append(_check(root.left, cmp_func))
    return is_corr

def TEST_BST_TREE_CHECK():
    r = Tree(test_cmp)
    for i in range(10, 0, -2):
        r.insert(randint(-10,10))
    err = _check(r.root, test_cmp)
    return not(False in err)

def cmp_str(a,b):
    if len(a) > len(b):
        return -1
    elif len(a) == len(b):
        return 0
    return 1

def TEST_TREE_OF_STRING():
    r = creat(cmp_str)
    r.insert("Финик")
    r.insert("Драник")
    r.insert("Сырник")
    r.insert("Панкеке")
    err = _check(r.root, cmp_str)
    return False not in err


def run_all_tests():
    red_color_add = '\033[91m'
    green_color_add = '\033[92m'
    end_color_add = '\033[0m'
    success_str = green_color_add + "passed" + end_color_add
    fail_str = red_color_add + "failed" + end_color_add

    passed_tests_count = 0
    all_tests_count = 0

    test_funcs = [TEST_SIZE_CORRECT, TEST_DEL_EXIST, TEST_DEL_NOT_EXIST, TEST_SEARCH_EXIST_KNOT, TEST_SEARCH_NOT_EXIST_KNOT,
                  TEST_BST_TREE_CHECK, TEST_TREE_OF_STRING]
    for test_func in test_funcs:
        test_success = test_func()
        print(test_func.__name__ + " : " + (success_str if test_success else fail_str))
        all_tests_count += 1
        passed_tests_count += (1 if test_success else 0)

    print("--------------------")
    print("Passed tests count: ", passed_tests_count)
    print("Failed tests count: ", all_tests_count - passed_tests_count)

if __name__ == "__main__":
    run_all_tests()