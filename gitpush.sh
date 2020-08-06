#!/bin/sh

message="auto-commit from $USER@$(hostname -s) on $(date)"
GIT=`which git`
REPO_DIR=$(pwd)


cd ${REPO_DIR}


# stage & commit - local branch
${GIT} checkout local
${GIT} pull --rebase
${GIT} add --all .
${GIT} commit -m "$message"

# push changes to remote
gitPush=$(${GIT} push -vvv origin master 2>&1)
echo "$gitPush"
