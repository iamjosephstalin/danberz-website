
path = r'index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

search_terms = ["Ready-to-Ship", "Global Sourcing", "Project Support"]
for term in search_terms:
    index = content.find(term)
    if index != -1:
        # Find line number
        line_num = content[:index].count('\n') + 1
        print(f"'{term}' found at line {line_num}")
    else:
        print(f"'{term}' not found")
