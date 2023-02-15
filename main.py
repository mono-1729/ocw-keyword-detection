import whisper
model = whisper.load_model("base")
# result = model.transcribe("準備したファイル名を指定") # 今回の記事ではtest.m4aを用います。
result = model.transcribe("CZLLVP-Qd5c.mp3", verbose=True,language="ja",)
sentences=list(result['text'].split("\n"))
print(sentences)
sentences.pop()
for i in range(len(sentences)):
    bracket=sentences[i].find(']')
    colon=sentences[i].find(':')
    time=int(sentences[i][1:colon])*60+int(sentences[i][colon+1:colon+6])
    sentences[i]={'time':time,'text':sentences[i][bracket+1:]}
# for sentence in sentences:
#     print(sentence['time'])