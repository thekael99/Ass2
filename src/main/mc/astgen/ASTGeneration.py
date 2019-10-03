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
        return [FuncDecl(name,param,returnType,body)]    
      
    def visitArgList(self, ctx: MCParser.ArgListContext):
        return reduce(lambda x, y: x + self.visit(y), ctx.arg(), [])

    def visitArg(self, ctx: MCParser.ArgContext):
        priType = self.visit(ctx.priType())
        name = Id(ctx.ID().getText())
        if ctx.LSB():
            return [VarDecl(name, ArrayPointerType(priType))]
        else:
            return [VarDecl(name, priType)]

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
        return self.visitChildren(ctx)

    def visitPrimaryExpress(self, ctx: MCParser.PrimaryExpressContext):
        return self.visitChildren(ctx)

    def visitPostExpress(self, ctx: MCParser.PostExpressContext):
        return self.visitChildren(ctx)

    def visitInvocationExpress(self, ctx: MCParser.InvocationExpressContext):
        return self.visitChildren(ctx)

    def visitUnaryExpress(self, ctx: MCParser.UnaryExpressContext):
        return self.visitChildren(ctx)

    def visitMultiplicativeExpress(self, ctx: MCParser.MultiplicativeExpressContext):
        return self.visitChildren(ctx)

    def visitAdditiveExpress(self, ctx: MCParser.AdditiveExpressContext):
        return self.visitChildren(ctx)

    def visitRelaExpress(self, ctx: MCParser.RelaExpressContext):
        return self.visitChildren(ctx)

    def visitEqualExpress(self, ctx: MCParser.EqualExpressContext):
        return self.visitChildren(ctx)

    def visitLogicalAndExpress(self, ctx: MCParser.LogicalAndExpressContext):
        return self.visitChildren(ctx)

    def visitLogicalOrExpress(self, ctx: MCParser.LogicalOrExpressContext):
        return self.visitChildren(ctx)

    def visitAssigExpress(self, ctx: MCParser.AssigExpressContext):
        return self.visitChildren(ctx)

    def visitExpress(self, ctx: MCParser.ExpressContext):
        return self.visitChildren(ctx)

    def visitSimpleStament(self, ctx: MCParser.SimpleStamentContext):
        return self.visitChildren(ctx)

    def visitStructStamen(self, ctx: MCParser.StructStamenContext):
        return self.visitChildren(ctx)

    def visitStament(self, ctx: MCParser.StamentContext):
        return self.visitChildren(ctx)

    def visitBlockStament(self, ctx: MCParser.BlockStamentContext):
        return Block([])

    def visitIfStament(self, ctx: MCParser.IfStamentContext):
        return self.visitChildren(ctx)

    def visitDoWhileStament(self, ctx: MCParser.DoWhileStamentContext):
        return self.visitChildren(ctx)

    def visitForStament(self, ctx: MCParser.ForStamentContext):
        return self.visitChildren(ctx)

    def visitBreakStament(self, ctx: MCParser.BreakStamentContext):
        return self.visitChildren(ctx)

    def visitContinueStament(self, ctx: MCParser.ContinueStamentContext):
        return self.visitChildren(ctx)

    def visitReturnStament(self, ctx: MCParser.ReturnStamentContext):
        return self.visitChildren(ctx)

    def visitReturnNone(self, ctx: MCParser.ReturnNoneContext):
        return self.visitChildren(ctx)

    def visitReturnValue(self, ctx: MCParser.ReturnValueContext):
        return self.visitChildren(ctx)

    def visitExpressStament(self, ctx: MCParser.ExpressStamentContext):
        return self.visitChildren(ctx)
