#!/bin/bash -x

git remote add -f w3af git://github.com/andresriancho/w3af.git
git fetch w3af

git branch -D w3af-master
git branch -D w3af-develop
git checkout -b w3af-master w3af/master
git checkout -b w3af-develop w3af/develop

if [ $CIRCLE_BRANCH == 'master' ]; then
    git checkout master
    git rm -r w3af-repo

    git read-tree --prefix=w3af-repo/ -u w3af-master
    git checkout w3af-master
    git pull -v

    git checkout master
    git merge --squash -s subtree --no-commit w3af-master
else
    git checkout $CIRCLE_BRANCH
    git rm -r w3af-repo

    git read-tree --prefix=w3af-repo/ -u w3af-develop
    git checkout w3af-develop
    git pull -v

    git checkout $CIRCLE_BRANCH
    git merge --squash -s subtree --no-commit w3af-develop
fi