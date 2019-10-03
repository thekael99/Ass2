from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
import functools

class ASTGeneration(MPVisitor):
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.decl()])

    def visitDecl(self,ctx:MPParser.DeclContext):
    #decl: var_dec | fun_dec | procedure_dec 
        result = self.visitChildren(ctx)
        if ctx.var_dec():
            for i in range(1,len(result)):
                result[0] = str(result[0]) + "," + str(result[i])
            return result[0]
        else: 
            return result

    def visitVar_dec(self, ctx:MPParser.Var_decContext):
    # VAR varlist_dec
        return  self.visit(ctx.varlist_dec())
#       if ctx.getParent() == ctx.decl():
 #           for i in range(1,len(result)):
 #               result[0] = str(result[0]) + "," + str(result[i])
 #           return result[0]
 #       else:
  #          return result
    def visitVarlist_dec(self, ctx:MPParser.Varlist_decContext):       
    # varlist_dec: one_var_dec varlist_dec | one_var_dec ; 
        #print("Varlist_dec")
        if ctx.varlist_dec():
            return self.visit(ctx.one_var_dec()) + self.visit(ctx.varlist_dec()) 
        else:
            return self.visit(ctx.one_var_dec())

    def visitOne_var_dec(self,ctx:MPParser.One_var_decContext):
    #one_var_dec:  idlist COLON types  SEMI 
       # print("One_var_dec")
        id_l = self.visit(ctx.idlist())
        types = self.visit(ctx.types())
        return [VarDecl(Id(x),types) for x in id_l]
