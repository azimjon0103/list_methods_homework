from re import A


def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    ##a=fruits.count("apple")
   # b=5-a
    
    i=0
    ans=[]
    while i<len(fruits):
        if fruits[i]!="apple":
            ans.append(fruits[i])
        i+=1
    return ans
print(main(["apple", "banana", "apple",  "apple"]))    