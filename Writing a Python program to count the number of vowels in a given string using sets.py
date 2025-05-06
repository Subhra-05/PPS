def vowel_count(str):
	count = 0
	vowel = set("aeiouAEIOU")
	for char in str:
		if char in vowel:
			count+=1
	return count
	# Write your code here to count the vowels
	
str = input()
vowel_count(str)
print(vowel_count(str))
