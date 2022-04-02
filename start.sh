python3 ./bingUHD.py

year=`date +%Y `
month=`date +%m `
day=`date +%d `
hour=`date +%H`
now=$year-$month-$day-$hour


git config --global user.email "kinofgl@gmail.com"
git config --global user.name "kinofgl"

git add .
git commit -m "$now"