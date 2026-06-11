import os
import shutil

ROOT_DIR = r'c:\Users\invde\OneDrive\Documents\gnss-orbital-py'

def safe_mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# 1. Create target directories
src_dir = os.path.join(ROOT_DIR, 'src')
scripts_dir = os.path.join(ROOT_DIR, 'scripts')
archive_dir = os.path.join(ROOT_DIR, 'archive')

frontend_dir = os.path.join(ROOT_DIR, 'frontend')
frontend_js_dir = os.path.join(frontend_dir, 'js')
frontend_css_dir = os.path.join(frontend_dir, 'css')

safe_mkdir(src_dir)
safe_mkdir(scripts_dir)
safe_mkdir(archive_dir)
safe_mkdir(frontend_js_dir)
safe_mkdir(frontend_css_dir)

# 2. Move backend and orbital into src
backend_src = os.path.join(ROOT_DIR, 'backend')
backend_dest = os.path.join(src_dir, 'backend')
if os.path.exists(backend_src) and not os.path.exists(backend_dest):
    shutil.move(backend_src, backend_dest)

orbital_src = os.path.join(ROOT_DIR, 'orbital')
orbital_dest = os.path.join(src_dir, 'orbital')
if os.path.exists(orbital_src) and not os.path.exists(orbital_dest):
    shutil.move(orbital_src, orbital_dest)

# 3. Archive old files
old_files = ['app.py', 'karmaloop.yaml']
for f in old_files:
    src = os.path.join(ROOT_DIR, f)
    if os.path.exists(src):
        shutil.move(src, os.path.join(archive_dir, f))

# 4. Move frontend JS and CSS
app_js_src = os.path.join(frontend_dir, 'app.js')
if os.path.exists(app_js_src):
    shutil.move(app_js_src, os.path.join(frontend_js_dir, 'app.js'))

style_css_src = os.path.join(frontend_dir, 'style.css')
if os.path.exists(style_css_src):
    shutil.move(style_css_src, os.path.join(frontend_css_dir, 'style.css'))

# Any other loose .py scripts in frontend (like update scripts) can be moved to archive
for f in os.listdir(frontend_dir):
    if f.endswith('.py'):
        shutil.move(os.path.join(frontend_dir, f), os.path.join(archive_dir, f))

print("Reorganization complete.")
