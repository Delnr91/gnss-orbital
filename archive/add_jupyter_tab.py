import os

file_path = r'c:\Users\invde\OneDrive\Documents\gnss-orbital-py\frontend\app.js'

with open(file_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Update tab switching logic
# Existing tabs: ['overview', 'simulator', 'brain']
tab_logic_old = '''const tabs = ['overview', 'simulator', 'brain'];'''
tab_logic_new = '''const tabs = ['overview', 'simulator', 'brain', 'jupyter'];'''
code = code.replace(tab_logic_old, tab_logic_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Jupyter tab logic added.")
