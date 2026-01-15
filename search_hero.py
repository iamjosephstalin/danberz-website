
path = r'assets/js/main.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

index = content.find('hero-sequence')
if index != -1:
    start = max(0, index - 300)
    end = min(len(content), index + 500)
    print(content[start:end])
else:
    print("hero-sequence not found")
