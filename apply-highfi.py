#!/usr/bin/env python3
from pathlib import Path
import re, shutil, sys
root=Path(__file__).resolve().parent
html=root/'index.html'
if not html.exists():
    sys.exit('ERROR: index.html not found. Run this from your GitHub Pages repository root.')
source=html.read_text(encoding='utf-8')
if 'hf-devops-highfi.css' in source:
    print('High-fi DevOps animation assets are already linked. No change made.')
    sys.exit(0)
# Add assets references only; the original README-derived page markup and all links remain untouched.
css='<link rel="stylesheet" href="assets/css/hf-devops-highfi.css">\\n'
js='<script src="assets/js/hf-devops-highfi.js" defer></script>\\n'
if re.search(r'</head>',source,re.I):
    source=re.sub(r'</head>',css+'</head>',source,count=1,flags=re.I)
else:
    source=css+source
if re.search(r'</body>',source,re.I):
    source=re.sub(r'</body>',js+'</body>',source,count=1,flags=re.I)
else:
    source+='\\n'+js
backup=html.with_suffix('.html.highfi-backup')
if not backup.exists(): shutil.copy2(html,backup)
html.write_text(source,encoding='utf-8')
print('Updated index.html with high-fidelity 3D DevOps animation links.')
print('Original saved as:',backup.name)
print('Existing README content, internal links and project URLs were not rewritten.')
