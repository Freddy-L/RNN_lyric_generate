import random


poetry = open("./poetry.txt", 'r')
rap = open("./rap.txt", "r")
rap2 = open("./rapv2.txt", 'r')

rap_lyrics = []
poems = []

reversed_rap = open('./reversed_rap.txt', 'w')
reversed_text = open('./reversed_text.txt', 'w')

length = []
for line in poetry.readlines():
    title = line.strip().replace(' ', '').split(':')[0]
    poem = list(line.strip().replace(' ', '').split(':')[1])
    poem.reverse()
    try:
        if poem[0] == '。':
            poem = poem[1:]
            length.append(len(poem))
        poems.append(title+':'+''.join(poem)+"。"+'\n')
    except:
        continue

for line in rap.readlines():
    title = line.strip().replace(' ', '').split(':')[0]
    lyric = list(line.strip().replace(' ', '').split(':')[1])
    lyric.reverse()
    try:
        if lyric[0] == '。':
            lyric = lyric[1:]
            length.append(len(lyric))
        rap_lyrics.append(title + ':' + ''.join(lyric) + "。" + '\n')
    except:
        continue

for line in rap2.readlines():
    title = line.strip().replace(' ', '').split(':')[0]
    lyric = list(line.strip().replace(' ', '').split(':')[1])
    lyric.reverse()
    try:
        if lyric[0] == '。':
            lyric = lyric[1:]
            length.append(len(lyric))
        rap_lyrics.append(title + ':' + ''.join(lyric) + "。" + '\n')
    except:
        continue


random.shuffle(rap_lyrics)
texts = rap_lyrics+poems
random.shuffle(texts)

for line in texts:
    reversed_text.write(line)

for line in rap_lyrics:
    reversed_rap.write(line)

reversed_text.close()
reversed_rap.close()
poetry.close()


length.sort()
print(length[int(0.95*len(length))])


# test = '鹊头白看那，惊不倘光冰。枝花连敛栗，别*弹醉长。月浴亦夜听，明日残吟钟'
# test = list(test)
# test.reverse()
# print(''.join(test))
# s = list('脑此能不，宵去想也我没们陌当的真我，熬为无，套开一想不睡，场随，票丽歌药走歌的你')
# s.reverse()
# print(''.join(s))


