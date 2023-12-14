"""Top 3 salaries module."""


def top3_salaries_stats(
    *departments: tuple[str, dict],
    excluding: tuple[str, ...] = None,
) -> tuple[tuple[str, float], tuple[str, float]]:
    """Find 3 most- and least-paid departments in a given tuple by average value.

    Args:
        departments: a tuple with departments names their values.
        excluding: tuple with names of departments to be excluded from stats, defaults to None.

    Returns:
        stats: tuple of top 3 most and least paid departments with their average salaries.
    """
    avg_salaries = {}
    for department in departments:
        if excluding is None or department[0] in excluding:
            salaries = department[1].values()
            avg_salary = round(sum(salaries) / len(salaries), 2) if salaries else 0
            avg_salaries[department[0]] = avg_salary

    salaries_sorted = sorted(avg_salaries.items(), key=lambda srt: srt[1], reverse=True)
    top3_most_paid = salaries_sorted[:3]
    top3_least_paid = salaries_sorted[-3:][::-1]
    return tuple(top3_most_paid), tuple(top3_least_paid)

# ----------------------
# ПРОВЕРКА

dep1 = (
        'test1', {
            'test1.1': 231.231,
            'test1.2': 312.312,
            'test1.3': 123.123,
        }
)
dep2 = (
        'test2', {
            'test2.1': 228.228,
            'test2.2': 1337.337,
        }
)

print(top3_salaries_stats(dep1, dep2))