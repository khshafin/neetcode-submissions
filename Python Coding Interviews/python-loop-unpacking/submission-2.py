from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    
    for tuples in scores:
        best_name, best_score = tuples[0], tuples[1]

    for name, score in scores:
        if score > best_score:
            best_score = score
            best_name = name
    return best_name
        


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
