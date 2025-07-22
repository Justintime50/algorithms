from algorithms.sequences.lockers import solve_locker_problem


def test_solve_locker_problem():
    solution = solve_locker_problem()

    assert solution == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
