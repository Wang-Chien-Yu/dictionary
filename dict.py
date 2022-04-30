#讀取檔案
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count +=1
		#if count % 1000 == 0: # %求餘數
			#print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')

wc = {} #word_count 

for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1 #如果有value +1
		else:	
			wc[word] = 1 #如果沒有新增key進wc字典

# for w in wc:
# 	if wc[w] > 100:
# 		print(w, wc[w])

while True:
	word = input('請輸入想查詢的字: ')
	if word == 'q':
		print('感謝你的查詢')
		break
	if word in wc:
		print(word, '出現過的次數為', wc[word])
	else:
		print('這個字沒有出現過')


# #dictionary 字典
# #words = {
# # 	'key': 'value'
# # }
# words = {
# 	'ramen': '拉麵',
# 	'pasta': '義大利麵'
# }

# words['tea'] = '茶' #增加新的key到字典

# # print(words['ramen']) #印出字典

# print(words)

# p0 = {
# 	'name':'麥香奶茶',
# 	'price': 15
# }

# p1 = {
# 	'name':'麥香紅茶',
# 	'price': 10
# }

# product = [p0,p1]

# print(product[0]['name'])