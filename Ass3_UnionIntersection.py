
import itertools



def fuzzy_union(set1, set2):
    union = {}
    for key in set1.keys():
        union[key] = max(set1[key], set2[key])
    return union

def fuzzy_intersection(set1, set2):
    intersection_set = {}
    for key in set1.keys():
        intersection_set[key] = min(set1[key], set2[key])
    return intersection_set


def fuzzy_complement(set1):
    complement_set = {}
    for key in set1.keys():
        complement_set[key] = 1 - set1[key]
    return complement_set


def fuzzy_difference(set1, set2):
    difference_set = {}
    for key in set1.keys():
        difference_set[key] = min(set1[key], 1 - set2[key])
    return difference_set


def cartesian_product_fuzzy_sets(set1, set2):
    cartesian_product = {}
    for key1, value1 in set1.items():
        for key2, value2 in set2.items():
            cartesian_product[(key1, key2)] = min(value1, value2)
    return cartesian_product


def max_min_composition(relation1, relation2):
    composition = {}
    for (x, z1), (z2, y) in itertools.product(relation1.keys(), relation2.keys()):
        if z1 == z2:
            if (x, y) in composition:
                composition[(x, y)] = max(
                    composition[(x, y)], min(relation1[(x, z1)], relation2[(z2, y)])
                )
            else:
                composition[(x, y)] = min(relation1[(x, z1)], relation2[(z2, y)])
    return composition


# Example usage:

# Define fuzzy sets
set1 = {"x1": 0.7, "x2": 0.5}
set2 = {"x1": 0.4, "x2": 0.6}

# Operations on fuzzy sets
union_set = fuzzy_union(set1, set2)
intersection_set = fuzzy_intersection(set1, set2)
complement_set1 = fuzzy_complement(set1)
difference_set = fuzzy_difference(set1, set2)

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Complement of Set 1:", complement_set1)
print("Difference (Set1 - Set2):", difference_set)

# Create fuzzy relations
relation1 = cartesian_product_fuzzy_sets(set1, set2)
relation2 = cartesian_product_fuzzy_sets(set2, set1)

print("relation1 : ", relation1)
print("relation 2: ", relation2)

# Max-Min Composition
composition = max_min_composition(relation1, relation2)

print("Max-Min Composition:")
for pair, value in composition.items():
    print(pair, ":", value)
