'''
    적성일 : 2023년 11월 15일
    작성자 : 202195057 손패택
    설면: 
'''
text = "There's a reason some people are working to make \
    it harder to vote, especially for people of color. \
        It's because when we show up, things change."
        

text2 = text.split()
print(text2)
print('wordl count : ', len(text2))



text = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG U+ Mystic Pink 30%, SKT Mystic Blue not disclosed) '


low_text = text.lower()  

text = ''
for word in low_text.split(' '):
    if word == 'kt' or word == 'samsung' or word == 'lg' or word == 'skt':
        text += '** '
    else:
        text += word + ' '

print('text1 : ', text)


split_text = low_text.split(' ')
text=''
for word in split_text :
    if word == 'kt' or word == 'samsung' or word == 'lg' or word == 'skt':
        text += word.replace(word, '** ')
    else:
        text += word + ' '    

print('text2 : ', ''.join(text))  

text = text.replace('KT', '**').replace('Samsung', '**').replace('SKT', '**').replace('LG', '**')

print(text)



text_lower = text.lower()


replace_words = ['kt', 'samsung', 'skt', 'lg']

for word in replace_words:
    text_lower = text_lower.replace(word, '**')

print(text_lower)