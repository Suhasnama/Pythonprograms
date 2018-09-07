
import sys

def Cat(filename):
  
  # print(filename)
  f =  open(filename ,'r')
  text = f.read()
  print (text)
  f.close
def main():
  Cat(sys.argv[1])



if __name__ == '__main__':
  main()
