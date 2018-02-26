def answer(chunk, word):
	if word not in chunk:
		return chunk

	left_location = chunk.find(word)
	right_location = chunk[left_location + 1:].find(word) + left_location + 1

	if left_location >= 0 and right_location >= 0 and ord(chunk[left_location]) < ord(chunk[right_location]):
		return answer(chunk[:left_location] + chunk[left_location + len(word):], word)
	elif left_location >= 0 and right_location >= 0 and ord(chunk[left_location]) >= ord(chunk[right_location]):
		return answer(chunk[:right_location] + chunk[right_location + len(word):], word)
	elif left_location >= 0 and right_location < 0:
		return answer(chunk[:left_location] + chunk[left_location + len(word):], word)

message = "lololololo"
inserted_trash = "lol"
print(answer(message, inserted_trash))

message = "goodgooogoogfogoood"
inserted_trash = "goo"
print(answer(message, inserted_trash))
