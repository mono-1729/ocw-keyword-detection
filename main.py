import whisper
model = whisper.load_model("base")
# result = model.transcribe("準備したファイル名を指定") # 今回の記事ではtest.m4aを用います。
result = model.transcribe("CZLLVP-Qd5c.mp3", verbose=True,language="ja",)
sentences=list(result['text'].split("\n"))
print(sentences)