
path = r'assets/js/main.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

index = content.find('hero-sequence')
if index != -1:
    start = max(0, index + 1500)
    end = min(len(content), index + 2500)
    with open('hero_snippet_3.txt', 'w', encoding='utf-8') as out:
        out.write(content[start:end])
    print("Snippet written to hero_snippet_3.txt")
else:
    print("hero-sequence not found")
