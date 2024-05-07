import os

dirs = [
    'app',
    'app/templates',
    'data',
    'data/images',
    'models',
    'models/clip_model',
    'vector_db',
    'tests',
]

for dir in dirs:
    os.makedirs(dir, exist_ok=True)

files = [
    '.gitignore',
    'requirements.txt',
    'README.md',
    'app/__init__.py',
    'app/main.py',
    'app/utils.py',
    'vector_db/__init__.py',
    'tests/__init__.py',
    'tests/test_main.py',
]

for file in files:
    open(file, 'a').close()  # 'a' mode doesn't truncate existing files
