from absl import app
from absl import flags

FLAGS = flags.FLAGS

flags.DEFINE_string('name', 'Jane Random', 'Your name.')

def main(argv):
  if FLAGS.debug:
    print('non-flag arguments:', argv)
  print('Happy, ', FLAGS.name)


if __name__ == '__main__':
  app.run(main)



  i have a new update
