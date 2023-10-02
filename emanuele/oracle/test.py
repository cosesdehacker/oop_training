from emanuele.oracle.main import get_answer


def test_get_answer():
    prev_answer = get_answer()
    for _ in range(1, 1000):
        last_answer = get_answer(prev_answer)
        if last_answer == prev_answer:
            print("todo mal")
            return False
        else:
            prev_answer = last_answer
    print("todo bastante bien")
    return True


if __name__ == '__main__':
    test_get_answer()
