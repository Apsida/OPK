from circle_queue import *

def TEST_CREAT_ZERO_LEN():
    que = circ_queue(0)
    if que.head() != -1:
        return False
    return True

def TEST_CREAT_VOID():
    que = circ_queue(5)
    return not(que.is_empty() != True)

def TEST_ADD_EXTRA_ELEM():
    que = circ_queue(1)
    que.ent_queue(1)
    return not(que.ent_queue(2) != -1)

def TEST_DEL_VOID():
    que = circ_queue(1)
    if que.del_queue() != None:
        return False
    return True

def TEST_FIFO_ALG():
    qu = circ_queue(3)
    qu.ent_queue(1)
    qu.ent_queue(2)
    qu.ent_queue(3)
    err = False
    if qu.head() != 1:
        return err
    qu.del_queue()
    if qu.head() != 2:
        return err
    qu.del_queue()
    if qu.head() != 3:
        return err
    return not(err)

def run_all_tests():
    red_color_add = '\033[91m'
    green_color_add = '\033[92m'
    end_color_add = '\033[0m'
    success_str = green_color_add + "passed" + end_color_add
    fail_str = red_color_add + "failed" + end_color_add

    passed_tests_count = 0
    all_tests_count = 0

    test_funcs = [TEST_CREAT_ZERO_LEN, TEST_CREAT_VOID, TEST_ADD_EXTRA_ELEM, TEST_DEL_VOID, TEST_FIFO_ALG]
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