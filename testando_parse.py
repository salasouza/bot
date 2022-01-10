import argparse as args

# Creating parser 

parser = args.ArgumentParser(description = "testando programa parser")

# Add arguments
parser.add_argument('--frase',
                    action='store', 
                    dest='frase',
                    default='Oi, algo aconteceu!',
                    required=False,
                    help='A frase que deseja imprimir x vezes')

parser.add_argument('-n',
                    action='store',
                    dest ='n',
                    required=True,
                    help='O número de vezes que a frase será imprimida')


# Verification of arguments

arguments = parser.parse_args()

for i in range(0, int(arguments.n)):
    
    print(arguments.frase)
