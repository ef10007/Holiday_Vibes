#!/bin/sh

DATE=`date +%d.%b.%Y`

MSG="$DATE"

git add --all
git commit -am "${MSG}"

git push
