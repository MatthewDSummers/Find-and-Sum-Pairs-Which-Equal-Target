# An algorithm which accepts only an array of distinct numbers,
# then finds pairs of the non-identical numbers (can't be paired with itself)
# within the array which can be summed to equal the target sum

def twoNumberSum(array, targetSum):
    if array != []:   # don't accept empty arrays (line 28)
        sum, occurrences = [], []

        for i in array:
            if i not in occurrences:   #append only distinct numbers from original array to "occurrences"
                occurrences.append(i)
        if len(occurrences) != len(array):   #if original array is not the same length as "occurrences", the original array contained duplicate numbers; return
            return("Contains duplicates")

        else:   #if array is not empty and only has distinct numbers...
            for i in range(len(array)):   # loop through array
                for j in range(i, len(array)):   # nested loop through array to compare subsequent indices against current initial index
                    if array[i] != array[j]:   #only process distinct numbers (don't sum itself with itself)
                        if (array[i]+array[j]) == targetSum:   #check if the sum of the current indices equal the target sum
                            sum.append([array[i], array[j]])  #if so, then append them to the resulting array "sum"

        if sum == []:
            return("No pair equals the target sum")
        else:
            return(sum)

    else:
        return("Give me an array, please")

print(twoNumberSum([6,5,-1,11,4], 10))   #returns pairs which when summed equal the target
print(twoNumberSum([3,5,8], 20))   #(no match)
print(twoNumberSum([1,1,2,2,3,4,5,5], 2))   #(has duplicate)
print(twoNumberSum([], 10))   #   (given array is empty)

