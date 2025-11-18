"""
PROBLEM:

Imagine 100 lockers numbered 1 to 100 with 100 students lined up in front of those 100 lockers:

The first student opens every locker.

The second student closes every 2nd locker.

The 3rd student changes every 3rd locker; if it's closed, she opens it; if it's open, she closes it.

The 4th student changes every fourth locker.

The 5th student changes every 5th locker.

That same pattern continues for all 100 students.

Which lockers are left open after all 100 students have walked the row of lockers?
"""

STUDENTS = 100


def solve_locker_problem():
    lockers = [0] * 100

    for student in range(1, STUDENTS + 1):
        for i, locker in enumerate(lockers):
            if (i + 1) % student == 0:
                if lockers[i] == 0:
                    lockers[i] = 1
                elif lockers[i] == 1:
                    lockers[i] = 0

    open_lockers = [i + 1 for i, locker in enumerate(lockers) if locker == 1]

    return open_lockers


def main():
    solution = solve_locker_problem()
    print(solution)


if __name__ == "__main__":
    main()
