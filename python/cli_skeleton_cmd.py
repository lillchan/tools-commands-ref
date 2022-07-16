import cmd

class BaseCmd(cmd.Cmd):
  """ common command elements """
  def __init__(self):
    pass
  
  def cmdloop(self):
    do_again = True
    while(do_again):
      try:
        pass
      except KeyboardInterrupt:
        print("ctrl-d to quit")

class Main(BaseCmd):
  prompt = 'prompt> '

  def help_command(self):
    print('Help description of what the command does')

  def do_command(self, args):
    CmdCommand().cmdloop()

if __name__ == '__main__':
  Main().cmdloop()