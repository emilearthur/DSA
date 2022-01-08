"""
Question 1: write a function that finds the anagram of a given string. (Anagram is a word, phrase or name formed by rearranging
the letters of another). Test Case ==> Result {abraham => aaabhmr, mewls =>deelmw}

"""

from collections import Counter
from typing import List, Union

def Anagram(input: str) -> str:
    output = list(input)
    tmep = None
    for i in range(len(output)):
        for j in range(i+1):
            if output[j] > output[i]:
                temp = output[i]
                output[i], output[j] = output[j], temp # was
    return "".join(output)


def checkanagram(anagram: str, orginalword: str) -> bool:
    if len(anagram) != len(orginalword):
        return False
    
    anagramcount = Counter(anagram)
    orginalwordcount = Counter(orginalword)
    for k1, k2 in zip(sorted(anagramcount.items()),sorted(orginalwordcount.items())):
        if k1 != k2 or anagramcount[k1[0]]!=orginalwordcount[k2[0]]:
            return False
    return True


""""Question 3 (Two Way Sum problem): Given an array find the pair of two integers that sum up to a give integer S.
Test case ==> Results {([3, 5, 2, -4, 8, 11], 7) ==> [5,2], ([2, 7, 11, 15], 9) ==> [2, 7]}"""

def twoWayBruteforce(lst:  List[int], pairsum: int) ->  Union[List[int], None]:
    for i in range(len(lst)):
        for j in range(i + 1):
            if lst[i] + lst[j] == pairsum:
                return [lst[i], lst[j]]
    return None

def twoWayBruteforceAll(lst:  List[int], pairsum: int) ->  Union[List[List[int]], None]:
    pairvalues = []
    for i in range(len(lst)):
        for j in range(i + 1):
            if lst[i] + lst[j] == pairsum:
                pairvalues.append([lst[i], lst[j]])
    return pairvalues

def twoWayOptimize(lst:  List[int], pairsum: int) ->  Union[List[int], None]:
    hash = dict()
    for i in range(len(lst)):
        complement = pairsum - lst[i]
        if complement in hash:
            return [lst[i], hash[complement]]
        else:
            hash[lst[i]] = lst[i]
    return None


def twoWayOptimizeAll(lst:  List[int], pairsum: int) ->  Union[List[int], None]:
    hash = dict()
    pairValues = []
    for i in range(len(lst)):
        complement = pairsum - lst[i]
        if complement in hash:
            pairValues.append([lst[i], hash[complement]])
        else:
            hash[lst[i]] = lst[i]
    return pairValues


if __name__ == "__main__":
    print("Test for anagram")
    print(Anagram("abraham") == "aaabhmr")
    print(Anagram("mewled") == "deelmw")
    print(Anagram("mewling") != "mnwegi" ) # right output is "egilmnw"
    print("\n")
    
    print("Test for check anagram")
    print(checkanagram("abraham","aaabhmr")) # return True
    print(checkanagram("mewled","deelmw"))  # return True
    print(checkanagram("mewled","dddlmp"))  # return False
    print("\n")
    
    print("Test for check twoWayBruteForce")
    lst = [3, 5, 2, -4, 8, 11]
    print(twoWayBruteforce(lst, 7))
    print(twoWayBruteforce(lst, 50))
    print(twoWayBruteforce(lst, -1))
    print("\n")
    
    print("Test for check twoBruteForceAll")
    print(twoWayBruteforceAll(lst, 7))
    print(twoWayBruteforceAll(lst, 50))
    print(twoWayBruteforceAll(lst, -1))
    print("\n")
    
    print("Test for check twoBruteOptmize")
    print(twoWayOptimize(lst, 7))
    print(twoWayOptimize(lst, 50))
    print(twoWayOptimize(lst, -1))
    print("\n")
    
    print("Test for check twoBruteForceAll")
    print(twoWayOptimizeAll(lst, 7))
    print(twoWayOptimizeAll(lst, 50))
    print(twoWayOptimizeAll(lst, -1))
    print("\n")
    
