#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in range(length):
        if not hash_table_retrieve(ht, weights[i]):
            hash_table_insert(ht, weights[i], [i])
        else:
            hash_table_retrieve(ht, weights[i]).append(i)
    for w in weights:
        diff = limit - w
        cur_diff = hash_table_retrieve(ht, diff)
        if diff + w == limit and cur_diff is not None and diff == w and hash_table_retrieve(ht, w)[1]:
            return [hash_table_retrieve(ht, w)[1], hash_table_retrieve(ht, w)[0]]
        if diff + w == limit and cur_diff is not None:
            if hash_table_retrieve(ht, diff)[0] >= hash_table_retrieve(ht, w)[0]:
                return [hash_table_retrieve(ht, diff)[0], hash_table_retrieve(ht, w)[0]]
            else:
                return [hash_table_retrieve(ht, w)[0], hash_table_retrieve(ht, diff)[0]]
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

# print(get_indices_of_item_weights([9], 1, 9))
print(get_indices_of_item_weights([4, 4,], 2, 8))
# print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5 , 21))
# print(get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9 , 7))