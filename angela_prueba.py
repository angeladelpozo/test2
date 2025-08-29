
import os, sys


print("hola mundo")

input_file = sys.argv[1]

if os.path.exists(input_file):
    print('Existe el fichero: %s' % (input_file))
else:
    sys.exit(2)