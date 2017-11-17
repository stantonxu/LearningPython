# find the missing number from the array
def missing_number(nums):
	n = len(nums)
	return n * (n+1) / 2 - sum(nums)
	
#nums = [2, 3, 9, 6, 5, 8, 1, 0, 4]
#print(missing_number(nums))


# reverse vovels of a string
import re

def reverseVowels(s):
	vowels = re.findall('(?i)[aeiou]', s)
	return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
	
#print(reverseVowels("aA"))
#print(reverseVowels("Hello"))


# valid perfect square
def isPerfectSquare(num):
	r = num
	while r*r > num:
		r = (r + num//r) // 2
	return r*r == num
	
#print(isPerfectSquare(16))
#print(isPerfectSquare(15))


# Guess Number Higher or Lower
def guessNumber(n):
	lo, hi = 1, n
	while lo < hi:
		mid = lo + (hi - lo) // 2
		if guess(mid) == -1:
			hi = mid - 1
		elif guess(mid) == 1:
			lo = mid + 1
		else:
			return mid
	return lo
	
def guess(n):
	m = 7
	if n<m: return 1
	elif n>m: return -1
	else: return 0

#print(guessNumber(11))

