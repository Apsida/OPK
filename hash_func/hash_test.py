from main import *
from random import randint

def run_all_tests():
    red_color_add = '\033[91m'
    green_color_add = '\033[92m'
    end_color_add = '\033[0m'
    success_str = green_color_add + "passed" + end_color_add
    fail_str = red_color_add + "failed" + end_color_add

    passed_tests_count = 0
    all_tests_count = 0

    test_funcs = [TEST_SIZE_CORRECT, TEST_DEL_EXIST, TEST_DEL_NOT_EXIST, TEST_SEARCH_EXIST_KNOT, TEST_SEARCH_NOT_EXIST_KNOT,
                  TEST_BST_TREE_CHECK_IS]
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