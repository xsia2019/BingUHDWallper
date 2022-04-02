python3 ./bingUHD.py

time=$(date "+%Y.%m.%d %H:%M:%S")

month=$(date -d yesterday "+%Y-%m")

git diff
git config --global user.email "kinofgl@gmail.com"
git config --global user.name "kinofgl"

git add BingUHD/"$month"/*.*
git commit -m "updated: $time UTC"
git push -u origin master
