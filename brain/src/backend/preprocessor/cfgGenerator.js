define([
    './cfgGenerator/LogicalAnd',
    './cfgGenerator/LogicalOr',
    './cfgGenerator/BitwiseAnd',
    './cfgGenerator/BitwiseOr',
    './cfgGenerator/BitwiseNot',
    './cfgGenerator/BitwiseLeftShift',
    './cfgGenerator/BitwiseRightShift',
    './cfgGenerator/Mod',
    './cfgGenerator/Mul',
    './cfgGenerator/Div',
    './cfgGenerator/Return',
    './cfgGenerator/CompoundStatement',
    './cfgGenerator/ExpressionStatement',
    './cfgGenerator/Add',
    './cfgGenerator/Sub',
    './cfgGenerator/Identifier',
    './cfgGenerator/Deref',
    './cfgGenerator/Ref',
    './cfgGenerator/Malloc',
    './cfgGenerator/Assign',
    './cfgGenerator/PlusAssign',
    './cfgGenerator/MinusAssign',
    './cfgGenerator/FunctionCall',
    './cfgGenerator/If',
    './cfgGenerator/While',
    './cfgGenerator/For',
    './cfgGenerator/Break',
    './cfgGenerator/Continue',
    './cfgGenerator/Less',
    './cfgGenerator/Eq',
    './cfgGenerator/Neq',
    './cfgGenerator/Leq',
    './cfgGenerator/Geq',
    './cfgGenerator/More',
    './cfgGenerator/Not',
    './cfgGenerator/Subscript'
], function (LogicalAnd, LogicalOr, BitwiseAnd, BitwiseOr, BitwiseNot, BitwiseLeftShift, BitwiseRightShift, Mod, Mul, Div, Return, CompoundStatement, ExpressionStatement, Add, Sub, Identifier, Deref, Ref, Malloc, Assign, PlusAssign, MinusAssign, FunctionCall, If, While, For, Break, Continue, Less, Eq, Neq, Leq, Geq, More, Not, Subscript) {

    function generateCfg(node) {
	var generators = {
	    'LOGICAL_AND': LogicalAnd,
	    'LOGICAL_OR': LogicalOr,
	    'AND': BitwiseAnd,
	    'OR': BitwiseOr,
	    'UNARYOP_~': BitwiseNot,
	    'LEFT': BitwiseLeftShift,
	    'RIGHT': BitwiseRightShift,
	    'MOD': Mod,
	    'MUL': Mul,
	    'DIV': Div,
	    'return': Return,
	    'compound_statement': CompoundStatement,
	    'expression_statement': ExpressionStatement,
	    'ADD': Add,
	    'SUB': Sub,
	    'INDENTIFIER': Identifier,
	    'UNARYOP_*' : Deref,
	    'UNARYOP_&' : Ref,
	    'MALLOC' : Malloc,
	    'ASSIGN': Assign,
	    '+=': PlusAssign,
	    '-=': MinusAssign,
	    'FUNCTION_CALL': FunctionCall,
	    'if': If,
	    'while': While,
	    'for': For,
	    'break': Break,
	    'continue': Continue,
	    'LESS': Less,
	    'EQ': Eq,
	    'NE': Neq,
	    'LESS_EQUAL': Leq,
	    'GEQ': Geq,
	    'GREATER': More,
	    'UNARYOP_!': Not,
	    'SUBSCRIPT': Subscript
	};

	var generator = generators[node.type];
	if (!generator) {
	    throw new Error("generateCfg: no function for " + JSON.stringify(node.type, null, 2));
	}
	return generator(generateCfg)(node);
    }

    return generateCfg;

});
