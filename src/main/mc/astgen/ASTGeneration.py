from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
from functools import reduce


class ASTGeneration(MCVisitor):
    def visitProgram(self, ctx: MCParser.ProgramContext):
        result = reduce(lambda x, y: x + self.visit(y), ctx.decl(), [])
        return Program(result)

    def visitDecl(self, ctx: MCParser.DeclContext):
        if ctx.varDec():
            return self.visit(ctx.varDec())
        else:
            return self.visit(ctx.funcDec())

    def visitVarDec(self, ctx: MCParser.VarDecContext):
        typeVar = self.visit(ctx.priType())
        idList = self.visit(ctx.idList())
        return [VarDecl(x[0], typeVar) if x[1] is None else VarDecl(x[0], ArrayType(x[1], typeVar)) for x in idList]

    def visitIdList(self, ctx: MCParser.IdListContext):
        return reduce(lambda x, y: x + [self.visit(y)], ctx.idVar(), [])

    def visitIdVar(self, ctx: MCParser.IdVarContext):
        if ctx.INTLIT():
            return [Id(ctx.ID().getText()), int(ctx.INTLIT().getText())]
        else:
            return [Id(ctx.ID().getText()), None]

    def visitFuncDec(self, ctx: MCParser.FuncDecContext):
        returnType = self.visit(ctx.funcType())
        name = Id(ctx.ID().getText())
        if ctx.argList():
            param = self.visit(ctx.argList())
        else:
            param = []
        body = self.visit(ctx.blockStament())
        return [FuncDecl(name, param, returnType, body)]

    def visitArgList(self, ctx: MCParser.ArgListContext):
        return reduce(lambda x, y: x + [self.visit(y)], ctx.arg(), [])

    def visitArg(self, ctx: MCParser.ArgContext):
        priType = self.visit(ctx.priType())
        name = Id(ctx.ID().getText())
        if ctx.LSB():
            return VarDecl(name, ArrayPointerType(priType))
        else:
            return VarDecl(name, priType)

    def visitFuncType(self, ctx: MCParser.FuncTypeContext):
        if ctx.VOIDTYPE():
            return VoidType()
        elif ctx.LSB():
            return ArrayPointerType(self.visit(ctx.priType()))
        else:
            return self.visit(ctx.priType())

    def visitPriType(self, ctx: MCParser.PriTypeContext):
        if ctx.INTTYPE():
            return IntType()
        elif ctx.BOOLEANTYPE():
            return BoolType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.STRINGTYPE():
            return StringType()

    def visitLiteral(self, ctx: MCParser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLLIT():
            if ctx.BOOLLIT().getText() == "true":
                return BooleanLiteral(True)
            else:
                return BooleanLiteral(False)
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())

    def visitPrimaryExpress(self, ctx: MCParser.PrimaryExpressContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.RB():
            return self.visit(ctx.express())
        else:
            return self.visit(ctx.invocationExpress())

    def visitPostExpress(self, ctx: MCParser.PostExpressContext):
        priExp = self.visit(ctx.primaryExpress())
        if ctx.LSB():
            index = self.visit(ctx.express())
            return ArrayCell(priExp, index)
        return priExp

    def visitInvocationExpress(self, ctx: MCParser.InvocationExpressContext):
        method = Id(ctx.ID().getText())
        param = reduce(lambda x, y: x+[self.visit(y)], ctx.express(), [])
        return CallExpr(method, param)

    def visitUnaryExpress(self, ctx: MCParser.UnaryExpressContext):
        if ctx.SUB():
            return UnaryOp('-', self.visit(ctx.unaryExpress()))
        elif ctx.NOT():
            return UnaryOp('!', self.visit(ctx.unaryExpress()))
        else:
            return self.visit(ctx.postExpress())

    def visitMultiplicativeExpress(self, ctx: MCParser.MultiplicativeExpressContext):
        if ctx.DIV():
            return BinaryOp('/', self.visit(ctx.multiplicativeExpress()), self.visit(ctx.unaryExpress()))
        elif ctx.MUL():
            return BinaryOp('*', self.visit(ctx.multiplicativeExpress()), self.visit(ctx.unaryExpress()))
        elif ctx.MOD():
            return BinaryOp('%', self.visit(ctx.multiplicativeExpress()), self.visit(ctx.unaryExpress()))
        else:
            return self.visit(ctx.unaryExpress())

    def visitAdditiveExpress(self, ctx: MCParser.AdditiveExpressContext):
        if ctx.ADD():
            return BinaryOp('+', self.visit(ctx.additiveExpress()), self.visit(ctx.multiplicativeExpress()))
        elif ctx.SUB():
            return BinaryOp('-', self.visit(ctx.additiveExpress()), self.visit(ctx.multiplicativeExpress()))
        else:
            return self.visit(ctx.multiplicativeExpress())

    def visitRelaExpress(self, ctx: MCParser.RelaExpressContext):
        if ctx.LT():
            return BinaryOp('<', self.visit(ctx.additiveExpress()[0]), self.visit(ctx.additiveExpress()[1]))
        elif ctx.LE():
            return BinaryOp('<=', self.visit(ctx.additiveExpress()[0]), self.visit(ctx.additiveExpress()[1]))
        elif ctx.GT():
            return BinaryOp('>', self.visit(ctx.additiveExpress()[0]), self.visit(ctx.additiveExpress()[1]))
        elif ctx.GE():
            return BinaryOp('>=', self.visit(ctx.additiveExpress()[0]), self.visit(ctx.additiveExpress()[1]))
        else:
            return self.visit(ctx.additiveExpress()[0])

    def visitEqualExpress(self, ctx: MCParser.EqualExpressContext):
        if ctx.EQUAL():
            return BinaryOp('==', self.visit(ctx.relaExpress()[0]), self.visit(ctx.relaExpress()[1]))
        elif ctx.NOTEQUAL():
            return BinaryOp('!=', self.visit(ctx.relaExpress()[0]), self.visit(ctx.relaExpress()[1]))
        else:
            return self.visit(ctx.relaExpress()[0])

    def visitLogicalAndExpress(self, ctx: MCParser.LogicalAndExpressContext):
        if ctx.AND():
            return BinaryOp('&&', self.visit(ctx.logicalAndExpress()), self.visit(ctx.equalExpress()))
        else:
            return self.visit(ctx.equalExpress())

    def visitLogicalOrExpress(self, ctx: MCParser.LogicalOrExpressContext):
        if ctx.OR():
            return BinaryOp('||', self.visit(ctx.logicalOrExpress()), self.visit(ctx.logicalAndExpress()))
        else:
            return self.visit(ctx.logicalAndExpress())

    def visitAssignExpress(self, ctx: MCParser.AssignExpressContext):
        if ctx.ASSIGN():
            return BinaryOp('=', self.visit(ctx.postExpress()), self.visit(ctx.assignExpress()))
        else:
            return self.visit(ctx.logicalOrExpress())

    def visitExpress(self, ctx: MCParser.ExpressContext):
        return self.visit(ctx.assignExpress())

    def visitSimpleStament(self, ctx: MCParser.SimpleStamentContext):
        if ctx.blockStament():
            return self.visit(ctx.blockStament())
        elif ctx.expressStament():
            return self.visit(ctx.expressStament())
        elif ctx.breakStament():
            return self.visit(ctx.breakStament())
        elif ctx.continueStament():
            return self.visit(ctx.continueStament())
        else:
            return self.visit(ctx.returnStament())

    def visitStructStamen(self, ctx: MCParser.StructStamenContext):
        if ctx.ifStament():
            return self.visit(ctx.ifStament())
        elif ctx.doWhileStament():
            return self.visit(ctx.doWhileStament())
        else:
            return self.visit(ctx.forStament())

    def visitStament(self, ctx: MCParser.StamentContext):
        if ctx.simpleStament():
            return self.visit(ctx.simpleStament())
        else:
            return self.visit(ctx.structStamen())

    def visitBlockStament(self, ctx: MCParser.BlockStamentContext):
        if ctx.bodyBlock():
            return Block(reduce(lambda x, y: x + self.visit(y), ctx.bodyBlock(), []))
        else:
            return Block([])

    def visitBodyBlock(self, ctx: MCParser.BodyBlockContext):
        if ctx.stament():
            return [self.visit(ctx.stament())]
        else:
            return self.visit(ctx.varDec())

    def visitIfStament(self, ctx: MCParser.IfStamentContext):
        exp = self.visit(ctx.express())
        if ctx.ELSE():
            stm1 = self.visit(ctx.stament()[0])
            stm2 = self.visit(ctx.stament()[1])
            return If(exp, stm1, stm2)
        else:
            stm = self.visit(ctx.stament()[0])
            return If(exp, stm)

    def visitDoWhileStament(self, ctx: MCParser.DoWhileStamentContext):
        listStm = reduce(lambda x, y: x+[self.visit(y)], ctx.stament(), [])
        exp = self.visit(ctx.express())
        return Dowhile(listStm, exp)

    def visitForStament(self, ctx: MCParser.ForStamentContext):
        exp1 = self.visit(ctx.express()[0])
        exp2 = self.visit(ctx.express()[1])
        exp3 = self.visit(ctx.express()[2])
        stm = self.visit(ctx.stament())
        return For(exp1, exp2, exp3, stm)

    def visitBreakStament(self, ctx: MCParser.BreakStamentContext):
        return Break()

    def visitContinueStament(self, ctx: MCParser.ContinueStamentContext):
        return Continue()

    def visitReturnStament(self, ctx: MCParser.ReturnStamentContext):
        if ctx.returnNone():
            return self.visit(ctx.returnNone())
        else:
            return self.visit(ctx.returnValue())

    def visitReturnNone(self, ctx: MCParser.ReturnNoneContext):
        return Return()

    def visitReturnValue(self, ctx: MCParser.ReturnValueContext):
        return Return(self.visit(ctx.express()))

    def visitExpressStament(self, ctx: MCParser.ExpressStamentContext):
        return self.visit(ctx.express())
