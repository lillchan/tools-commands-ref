# python
## cli skeleton - using cmd
```python
import cmd

class Main(BaseCmd):
  prompt = 'prompt> '

  def help_command(self):
    print('Help description of what the command does')

  def do_command(self, args):
    CmdCommand().cmdloop()

if __name__ == '__main__':
  Main().cmdloop()
```

## cli skeleton - using argparse
```python
```
