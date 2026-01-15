
path = r'assets/js/main.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

index = content.find('hero-sequence')
if index != -1:
    start = max(0, index - 500)
    end = min(len(content), index + 500)
    with open('hero_snippet.txt', 'w', encoding='utf-8') as out:
        out.write(content[start:end])
    print("Snippet written to hero_snippet.txt")
else:
    print("hero-sequence not found")
