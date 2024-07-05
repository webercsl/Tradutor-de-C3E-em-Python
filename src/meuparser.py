import ply.yacc as yacc
from lexer import tokens

# Precedência e associatividade dos operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'POWER'),
)

def p_program(p):
    '''program : VAR decl_list stmt_list
               | stmt_list'''
    if len(p) == 4:
        p[0] = ('program', p[2], p[3])
    else:
        p[0] = ('program', [], p[1])

def p_decl_list(p):
    '''decl_list : decl_list decl
                 | decl'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_decl(p):
    '''decl : type id_list SEMI'''
    p[0] = ('decl', p[1], p[2])

def p_type(p):
    '''type : REAL
            | INT'''
    p[0] = p[1]

def p_id_list(p):
    '''id_list : id_list COMMA ID
               | ID'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_stmt_list(p):
    '''stmt_list : stmt_list stmt
                 | stmt'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_stmt(p):
    '''stmt : assign_stmt
            | while_stmt
            | if_stmt'''
    p[0] = p[1]

def p_assign_stmt(p):
    '''assign_stmt : ID ASSIGN expr SEMI'''
    p[0] = ('assign', p[1], p[3])

def p_while_stmt(p):
    '''while_stmt : WHILE LPAREN relexpr RPAREN LBRACE stmt_list RBRACE'''
    p[0] = ('while', p[3], p[6])

def p_if_stmt(p):
    '''if_stmt : IF LPAREN relexpr RPAREN LBRACE stmt_list RBRACE else_part'''
    p[0] = ('if', p[3], p[6], p[8])

def p_else_part(p):
    '''else_part : ELSE LBRACE stmt_list RBRACE
                 | empty'''
    if len(p) == 5:
        p[0] = p[3]
    else:
        p[0] = []

def p_relexpr(p):
    '''relexpr : expr EQ expr
               | expr NE expr
               | expr LT expr
               | expr LE expr
               | expr GT expr
               | expr GE expr'''
    p[0] = ('relexpr', p[2], p[1], p[3])

def p_expr(p):
    '''expr : expr PLUS term
            | expr MINUS term
            | term'''
    if len(p) == 4:
        p[0] = ('binop', p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | term POWER factor
            | factor'''
    if len(p) == 4:
        p[0] = ('binop', p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : LPAREN expr RPAREN
              | ID
              | NUM
              | FLOAT'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()
