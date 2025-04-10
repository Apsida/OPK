from rational import *

def TEST_CREAT_ZERO_DROB():
    was_exception = False
    try:
        a = create(0,0)
    except Exception:
        was_exception = True
    return was_exception

def TEST_CREAT_VOID():
    was_exception = False
    try:
        a = create(0, 0)
    except Exception:
        was_exception = True
    return was_exception

def TEST_ADD_ZERO():
    a = create(1,2)
    b = create(0,1)
    result = add(a,b)
    if result.numer != 1 and result.denom != 2:
        return False
    return True

def TEST_ADD_BIG_NUMBERS():
    a = create(1000, 2134)
    b = create(2134,24)
    result = add(a,b)
    if simplify(result) != 1144489:
        return False
    return True

def TEST_SUB_SIMILAR():
    a = create(1,2)
    b = create(1,2)
    result = sub(a,b)
    if simplify(result) != 0:
        return False
    return True

def TEST_MUL_ZERO():
    a = create(1,2)
    b = create(0,2)
    result = mul(a,b)
    if result.numer != 0:
        return False
    return True

def TEST_DIV_ZERO():
    a = create(1,2)
    b = create(0,2)
    was_exception = False
    try:
        div(a, b)
    except Exception:
        was_exception = True
    if was_exception:
        return  True
    else:
        return False

def TEST_POWER_ZERO():
    a = create(1,2)
    result = power(a,0)
    if simplify(result) != 1:
        return False
    return True

def TEST_POWER_BIG_POWERING():
    a = create(4,10)
    result = power(a,10)
    if result.numer == 4**10 and result.denom == 10*10:
        return False
    return True

def TEST_SIMPLIFY_ZERO():
    a = create(0,2)
    result = simplify(a)
    if result != 0:
        return False
    return True

def TEST_SIMPLIFY_TO_FLOAT():
    a = create(1,3)
    result = simplify(a)
    epsylon = 0.000001
    is_equal = abs(result - 0.33333) < epsylon
    if is_equal:
        return False
    return True


def run_all_tests():
    red_color_add = '\033[91m'
    green_color_add = '\033[92m'
    end_color_add = '\033[0m'
    success_str = green_color_add + "passed" + end_color_add
    fail_str = red_color_add + "failed" + end_color_add

    passed_tests_count = 0
    all_tests_count = 0

    test_funcs = [TEST_CREAT_ZERO_DROB, TEST_CREAT_VOID, TEST_ADD_ZERO, TEST_ADD_BIG_NUMBERS, TEST_SUB_SIMILAR, TEST_MUL_ZERO, TEST_DIV_ZERO,
                  TEST_POWER_ZERO, TEST_POWER_BIG_POWERING, TEST_SIMPLIFY_ZERO, TEST_SIMPLIFY_TO_FLOAT]
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