//1713215
grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options {
	language = Python3;
}

/*
 -------PARSER-------
 */

//Program
program: decl+ EOF;
decl: varDec | funcDec;

//Declara
// Variable
varDec: priType idList SEMI;

idList: idVar (CM idVar)*;

idVar: ID (LSB INTLIT RSB)?;

//Function
funcDec: funcType ID LB argList? RB blockStament;

argList: arg (CM arg)*;

arg: priType ID (LSB RSB)?;

//Type return
funcType: priType (LSB RSB)? | VOIDTYPE;

priType: BOOLEANTYPE | INTTYPE | FLOATTYPE | STRINGTYPE;

//Express
literal: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT;
primaryExpress
    : ID
	| literal
	| LB express RB
	| invocationExpress;

postExpress: primaryExpress (LSB express RSB)?;

invocationExpress: ID LB (express? | express (CM express)+) RB;

unaryExpress: postExpress | (SUB | NOT) unaryExpress;

multiplicativeExpress:
	unaryExpress
	| multiplicativeExpress (DIV | MUL | MOD) unaryExpress;

additiveExpress:
	multiplicativeExpress
	| additiveExpress (ADD | SUB) multiplicativeExpress;

relaExpress:
	additiveExpress
	| additiveExpress (LT | LE | GT | GE) additiveExpress;

equalExpress:
	relaExpress
	| relaExpress (EQUAL | NOTEQUAL) relaExpress;

logicalAndExpress:
	equalExpress
	| logicalAndExpress AND equalExpress;

logicalOrExpress:
	logicalAndExpress
	| logicalOrExpress OR logicalAndExpress;

assignExpress:
	logicalOrExpress
	| postExpress ASSIGN assignExpress;

express: assignExpress;

//Stament
simpleStament:
	blockStament
	| expressStament
	| breakStament
	| continueStament
	| returnStament;

structStamen: ifStament | doWhileStament | forStament;

stament: simpleStament | structStamen;

blockStament: LP bodyBlock* RP;
bodyBlock: stament | varDec;

ifStament: IF LB express RB stament (ELSE stament)?;

doWhileStament: DO stament+ WHILE express SEMI;

forStament: FOR LB express SEMI express SEMI express RB stament;

breakStament: BREAK SEMI;

continueStament: CONTINUE SEMI;

returnStament: returnNone | returnValue;
returnNone: RETURN SEMI;
returnValue: RETURN express SEMI;

expressStament: express SEMI;

/*
 -------LEXER-------
 */

//Whitespace and comments
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
LINECMT: '//' (~[\r\n])* -> skip;
BLOCKCMT: ('/*' .*? '*/') -> skip;

///Literals

//integer
INTLIT: [0-9]+;

//float
FLOATLIT: (INTLIT '.' | '.' INTLIT | INTLIT '.' INTLIT) (
		[Ee] SUB? INTLIT
	)?
	| INTLIT ([Ee] SUB? INTLIT);

//boolean
BOOLLIT: TRUE | FALSE;

//string
UNCLOSE_STRING:
	'"' Character* (EOF | [\r\n]) {self.text = self.text[1:].rstrip("\n\r")};

ILLEGAL_ESCAPE:
	'"' Character* ('\\' ~[btnfr"'\\]) {self.text = self.text[1:]};

STRINGLIT: '"' Character* '"' {self.text = self.text[1:-1]};
fragment Character: ~["\\\r\n\b\f\t] | '\\' [btnfr"'\\];

//Keyword
BREAK: 'break';
CONTINUE: 'continue';
ELSE: 'else';
FOR: 'for';
IF: 'if';
RETURN: 'return';
DO: 'do';
WHILE: 'while';
TRUE: 'true';
FALSE: 'false';
BOOLEANTYPE: 'boolean';
STRINGTYPE: 'string';
INTTYPE: 'int';
FLOATTYPE: 'float';
VOIDTYPE: 'void';

//Identifer
ID: [a-zA-Z_] [0-9a-zA-Z_]*;

//Operator
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
NOT: '!';
MOD: '%';
OR: '||';
AND: '&&';
NOTEQUAL: '!=';
EQUAL: '==';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
ASSIGN: '=';

//Separator
LB: '(';
RB: ')';
LP: '{';
RP: '}';
LSB: '[';
RSB: ']';
SEMI: ';';
CM: ',';

//Error character
ERROR_CHAR: .;