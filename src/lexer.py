import ply.lex as lex

# Lista de tokens
tokens = [
    'ID', 'NUM', 'FLOAT',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER',
    'ASSIGN',
    'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE',
    'COMMA', 'SEMI',
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',
    'REAL', 'INT', 'VAR',
    'WHILE', 'IF', 'ELSE'
]

# Regras de expressões regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POWER = r'\^'
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_SEMI = r';'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_EQ = r'=='
t_NE = r'<>'

# Palavras-chave
reserved = {
    'var': 'VAR',
    'real': 'REAL',
    'int': 'INT',
    'while': 'WHILE',
    'if': 'IF',
    'else': 'ELSE'
}

# Regras de expressões regulares com ações
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Checa por palavras-chave reservadas
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espaços e tabs
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Constrói o lexer
lexer = lex.lex()
