# Problem
# =================================
# Reshuffle a given word to avoid any repetition of 
# alphabets in a sequence

# Code
# =================================
alphas = str(input("Enter Alphabets : "))

def conCatElements(Array):
	word = ''
	for element in Array:
		word+=element 
	return word

def checkAndRearrange():
	uniqueAlphas = []
	likedAlphas = []
	recentAlpha = ''
	for alpha in alphas:
		if alpha != recentAlpha:
			recentAlpha=alpha
			uniqueAlphas.append(recentAlpha)
		else:
			likedAlphas.append(alpha)
	
	# If non repeated
	if len(likedAlphas)==0:
		print(conCatElements(uniqueAlphas))
	
	# If there were repeated values
	# ====================================
	# FIRST ITERATION
	# ===================================
	else:
		firstLoopCount =0
		secondLoopCount = 0
		for likedAlpha in likedAlphas:
			for uniqueAlpha in uniqueAlphas:
				if likedAlpha != uniqueAlpha:
					# If it's first iteration don't check backwards
					if secondLoopCount==0:
						uniqueAlphas.insert(secondLoopCount, likedAlpha)
						likedAlphas.pop(firstLoopCount)
						secondLoopCount+=1
						break

					# Checking if there is a backwards number
					try:
						if likedAlpha!=uniqueAlphas[secondLoopCount-1]:
							uniqueAlphas.insert(secondLoopCount, likedAlpha)
							likedAlphas.pop(firstLoopCount)
					
					except:
						uniqueAlphas.insert(secondLoopCount, likedAlpha)
						likedAlphas.pop(firstLoopCount)
					break
					
				else:
					secondLoopCount+=1
					
			firstLoopCount+=1
		# Printing new word
		if len(likedAlphas)==0:
			print(conCatElements(uniqueAlphas))
		
		else:
			word = conCatElements(uniqueAlphas)+conCatElements(likedAlphas)
			print(word)

checkAndRearrange()
