#!/bin/bash

echo 'Creating test content, following errors expected:'
echo 'WARNING: Blog post must have a @name: 40-broken.html
WARNING: Header image must be on first line'
echo 'Output start:'
echo

mkdir src/images
mkdir src/downloads
mkdir src/pages
cd tests
python3 test_downloads.py
python3 test_images.py
python3 test_blog.py
cd ..

python3 make_web.py

if [ $? -eq 0 ]; then
    cd output
    python3 -m http.server
fi
