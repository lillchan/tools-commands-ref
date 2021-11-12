# git
```bash
# put current changes on top of master
$ git pull --rebase origin master

# prettier git log
$ git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cD) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative

# if branch has been force pushed, just delete branch, pull and, checkout again
$ git branch -d <branch name>

# reset to a specific commit
$ git reset --hard <commit>

# pr's since last release
$ git log --first-parent --pretty=format:%s <release>..HEAD
```