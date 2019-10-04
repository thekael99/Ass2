# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#decl.
    def visitDecl(self, ctx:MCParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#varDec.
    def visitVarDec(self, ctx:MCParser.VarDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#idList.
    def visitIdList(self, ctx:MCParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#idVar.
    def visitIdVar(self, ctx:MCParser.IdVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcDec.
    def visitFuncDec(self, ctx:MCParser.FuncDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#argList.
    def visitArgList(self, ctx:MCParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#arg.
    def visitArg(self, ctx:MCParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcType.
    def visitFuncType(self, ctx:MCParser.FuncTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#priType.
    def visitPriType(self, ctx:MCParser.PriTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#literal.
    def visitLiteral(self, ctx:MCParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primaryExpress.
    def visitPrimaryExpress(self, ctx:MCParser.PrimaryExpressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#postExpress.
    def visitPostExpress(self, ctx:MCParser.PostExpressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#invocationExpress.
    def visitInvocationExpress(self, ctx:MCParser.InvocationExpressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#unaryExpress.
    def visitUnaryExpress(self, ctx:MCParser.UnaryExpressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#multiplicativeExpress.
    def visitMultiplicativeExpress(self, ctx:MCParser.MultiplicativeExpressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#additiveExpress.
    def visitAdditiveExpress(self, ctx:MCParser.AdditiveExpressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#relaExpress.
    def visitRelaExpress(self, ctx:MCParser.RelaExpressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#equalExpress.
    def visitEqualExpress(self, ctx:MCParser.EqualExpressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#logicalAndExpress.
    def visitLogicalAndExpress(self, ctx:MCParser.LogicalAndExpressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#logicalOrExpress.
    def visitLogicalOrExpress(self, ctx:MCParser.LogicalOrExpressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#assignExpress.
    def visitAssignExpress(self, ctx:MCParser.AssignExpressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#express.
    def visitExpress(self, ctx:MCParser.ExpressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#simpleStament.
    def visitSimpleStament(self, ctx:MCParser.SimpleStamentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#structStamen.
    def visitStructStamen(self, ctx:MCParser.StructStamenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#stament.
    def visitStament(self, ctx:MCParser.StamentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#blockStament.
    def visitBlockStament(self, ctx:MCParser.BlockStamentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#bodyBlock.
    def visitBodyBlock(self, ctx:MCParser.BodyBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#ifStament.
    def visitIfStament(self, ctx:MCParser.IfStamentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#doWhileStament.
    def visitDoWhileStament(self, ctx:MCParser.DoWhileStamentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#forStament.
    def visitForStament(self, ctx:MCParser.ForStamentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#breakStament.
    def visitBreakStament(self, ctx:MCParser.BreakStamentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continueStament.
    def visitContinueStament(self, ctx:MCParser.ContinueStamentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#returnStament.
    def visitReturnStament(self, ctx:MCParser.ReturnStamentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#returnNone.
    def visitReturnNone(self, ctx:MCParser.ReturnNoneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#returnValue.
    def visitReturnValue(self, ctx:MCParser.ReturnValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expressStament.
    def visitExpressStament(self, ctx:MCParser.ExpressStamentContext):
        return self.visitChildren(ctx)



del MCParser