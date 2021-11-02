# vim
## editing
* j k h l: up down left right
* w b: hop word forward and back
* yy: yank line
* dd: delete line
* dw: delete word (from current place)
* dj: delete line + line below
* p and shift-p: paste line below or above
* u: undo last command
* shift-v: highlight line (visual)
* v: visual mode
* ctrl-c: leave from insert mode
* o and shift-o: insert new line below or above
* a: move over and insert
* shift-a: insert at end of line
* shift-i: insert at beginning of line
* x: delete character (normal mode)
* s: delete character and insert (normal mode)
* shift-d: delete rest of line
* shift-c: delete rest of line and insert
* shift-s: delete line and insert

## Navigation
* ctrl-P: fzf GFiles (git ls-files)
* `<space>-gd`: get definition (fzf)
* `<space>-gr`: get references (fzf)
* ctrl-^: jump to last edited file
* ctrl-o and ctrl-i: jump back and forth in history
* `/<word>`: search (enter and n to hop through results, shift-n to hop back)
* `:%s/<original>/<replacement>/gc`: search and replace entire doc with confirmation
* `*`: jump to next occurrence of word (cursor is on) - can continue with n
* `#`: jump to previous accurrence of word (cursor is on) - can continue with n
