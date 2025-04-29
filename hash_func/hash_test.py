from main import *
from random import randint

def TEST_SET_FUNC():
    ht = Hash_Table(5, jenkins_hash, 0)
    ht.ht_set("Karl", "Klornet")
    return ht.ht_has("Karl") == 1 and  ht.ht_get("Karl") == "Klornet"

def TEST_FIND_EXIST():
    ht = Hash_Table(5, jenkins_hash, 0)
    ht.ht_set("Karl", "Klornet")
    return ht.ht_has("Karl") == 1

def TEST_FIND_NOT_EXIST():
    ht = Hash_Table(5, jenkins_hash, 0)
    ht.ht_set("Karl", "Klornet")
    return ht.ht_has("Klara") == 0

def TEST_DESTROY_FUNC():
    ht = Hash_Table(5,jenkins_hash,0)
    ht.ht_set("Karl","Klornet")
    ht.ht_destroy()
    return ht.size_t == 0 and ht.table == []

def TEST_GET_EXIST():
    ht = Hash_Table(5, jenkins_hash, 0)
    ht.ht_set("Karl", "Klornet")
    return ht.ht_get("Karl") == "Klornet"

def TEST_GET_NOT_EXIST():
    ht = Hash_Table(5, jenkins_hash, 0)
    ht.ht_set("Karl", "Klornet")
    was_err = False
    try:
        ht.ht_get("Klara")
    except Exception:
        was_err = True
    return was_err

def TEST_DELETE_EXIST():
    ht = Hash_Table(5, jenkins_hash, 0)
    ht.ht_set("Karl", "Klornet")
    ht.ht_delete("Karl")
    return ht.ht_has("Karl") == 0

def TEST_DELETE_NOT_EXIST():
    ht = Hash_Table(5, jenkins_hash, 0)
    ht.ht_set("Karl", "Klornet")
    was_err = False
    try:
        ht.ht_delete("Klara")
    except Exception:
        was_err = True
    return was_err

def TEST_RESIZE():
    ht = Hash_Table(5, jenkins_hash, 0)
    ht.ht_set("Karl", "Karal")
    ht.ht_set("Klara", "Klornet")
    ht.ht_resize(10)
    return ht.size_t == 10 and ht.ht_has("Klara") == 1 and ht.ht_has("Karl") == 1


def run_all_tests():
    red_color_add = '\033[91m'
    green_color_add = '\033[92m'
    end_color_add = '\033[0m'
    success_str = green_color_add + "passed" + end_color_add
    fail_str = red_color_add + "failed" + end_color_add

    passed_tests_count = 0
    all_tests_count = 0

    test_funcs = [TEST_SET_FUNC, TEST_FIND_EXIST, TEST_FIND_NOT_EXIST, TEST_DESTROY_FUNC, TEST_GET_EXIST,
                  TEST_GET_NOT_EXIST, TEST_DELETE_EXIST, TEST_DELETE_NOT_EXIST, TEST_RESIZE]
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