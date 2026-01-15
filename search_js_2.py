
path = r'assets/js/main.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Search for window.gsap usage
start_index = content.find('window.gsap')
if start_index != -1:
    print(f"window.gsap context: {content[start_index:start_index+500]}")

# Search for any object with 'trigger' property which is common in ScrollTrigger
import re
# Look for {trigger: or "trigger":
matches = [m for m in re.finditer(r'\{.{0,20}trigger:', content)]
for m in matches:
    start = max(0, m.start() - 50)
    end = min(len(content), m.end() + 300)
    print(f"Trigger match at {m.start()}: {content[start:end]}")
