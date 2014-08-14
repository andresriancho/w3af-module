#!/bin/bash -x

if [ $CIRCLE_BRANCH == 'master' ]; then
    git remote
    git checkout w3af-master
    git pull -v

    git checkout master
    git merge --squash -s subtree --no-commit w3af-master
else
    git remote
    git checkout w3af-develop
    git pull -v

    git checkout develop
    git merge --squash -s subtree --no-commit w3af-develop
fi