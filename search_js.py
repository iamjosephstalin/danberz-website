
path = r'assets/js/main.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Search for scrub
import re
matches = [m for m in re.finditer(r'scrub:(!0|!1|[0-9.]+)', content)]
for m in matches:
    start = max(0, m.start() - 50)
    end = min(len(content), m.end() + 50)
    print(f"Match at {m.start()}: {content[start:end]}")

print("-" * 20)
# Search for scrollTrigger usage
matches2 = [m for m in re.finditer(r'scrollTrigger:\{', content)]
for m in matches2:
    start = max(0, m.start() - 100)
    end = min(len(content), m.end() + 100)
    print(f"ScrollTrigger at {m.start()}: {content[start:end]}")
