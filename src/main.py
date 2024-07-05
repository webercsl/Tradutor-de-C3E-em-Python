# main.py

from lexer import lexer
from meuparser import parser
from code_generator import generate_code

def main():
    data = '''
    var
        int cont, num;
        real cont2;

    num = 0;
    while(cont < 10) {
        cont2 = 3.1415 * cont ^ 2;
        if (cont < 5) {
            num = num + cont2;
        }
        else {
            cont = 0;
        }
        cont = cont + 1;
    }
    '''

    lexer.input(data)
    for tok in lexer:
        print(tok)

    ast = parser.parse(data)
    if ast:
        print("Parsing completed successfully!")
        generate_code(ast)
    else:
        print("Parsing failed.")

if __name__ == '__main__':
    main()
