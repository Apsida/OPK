from BST_tree import *

def TEST_DEL_EXIST():
    r = Node(51)
    for i in range(11, 100, 10):
        if i != 51:
            r = insert(r, i)
    r = del_knot(r, 21)
    return not(search(r, 21))

def TEST_DEL_NOT_EXIST():
    r = Node(51)
    was_exept = False
    for i in range(11, 100, 10):
        if i != 51:
            r = insert(r, i)
    try:
        del_knot(r, 22)
    except Exception:
        was_exept = True
    return was_exept

def TEST_SEARCH_EXIST_NODE():
    r = Node(5)
    for i in range(0,10,2):
        r = insert(r, i)
    return search(r,8)

def TEST_SEARCH_NOT_EXIST_NODE():
    r = Node(5)
    for i in range(0, 10, 2):
        r = insert(r, i)
    return not(search(r, 7))

def _check(root):
    if root is None:
        return True
    if (not(root.left) is None and not(root.right is None)
        and root.left.val <= root.val <= root.right.val):
        return True
    _check(root.right)
    _check(root.left)
    return False

def TEST_BST_TREE_RIGHT_BIGGER():
    r = Node(5)
    for i in range(10, 0, -2):
        r = insert(r, i)
    return _check(r)


def run_all_tests():
    red_color_add = '\033[91m'
    green_color_add = '\033[92m'
    end_color_add = '\033[0m'
    success_str = green_color_add + "passed" + end_color_add
    fail_str = red_color_add + "failed" + end_color_add

    passed_tests_count = 0
    all_tests_count = 0

    test_funcs = [TEST_DEL_EXIST, TEST_DEL_NOT_EXIST, TEST_SEARCH_EXIST_NODE, TEST_SEARCH_NOT_EXIST_NODE,
                  TEST_BST_TREE_RIGHT_BIGGER]
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