import sys
def isPalindrome(word):
    ans=True
    i=0
    j=len(word)-1
    while i<j:
        if word[i]!=word[j]:
            ans=False
            break
        i+=1
        j-=1
    return ans
def main():
    if len(sys.argv)<2:
        print("Empty string")
    else:
        print(isPalindrome(sys.argv[1]))
if __name__ == "__main__":
    main()