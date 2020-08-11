#!/bin/sh

message="auto-commit from $USER@$(hostname -s) on $(date)"
GIT=`which git`
REPO_DIR=$(pwd)

cd ${REPO_DIR}
${GIT} add -A
${GIT} commit -m "$message"
${GIT} pull --rebase
gitPush=$(${GIT} push -vvv origin master 2>&1)