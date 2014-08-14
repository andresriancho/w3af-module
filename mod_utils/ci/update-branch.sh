#!/bin/bash -x

if [ $CIRCLE_BRANCH == 'master' ]; then
    git checkout w3af-master
    git pull

    git checkout master
    git merge --squash -s subtree --no-commit w3af-master
else
    git checkout w3af-develop
    git pull

    git checkout develop
    git merge --squash -s subtree --no-commit w3af-develop
fi