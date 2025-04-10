import os

from faster_whisper import WhisperModel



def init_model():
    model = WhisperModel(
        "medium",
        device="cpu",
        download_root=f"{os.getcwd()}/cache_model",
    )
    return model

model = init_model()

segments, info = model.transcribe(
    f"POINT СМОТРЯТ АЛЬБЕРТА ⧸ Мозг на игле. Как работает зависимость？ [urSCve8uRhc].m4a",
    beam_size=5,
    word_timestamps=True,
)

print(info)

for segment in segments:
    # print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
    print(segment.start, segment.end, segment.text)
    for word in segment.words:
        print("[%.2fs -> %.2fs] %s" % (word.start, word.end, word.word))

# model = WhisperModel(
#     self._type_model,
#     device=self._device,
#     download_root=f"{os.getcwd()}/cache_model",
# )