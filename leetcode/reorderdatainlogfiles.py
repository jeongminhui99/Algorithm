from typing import List


def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letters, digit = [],[]
    for log in logs:
        if log.split()[1].isdigit():
            digit.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digit