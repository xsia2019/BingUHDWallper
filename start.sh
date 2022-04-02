python3 ./bingUHD.py

year=`date +%Y `
month=`date +%m `
day=`date +%d `
hour=`date +%H`
minute=`date +%M`
second=`date +%S`
now=$year.$month.$day.$hour.$minute.$second
this_month=$year-$month

git diff
git config --global user.email "kinofgl@gmail.com"
git config --global user.name "kinofgl"

git add BingUHD/"$this_month"/*.*
git commit -m "updated: $now"
git push -u origin master
