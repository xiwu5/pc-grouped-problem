# one iteration

# letter appearence frenq
# using map to store freq:  1 1 1 - e a t[store as a structure which order doesn't matter]
                                        # a set() since order doesnt matter
# comparing freq: # how to compare two sets:
                        # add this char into the set: failed return T, worked, return F
    # same : group them
    # diff: store the new words freq as a new key in the map/dict:
            # 1 1 1 t a n

# return boolean value: T/F

# if it is F:
    # back to step 1


# comparing/adding char X
# write a helper to break problem into smaller one
# function of this helper: judge is 2 words are anagram

def is_anagram(str1, str2):
    # reorder 2 strings
    # compare the result
    x = sorted(str1)
    y = sorted(str2)
    return x == y 


def grouped(s):
    ans = []
    # iterate
        # check is_anagram of 2 words:
            # if true, add into set
            # if false, skip to next words
    
    # 2 points:first second
    #first = 0
    # stop condition
    for first in range(len(s)):
        second = first + 1
        result = set()
        # letter would be first
        while(second < len(s) - 1):
            if is_anagram(s[first], s[second]):
                result.add(s[first])
                result.add(s[second])
                second += 1
            else:
                second += 1

            ans.append(result)
            
    # move first when second hit the end, reset second
    clean = set()
    for word in ans:
        clean.add(tuple(word))
    return clean


lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
answer_1 = set([("ate", "eat", "tea"), ("bat",), ("nat", "tan")])
print("test1",grouped(lst))
assert grouped(lst) == answer_1

lst = ["bored", "players", "sadder", "dreads", "robed", "parsley"]
answer_2 = set([("bored", "robed"), ("parsley", "players"),
                ("dreads", "sadder")])
assert grouped(lst) == answer_2

lst = ["eat", "tae", "tea", "eta", "aet", "ate"]
answer_3 = set([("aet", "ate", "eat", "eta", "tae", "tea")])
assert grouped(lst) == answer_3

lst = ["eat", "ear", "tar", "pop", "pan", "pap"]
answer_4 = set([("eat",), ("ear",), ("tar",), ("pop",), ("pan",),
                ("pap",)])
assert grouped(lst) == answer_4

lst = []
answer_5 = set()
assert grouped(lst) == answer_5

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
