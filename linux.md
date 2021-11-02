# linux
# chmod
* 3 groups (in this order): user, group, other
* 3 permission levels: read (r), write (w), execute (x)
* TODO: modifying permissions

# random
```bash
# how long has my computer been running
$ uptime

# check diff btw files (-u=unified mode, -c=context mode)
$ diff [-cu]

# check and kill running processes
# lots of output, should | grep for specific process
$ ps -ef
$ kill <PID>

# get IP for domain (can also run against an IP)
$ host google.com

# see the hops needed to get to a destination (or where it gets stuck)
$ traceroute google.com

# uppercase
$ echo 'something' | awk '{print toupper($0)}'

# manual
$ man <command>
```