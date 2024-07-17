import contextlib

text = "insert your text here"
try:
    file = open("output/rick-roll.txt", "w")
    file.write("[" + text + "]" + "(https://youtu.be/dQw4w9WgXcQ?si=nelBnas0wSu0yxWJ)")
    print("[" + text + "]" + "(https://youtu.be/dQw4w9WgXcQ?si=nelBnas0wSu0yxWJ)")
    file.close()
except FileNotFoundError:
    print("[" + text + "]" + "(https://youtu.be/dQw4w9WgXcQ?si=nelBnas0wSu0yxWJ)")




