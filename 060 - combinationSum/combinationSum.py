
def breadthSearch(candidates, target, diff, tempList, result):
    if diff == 0:
        result.append(tempList[:])
        return
    else:
        i = 0
        searchCandidate = True

        while searchCandidate:
            currentCandidate = candidates[i]
            diff = target - currentCandidate

            if diff >= 0:
                tempList.append(currentCandidate)
                breadthSearch(candidates[i:], diff, diff, tempList, result)
                tempList.pop()

            if i < len(candidates) - 1:
                i += 1
            else:
                searchCandidate = False


def combinationSum(candidates, target):
    result = []
    candidates.sort(reverse=True)
    tempList = []
    breadthSearch(candidates, target, target, tempList, result)

    return result


# Test case:
candidates = [2, 3, 5]
target = 8
out = combinationSum(candidates, target)
print("Out:", out)
