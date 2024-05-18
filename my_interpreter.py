# Program: Assignment*
# Assignment: Identifier = Exp;
# Exp: Exp + Term | Exp - Term | Term 
# Term: Term * Fact | Fact
# Fact: (Exp) | - Fact | + Fact | Literal | Identifier
# Identifier: Letter [Letter | Digit]*
# Letter: a|...|z|A|...|Z|_
# Literal: 0 | NonZeroDigit Digit*
# NonZeroDigit: 1|...|9
# Digit: 0|1|...|9
import re
import sys

symbol_table = {}
def get_assignments(program):
    assignments = re.findall(r'.*?;', program)
    return assignments

def tokenize(code):
    tokens = re.findall(r'\b\w+\b|[^\s\w]', code)
    return tokens

def parse(tokens):
    
    def expect(syntax):
        if(re.match(syntax, tokens[0])):
            return tokens[0]
        else:
            raise SyntaxError("Expected valid tokens")
            
            
    def parse_identifier():
        identifier = expect("[a-zA-Z_][a-zA-Z0-9_]*")
        return identifier
    
    
    def is_literal():
        if (tokens is None):
            return False
        literal_regex = r'0|[1-9][0-9]*'
        return bool(re.fullmatch(literal_regex, tokens[0]))
    
    
    def parse_literal():
        if(is_literal()):
            return tokens[0]
        else:
            raise SyntaxError("Syntax Error")
            
            
    def parse_factor():
        if not tokens:
            raise SyntaxError("SyntaxError")
        if(tokens[0]=='('):
            tokens.pop(0)
            exp = parse_expression()
            if(tokens[0]!=')'):
                raise SyntaxError("Syntax Error")
            tokens.pop(0)
            return exp
        elif(tokens[0]=='-'):
            tokens.pop(0)
            exp = int(parse_factor())
            return -exp
        elif(tokens[0]=='+'):
            tokens.pop(0)
            exp = parse_factor()
            return exp
        elif(is_literal()):
            exp = parse_literal()
            tokens.pop(0)
            return int(exp)
        else:
            exp = parse_identifier()
            if exp in symbol_table:
                tokens.pop(0)
                return symbol_table[exp]
            else:
                raise SyntaxError("Variable not Initialized")
            
    def parse_term():
        F = parse_factor()
        while (tokens[0]=='*'):
            tokens.pop(0)
            T = parse_factor()
            F = T * F
        
        return F
        
    def parse_expression():
        T = parse_term()
        while tokens[0] in "+-":
            if(tokens[0]=='+'):
                tokens.pop(0)
                exp = parse_term()
                T = T + exp
            elif (tokens[0]=='-'):
                tokens.pop(0)
                exp = parse_term()
                T = T - exp
           
        return T
            
            
    #Assignment: id = exp
    def match_assignment():
        identifier = parse_identifier()
        tokens.pop(0)
        if(tokens[0] != '='):
            raise SyntaxError("Syntax Error")
        tokens.pop(0)
        value = 0
        if(not tokens or tokens[0]==';'):
            raise SyntaxError("Invalid")
        while tokens[0] != ';':
            value += parse_expression()
        symbol_table[identifier] = value
    match_assignment()


def readinput(filename):
  try:
    parts = filename.split('.')
    if len(parts) != 2 or parts[1] != "my":
      raise RuntimeError("Error: Only accept *.my files")
    with open(filename, "r") as file:
      content = file.read()
      return content
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except RuntimeError as e:
    print(e)
  return None

# Example usage
if len(sys.argv) != 2:
    print("Expectiing a single argument: filename")
    exit(0)
filename = sys.argv[1]
file_content = readinput(filename)

if file_content:
  code = file_content
  assignment_list = get_assignments(code)
  if not assignment_list or code[-1]!=';':
      print("error")
  else:
      try:
          for assignment in assignment_list:
              tokens = tokenize(assignment)
              parse(tokens)
          for key,val in symbol_table.items():
              print(key,"=",val)
      except SyntaxError:
          print("error")
else:
  print("Please check your source file.")