#        for i in range(1,len(result)):
#            result[0] = str(result[0]) + "," + str(result[i])
        
    
    def visitIdlist(self,ctx:MPParser.IdlistContext):
    #idlist: ID COMMA idlist | ID;
        result = []
        while(ctx.getChildCount() != 1): 
            result.append(ctx.ID().getText())
            ctx = ctx.idlist()
        result.append(ctx.ID().getText())
        return result

    def visitFun_dec(self, ctx:MPParser.Fun_decContext):
    #  fun_dec: FUNCTION ID LB paralist RB COLON types SEMI (var_dec)? compoundStatement
        para = self.visit(ctx.paralist())
        cpstmt = self.visit(ctx.compoundStatement())


        if ctx.var_dec(): 
            local = self.visit(ctx.var_dec())
        else:
            local = []

        return FuncDecl(Id(ctx.ID().getText()),
                        para,
                        local,
                        cpstmt,
                        self.visit(ctx.types()))

    def visitProcedure_dec(self, ctx:MPParser.Procedure_decContext):
    #procedure_dec: PROCEDURE ID LB paralist RB SEMI var_dec? compoundStatement ;
        para = self.visit(ctx.paralist())
        if ctx.var_dec(): 
            local = self.visit(ctx.var_dec())
        else:
            local = []
        cpstmt = self.visit(ctx.compoundStatement())
        return FuncDecl(Id(ctx.ID().getText()),
                        para,
                        local,
                        cpstmt)
    def visitParalist(self, ctx:MPParser.ParalistContext):
    #paralist: para_dec SEMI paralist | (para_dec)? 

        if ctx.paralist():
            return self.visit(ctx.para_dec()) + self.visit(ctx.paralist()) 
        elif ctx.para_dec():
            return self.visit(ctx.para_dec())
        else:
            return []

    def visitPara_dec(self, ctx:MPParser.Para_decContext):
    #para_dec: idlist COLON types
        id_l = self.visit(ctx.idlist())
        types = self.visit(ctx.types())
        return [VarDecl(Id(x),types) for x in id_l]


    def visitTypes(self, ctx:MPParser.TypesContext):
    #types: primitive_types| compound_type 
        return self.visitChildren(ctx)

    def visitLiterals(self, ctx:MPParser.LiteralsContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():           
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOL_LIT():
            if str(ctx.BOOL_LIT().getText())[0] == "T" or str(ctx.BOOL_LIT().getText())[0] == "t":
                return BooleanLiteral(True)
            else:
                return BooleanLiteral(False)
        else: 
            return StringLiteral(ctx.STRING_LIT().getText())

    def visitPrimitive_types(self, ctx:MPParser.Primitive_typesContext):
    #primitive_types: ( BOOLEAN | INTEGER | REAL | STRING )
        if ctx.BOOLEAN():
            return BoolType()
        elif ctx.INTEGER():
            return IntType()
        elif ctx.REAL():
            return FloatType()
        else:
            return StringType()

    def visitCompound_type(self, ctx:MPParser.Compound_typeContext):    
    #compound_type: array_dec
        return self.visitChildren(ctx)

    def visitArray_dec(self, ctx:MPParser.Array_decContext):
    #array_dec: ARRAY LSB SUB? INTLIT DD2 SUB? INTLIT RSB OF primitive_types 
        lower = int(ctx.INTLIT(0).getText())
        uper = int(ctx.INTLIT(1).getText())
        types = self.visit(ctx.primitive_types())

        if ctx.SUB(0):
            lower = "-" + str(lower) 
        if ctx.SUB(1):
            uper = "-" + str(uper)

        return ArrayType(lower,uper,types)
 
    """operand
    : literals
    | ID
    | funcall
    ;"""
    def visitOperand(self, ctx:MPParser.OperandContext):
        #print("operand")
        if  ctx.getChild(0) == ctx.literals():
            return self.visit(ctx.literals())
        elif ctx.getChild(0) == ctx.ID():
            return Id(ctx.ID().getText())
        else: 
            return self.visit(ctx.funcall())

    """expression:
    expression ANDTHEN expression1
    | expression ORELSE expression1
    | expression1
    | operand
    ;"""
    def visitExpression(self, ctx:MPParser.ExpressionContext):
        #print("expr")
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        elif ctx.getChild(1) == ctx.ANDTHEN():
            andthen = "andthen"
            return BinaryOp(andthen,self.visit(ctx.expression()),self.visit(ctx.expression1()))
        else: 
            orelse = "orelse" 
            return BinaryOp(orelse,self.visit(ctx.expression()),self.visit(ctx.expression1()))

    """expression1:
    expression2 EQUAL expression2
    | expression2 NOT_EQUAL expression2
    | expression2 LESS_THAN expression2
    | expression2 GREATER_THAN expression2
    | expression2 LESS_THAN_EQUAL expression2
    | expression2 GREATER_THAN_EQUAL expression2
    | expression2
    ;"""
    def visitExpression1(self, ctx:MPParser.Expression1Context):
        #print("expr1")
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.expression2(0)),self.visit(ctx.expression2(1)))

    """expression2:
    expression2 ADD expression3
    | expression2 SUB expression3
    | expression2 OR expression3
    | expression3
    ;"""
    def visitExpression2(self, ctx:MPParser.Expression2Context):
        #print("expr2")
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.expression2()),self.visit(ctx.expression3()))

    """expression3:
    expression3 DIVISION expression4
    | expression3 MULTIPLICATION expression4
    | expression3 DIV expression4
    | expression3 MOD expression4
    | expression3 AND expression4
    | expression4
    ;"""
    def visitExpression3(self, ctx:MPParser.Expression3Context):
        #print("expr3")
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.expression3()),self.visit(ctx.expression4()))

    """expression4:
    SUB expression4
    | NOT expression4
    | expression5
    ;"""
    def visitExpression4(self, ctx:MPParser.Expression4Context):
        #print("expr4")
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.expression4()))        

    """expression5:
    expression5 LSB expression RSB
    | expression6
    ;"""
    def visitExpression5(self, ctx:MPParser.Expression5Context):
        #print("expr5")
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else: 
            return ArrayCell(self.visit(ctx.expression5()),self.visit(ctx.expression()))        

    """expression6:
    LB expression RB
    | operand
    ;"""
    def visitExpression6(self, ctx:MPParser.Expression6Context):
        #print("expr6")
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            return self.visit(ctx.expression())

    """arrayelement:
    expression5 LSB expression RSB
    ;"""
    def visitArrayelement(self, ctx:MPParser.ArrayelementContext):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else: 
            return ArrayCell(self.visit(ctx.expression5()),self.visit(ctx.expression()))  

    def visitFuncall(self, ctx:MPParser.FuncallContext):
    #funcall: ID LB listexp? RB 
        if ctx.listexp():
            return CallExpr(Id(ctx.ID().getText()),self.visit(ctx.listexp()))
        else:
            return CallExpr(Id(ctx.ID().getText()),[])

    def visitListexp(self, ctx:MPParser.ListexpContext):
    #listexp: expression COMMA listexp | expression
     #list store exp (listexp)
        if ctx.listexp():
            return [self.visit(ctx.expression())] + self.visit(ctx.listexp())
        else:
            return [self.visit(ctx.expression())]

    def visitCompoundStatement(self, ctx:MPParser.CompoundStatementContext):
    #compoundStatement: BEGIN (lis_statements)? END 
        if ctx.lis_statements():
            return self.visit(ctx.lis_statements())
        else: 
            return []

    
    """ statements
    : assignstatement
    | ifstatement
    | whilestatement
    | forstatement
    | breakstatement
    | continuestatement
    | returnstatement
    | compoundStatement
    | withstatements
    | callstatements
    ;"""
    def visitStatements(self, ctx:MPParser.StatementsContext):     
        if ctx.assignstatement():
            result = self.visitChildren(ctx)   
            for i in range(1,len(result)):
                result[0] = str(result[0]) + "," + str(result[i]) 
            return result[0] 
        else:
            return self.visitChildren(ctx)   

    def visitAssignstatement(self, ctx:MPParser.AssignstatementContext):
    #assignstatement: (variable ASSIGN)+ expression SEMI 
        exp = self.visit(ctx.expression())
        lisvar = ctx.variable()[::-1] #reserve list
        lisvarnext = lisvar[1:]
        result = [Assign(self.visit(lisvar[0]),exp)] + [Assign(self.visit(y),self.visit(x)) for x,y in zip(lisvar,lisvarnext)]
