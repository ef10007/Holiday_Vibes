#!/bin/sh

DATE=`date +%dth.%b.%Y`

MSG="$DATE"

git add --all
git commit -am "${MSG}"

git push
