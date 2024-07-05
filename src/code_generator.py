# code_generator.py

class CodeGenerator:
    def __init__(self):
        self.temp_count = 0
        self.label_count = 0
        self.code = []
        self.labels = {}

    def new_temp(self):
        self.temp_count += 1
        return f'T{self.temp_count}'

    def new_label(self):
        self.label_count += 1
        return f'L{self.label_count}'

    def generate_code(self, node):
        if isinstance(node, tuple):
            node_type = node[0]
        else:
            node_type = node

        if node_type == 'program':
            _, decls, stmts = node
            for decl in decls:
                self.generate_code(decl)
            for stmt in stmts:
                self.generate_code(stmt)
        elif node_type == 'decl':
            pass  # Declarations are not needed in three-address code
        elif node_type == 'assign':
            _, var, expr = node
            temp = self.generate_code(expr)
            self.code.append(f'{var} = {temp}')
        elif node_type == 'while':
            _, cond, stmts = node
            start_label = self.new_label()
            end_label = self.new_label()
            self.code.append(f'{start_label}:')
            cond_temp = self.generate_code(cond)
            self.code.append(f'IF {cond_temp} GOTO {end_label}')
            for stmt in stmts:
                self.generate_code(stmt)
            self.code.append(f'GOTO {start_label}')
            self.code.append(f'{end_label}:')
        elif node_type == 'if':
            _, cond, then_stmts, else_stmts = node
            else_label = self.new_label()
            end_label = self.new_label()
            cond_temp = self.generate_code(cond)
            self.code.append(f'IF {cond_temp} GOTO {else_label}')
            for stmt in then_stmts:
                self.generate_code(stmt)
            self.code.append(f'GOTO {end_label}')
            self.code.append(f'{else_label}:')
            for stmt in else_stmts:
                self.generate_code(stmt)
            self.code.append(f'{end_label}:')
        elif node_type == 'relexpr':
            _, op, left, right = node
            left_temp = self.generate_code(left)
            right_temp = self.generate_code(right)
            temp = self.new_temp()
            self.code.append(f'{temp} = {left_temp} {op} {right_temp}')
            return temp
        elif node_type == 'binop':
            _, op, left, right = node
            left_temp = self.generate_code(left)
            right_temp = self.generate_code(right)
            temp = self.new_temp()
            self.code.append(f'{temp} = {left_temp} {op} {right_temp}')
            return temp
        elif node_type == 'ID':
            return node[1]
        elif node_type in ('NUM', 'FLOAT'):
            return str(node[1])
        elif node_type == 'empty':
            return ''

    def print_code(self):
        for line in self.code:
            print(line)

def generate_code(ast):
    generator = CodeGenerator()
    generator.generate_code(ast)
    generator.print_code()
