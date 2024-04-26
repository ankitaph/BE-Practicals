A = {"x1": 0.2, "x2": 0.4, "x3": 0.6, "x4": 0.8}
B = {"x1": 0.3, "x2": 0.5, "x3": 0.7, "x4": 0.9}

R = {("x1", "y1"): 0.2, ("x1", "y2"): 0.4, ("x2", "y1"): 0.6, ("x2", "y2"): 0.8}
S = {("x1", "y1"): 0.3, ("x1", "y2"): 0.5, ("x2", "y1"): 0.7, ("x2", "y2"): 0.9}


def fuzzy_union(A, B):
    union = {}
    for key in A.keys():
        union[key] = max(A[key], B[key])
    return union


# Example usage
union_result = fuzzy_union(A, B)
print("Union:", union_result)


def fuzzy_intersection(A, B):
    intersection = {}
    for key in A.keys():
        intersection[key] = min(A[key], B[key])
    return intersection


# Example usage
intersection_result = fuzzy_intersection(A, B)
print("Intersection:", intersection_result)


def fuzzy_complement(A):
    complement = {}
    for key in A.keys():
        complement[key] = 1 - A[key]
    return complement


# Example usage
complement_result_A = fuzzy_complement(A)
complement_result_B = fuzzy_complement(B)
print("Complement A:", complement_result_A)
print("Complement B:", complement_result_B)


def fuzzy_difference(A, B):
    difference = {}
    for key in A.keys():
        difference[key] = min(A[key], 1 - B[key])
    return difference


# Example usage
difference_result = fuzzy_difference(A, B)
print("Difference:", difference_result)


def max_min_composition(R, S):
    composition = {}
    for x, z in R.keys():
        composition[(x, z)] = 0
        for y in [key[1] for key in R.keys() if key[0] == x]:
            composition[(x, z)] = max(composition[(x, z)], min(R[(x, y)], S[(y, z)]))
    return composition


# Example usage
composition_result = max_min_composition(R, S)
print("Max-Min Composition:", composition_result)
