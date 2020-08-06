#!/bin/sh

message="auto-commit from $USER@$(hostname -s) on $(date)"
GIT=`which git`
REPO_DIR=$(pwd)


cd ${REPO_DIR}

# pull rebase - remote master
${GIT} checkout master
${GIT} pull --all

# stage & commit - local branch
${GIT} checkout local
${GIT} add --all .
${GIT} commit -m "$message"

# merge local branch with master
${GIT} checkout master
${GIT} merge local --no-edit

# push changes to remote
gitPush=$(${GIT} push -vvv origin master 2>&1)
echo "$gitPush"


# checkout to local branch
${GIT} checkout local