#         for i in range(1,len(result)):
#           result[0] = str(result[0]) + "," + str(result[i]) 
        return [str(x) for x in result]


    def visitVariable(self, ctx:MPParser.VariableContext):
    #variable: ID | arrayelement
        if ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visitChildren(ctx)

    def visitIfstatement(self, ctx:MPParser.IfstatementContext):
    #ifstatement: IF expression THEN statements ( ELSE statements)? ;
        thenstmt = self.visit(ctx.statements(0))
        if not isinstance(thenstmt,list):
            thenstmt = [thenstmt]
        if ctx.statements(1):
            elsestmt = self.visit(ctx.statements(1))
            if not isinstance(elsestmt,list):
                elsestmt = [elsestmt]
            return If(self.visit(ctx.expression()),thenstmt,elsestmt)
        return If(self.visit(ctx.expression()),thenstmt)

    def visitWhilestatement(self, ctx:MPParser.WhilestatementContext):
    #whilestatement: WHILE expression DO  statements 
        result = self.visit(ctx.statements())
        if result: 
            if not isinstance(result,list):
                return While(self.visit(ctx.expression()),[result])
        return While(self.visit(ctx.expression()),result)
    def visitForstatement(self, ctx:MPParser.ForstatementContext):
    #forstatement: FOR ID ASSIGN initialExp (TO | DOWNTO) finalExp DO statements 
        result = self.visit(ctx.statements())
        if ctx.TO():
            up = True
        else:
            up = False
        if result: 
            if not isinstance(result,list):
                return For(Id(ctx.ID().getText()),self.visit(ctx.initialExp()),self.visit(ctx.finalExp()),up,[result])    
        return For(Id(ctx.ID().getText()),self.visit(ctx.initialExp()),self.visit(ctx.finalExp()),up,result)     

    def visitInitialExp(self, ctx:MPParser.InitialExpContext):
    #initialExp: expression
        return self.visitChildren(ctx)

    def visitFinalExp(self, ctx:MPParser.FinalExpContext):
        return self.visitChildren(ctx)

    def visitBreakstatement(self, ctx:MPParser.BreakstatementContext):
    #breakstatement: BREAK SEMI 
        return Break()

    def visitContinuestatement(self, ctx:MPParser.ContinuestatementContext):
    #continuestatement: CONTINUE SEMI 
        return Continue()

    def visitReturnstatement(self, ctx:MPParser.ReturnstatementContext):
    #returnstatement: RETURN expression? SEMI 
        if ctx.expression():
            return Return(self.visit(ctx.expression()))
        else: 
            return Return()
        
    def visitLis_statements(self, ctx:MPParser.Lis_statementsContext):
    #lis_statements: statements lis_statements | statements ;
    #lis_stmt
        if ctx.lis_statements():
            return [self.visit(ctx.statements())] + self.visit(ctx.lis_statements())
        else:
            return [self.visit(ctx.statements())]

    def visitWithstatements(self, ctx:MPParser.WithstatementsContext):
    #withstatements: WITH varlist_dec DO statements
        result = self.visit(ctx.varlist_dec())
        stmt = self.visit(ctx.statements())
        if not isinstance(stmt,list): 
            stmt = [stmt]
        stmt = [str(x) for x in stmt]
        return With(result,stmt)
 

    def visitCallstatements(self, ctx:MPParser.CallstatementsContext):
    #callstatements: funcall SEMI 
        ctx = ctx.funcall()
        if ctx.listexp():
            return CallStmt(Id(ctx.ID().getText()),self.visit(ctx.listexp()))
        else:
            return CallStmt(Id(ctx.ID().getText()),[])