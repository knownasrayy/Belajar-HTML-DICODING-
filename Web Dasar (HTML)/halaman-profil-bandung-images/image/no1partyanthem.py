import time

# Define the lyrics
lyrics = [
    {"text": "The look of love, the rush of blood", "time": 0.5},  # Dimulai pada 0 detik
    {"text": "The 'She's with me''s, the Gallic shrug", "time": 4.5},  # Dimulai pada 5 detik
    {"text": "The shutterbugs, the Camera Plus", "time": 4.5},  # Dimulai pada 6.5 detik
    {"text": "The black & white and the color dodge", "time": 4.0},  # Dimulai pada 8.5 detik
    {"text": "The good time girls, the cubicles", "time": 4.5},  # Dimulai pada 11 detik
    {"text": "The house of fun, the number one", "time": 4.0},  # Dimulai pada 13.5 detik
    {"text": "Party anthem, oh this lyric maybe", "time": 4.0},  # Dimulai pada 16.5 detik
    {"text": "It's not like I'm falling in love", "time": 5.0},  # Dimulai pada 18.5 detik
    {"text": "I just want you to do me a favour", "time": 4.5},  # Dimulai pada 22.5 detik
    {"text": "It's not like I'm falling in love", "time": 5.0},  # Dimulai pada 27 detik
    {"text": "I just want you to do me a favour", "time": 5.5},  # Dimulai pada 32 detik
    {"text": "There's a bloke standing next to me", "time": 6.0},  # Dimulai pada 37.5 detik
    {"text": "Who looks like he's about to throw", "time": 6.5},  # Dimulai pada 43.5 detik
    {"text": "He's got a look in his eye", "time": 7.0},  # Dimulai pada 50 detik
    {"text": "Like he's plotting something", "time": 7.5},  # Dimulai pada 57 detik
    {"text": "And I'm thinking, 'What's the story?'", "time": 8.0},  # Dimulai pada 64.5 detik
    {"text": "What's the story, what's the story?", "time": 8.5},  # Dimulai pada 72.5 detik
    {"text": "What's the story, what's the story?", "time": 9.0},  # Dimulai pada 81 detik
    {"text": "What's the story, what's the story?", "time": 9.5}   # Dimulai pada 90 detik
]

for lyric in lyrics:
    time.sleep(lyric["time"])
    print(lyric["text"])
