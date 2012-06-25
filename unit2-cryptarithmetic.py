from __future__ import division
import re,string,itertools,RunningTime,time
import cProfile

timed_call = RunningTime.timed_calls
timed_run = RunningTime.timed_run

def compile_word(word):
    """Compile an uppercase word as Numerical digits.
        for eg: YOU => '(U*1 + O*10 + U*100)'
        Non-Uppercase letters are left the same way
        for eg: '+' => '+'"""
    if word.isupper():
        expr = ["%s*%s"%(10**i,d)
                for i,d in enumerate(word[::-1])]
        return '('+' + '.join(expr)+')'
    else:
        return word

def valid(f):
    "Returns True if the formula has no leading zero and eval is True"
    try:
        return not re.search(r'\b0[0-9]',f) and eval(f) == True
    except ArithmeticError:
        return False
        
def fill_in(formula):
    "Generates all the possible filling-in of letters in formula with digits"
    letters = "".join(set(re.findall(r'[A-Z]',formula)))
    digits = itertools.permutations('1234567890',len(letters))
    for digit in digits:
        table = string.maketrans(letters,"".join(digit))
        yield formula.translate(table)

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN',fill in the digits to solve it.
    Input formula is a string;Outputs digits fill-in place of strings or None
    """
    for f in fill_in(formula):
        if valid(f):
            return f
            
#print timed_call(10,solve,'ODD+DOD==EVEN')
#next(fill_in('ODD+DOD==EVEN'))

def faster_solve(formula):
    """Given a formula like 'ODD + ODD == EVEN',fill in the digits to solve it.
    input formula is a string;output digits fill-in place of strings or None
    This revision calls only one eval per formula"""
    f,letters = compile_formula(formula,True)
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0),len(letters)):
        try:
            if f(*digits) == True:
                table = string.maketrans(letters,''.join(map(str,digits)))
                return formula.translate(table)
        except ArithmeticError:
            pass        
    
    
def compile_formula(formula,verbose = False):
    letters = ''.join(set(re.findall('[A-Z]',formula)))
    parms = ','.join(letters)
    tokens = map(compile_word,re.split('([A-Z]+)',formula))    
    body = ''.join(tokens)
    f = 'lambda %s: %s'%(parms,body)
    if verbose:
        print f
    return eval(f),letters

examples = """TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == BY**2
X / X == X
A**N + B**N == C**N and N>1
ATOM**0.5 == A + TO + M
GLITTERS is not GOLD
ONE < TWO and FOUR < FIVE
ONE < TWO < THREE
RAMN == R**3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN
PLUTO is not set([PLANETS])""".splitlines()

def test(method):
    start = time.time()
    for example in examples:
        print;print 13*" ",example
        print '%6.4f sec:   %s'%(timed_run(method,example))
    print 'Total time = ',time.time() - start

cProfile.run('test(solve)')
cProfile.run('test(faster_solve)')
