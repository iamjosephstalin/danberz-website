
path = r'assets/js/main.js'
offset = 40036
length = 1000

with open(path, 'r', encoding='utf-8') as f:
    f.seek(offset)
    content = f.read(length)
    print(content)
