# bash
## parse arguments
* https://sookocheff.com/post/bash/parsing-bash-script-arguments-with-shopts/

```bash
while getopts ":t:" opt; do
  case ${opt} in
    t )
      target=$OPTARG
      ;;
    \? )
      echo "Invalid option: $OPTARG" 1>&2
      ;;
    : )
      echo "Invalid option: $OPTARG requires an argument" 1>&2
      ;;
  esac
done
shift $((OPTIND -1))
```

## random
```bash
# print executed commands to terminal for debugging
$ set -x
```

## cli skeleton
```bash
#!/bin/bash

# referance another dir
reldir=${0%/*}
here=$(cd $reldir && pwd)
utils=$(cd $here/../utils && pwd)
cd $here

function usage {
  echo "$0 arg1 arg2"
  echo ""
  echo "$0 example1 example2"
  exit 1
}

arg1=$1
arg2=$2
# if needed, reference another util script
# source $utils/anotherscript.sh

# check required args and set other vars
case "$arg1" in
  foo)  woo2=foo; woo3="blah";;
  bar)  woo2=bar; woo3="blaah";;
  *) echo -e "woo '$woo' is not recognized\n"; exit 1;;
esac

# set env vars
export PS1="test prompt> "

# set other vars/do things
command=`command`
if [ -z "$command" ] # if [ -n "$command" ]
then
  echo "testing"
else
  echo "more testing"
fi

# ask for user input to continue
# -r = disble backslash escaping
# -p = prompt string
read -r -p "Continue? y/n: "
if [ "$REPLY" = 'y' ]; then
  echo "ok, continuing"
else
  echo "exiting"
  exit 1
fi

# (set -x; command > /dev/null)

function help {
  echo "example command"
  echo "example command"
  echo "Ctrl-D to exit"
}
export -f help

cat -<<EOF
=====================================================================

woo2=$woo2
woo3=$woo3

blah blah instructions

Type Ctrl-D to exit

=====================================================================

EOF

exec /bin/bash
```
