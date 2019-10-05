import unittest
from TestUtils import TestAST
from AST import*


class ASTGenSuite(unittest.TestCase):

    # def test_1(self):
    #     """ """
    #     input = """int a[1], b;
    #         void main(){
    #             int i, temp;
    #             for(i=1;i<10;i=i+1)
    #                 {
    #                     if(temp<10)
    #                         temp=temp+1;
    #                 }
    #             return;
    #         }"""
    #     expect = str(Program([VarDecl(Id("a"), ArrayType(1, IntType())), VarDecl(Id("b"), IntType()), FuncDecl(Id("main"), [], VoidType(), Block([VarDecl(Id("i"), IntType()), VarDecl(Id("temp"), IntType()), For(BinaryOp("=", Id("i"), IntLiteral(1)), BinaryOp(
    #         "<", Id("i"), IntLiteral(10)), BinaryOp("=", Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([If(BinaryOp("<", Id("temp"), IntLiteral(10)), BinaryOp("=", Id("temp"), BinaryOp("+", Id("temp"), IntLiteral(1))))])), Return()]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    # def test_2(self):
    #     """ """
    #     input = """int foo(int a[])
    #         {
    #             return a[0];
    #         }
    #         void main(){
    #             int arr[10];
    #             float f;
    #             f = 0;
    #             do f=f+foo(arr); f=f+1; while (foo(arr)+f)<100;
    #             return;
    #         }"""
    #     expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), ArrayPointerType(IntType()))], IntType(), Block([Return(ArrayCell(Id("a"), IntLiteral(0)))])), FuncDecl(Id("main"), [], VoidType(), Block([VarDecl(Id("arr"), ArrayType(10, IntType())), VarDecl(Id("f"), FloatType()), BinaryOp(
    #         "=", Id("f"), IntLiteral(0)), Dowhile([BinaryOp("=", Id("f"), BinaryOp("+", Id("f"), CallExpr(Id("foo"), [Id("arr")]))), BinaryOp("=", Id("f"), BinaryOp("+", Id("f"), IntLiteral(1)))], BinaryOp("<", BinaryOp("+", CallExpr(Id("foo"), [Id("arr")]), Id("f")), IntLiteral(100))), Return()]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    # def test_3(self):
    #     """ """
    #     input = """int a;
    #         float b;
    #         string c;
    #         int d[10];
    #         void main(){
    #             {

    #             }
    #             return;
    #         }"""
    #     expect = str(Program([VarDecl(Id("a"), IntType()), VarDecl(Id("b"), FloatType()), VarDecl(Id("c"), StringType()), VarDecl(
    #         Id("d"), ArrayType(10, IntType())), FuncDecl(Id("main"), [], VoidType(), Block([Block([]), Return()]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    # def test_4(self):
    #     """ """
    #     input = """void main(){
    #             {
    #                 int a,b;
    #                 boolean c,d;
    #                 a = 10 ;
    #                 b = 5;
    #                 c = true;
    #                 d = c == (a>b);
    #             }
    #             {
    #                 a = a+b; 
    #             }
    #             return;
    #         }"""
    #     expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([Block([VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType()), VarDecl(Id("c"), BoolType()), VarDecl(Id("d"), BoolType()), BinaryOp("=", Id("a"), IntLiteral(10)), BinaryOp(
    #         "=", Id("b"), IntLiteral(5)), BinaryOp("=", Id("c"), BooleanLiteral(True)), BinaryOp("=", Id("d"), BinaryOp("==", Id("c"), BinaryOp(">", Id("a"), Id("b"))))]), Block([BinaryOp("=", Id("a"), BinaryOp("+", Id("a"), Id("b")))]), Return()]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    # def test_5(self):
    #     """ """
    #     input = """int[] foo(){
    #             int a[5];
    #             return a;
    #         }
    #         void main(){
    #             foo();
    #             return;
    #         }"""
    #     expect = str(Program([FuncDecl(Id("foo"), [], ArrayPointerType(IntType()), Block([VarDecl(Id("a"), ArrayType(
    #         5, IntType())), Return(Id("a"))])), FuncDecl(Id("main"), [], VoidType(), Block([CallExpr(Id("foo"), []), Return()]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    # def test_6(self):
    #     """ """
    #     input = """void main(){
    #             return;
    #         }
    #         int a,b;"""
    #     expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block(
    #         [Return()])), VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType())]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    # def test_7(self):
    #     """ """
    #     input = """void main(){
    #             string str;
    #             str = "Chery Chery Lady\\n";
    #             int a;
    #             a = 10;
    #             return;
    #         }"""
    #     expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([VarDecl(Id("str"), StringType()), BinaryOp("=", Id(
    #         "str"), StringLiteral("Chery Chery Lady\\n")), VarDecl(Id("a"), IntType()), BinaryOp("=", Id("a"), IntLiteral(10)), Return()]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    # def test_8(self):
    #     """ """
    #     input = """
    #         int foo()
    #         {
    #             return 1;
    #         }
    #         void main()
    #         {
    #             int a;
    #             a=foo();
    #             return;
    #         }"""
    #     expect = str(Program([FuncDecl(Id("foo"), [], IntType(), Block([Return(IntLiteral(1))])), FuncDecl(Id("main"), [
    #     ], VoidType(), Block([VarDecl(Id("a"), IntType()), BinaryOp("=", Id("a"), CallExpr(Id("foo"), [])), Return()]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    # def test_9(self):
    #     """ """
    #     input = """void main(){
    #             int a;
    #             {a =1;}
    #             if(a==1)
    #                 return;
    #             else                
    #                 return;
    #         }"""
    #     expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([VarDecl(Id("a"), IntType()), Block(
    #         [BinaryOp("=", Id("a"), IntLiteral(1))]), If(BinaryOp("==", Id("a"), IntLiteral(1)), Return(), Return())]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    # def test_10(self):
    #     """ """
    #     input = """int foo(int a){
    #             if((a%2)==0)
    #                 a=a+1;
    #             else
    #                 do a=a-1;
    #                 while a > 0;
    #             return a;
    #         }
    #         void main(){
    #             int a,b[10],i;
    #             a=10;
    #             for(i=0;i<10;i=i+1)
    #                 b[i]=foo(a);                
    #             return;
    #         }"""
    #     expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), IntType())], IntType(), Block([If(BinaryOp("==", BinaryOp("%", Id("a"), IntLiteral(2)), IntLiteral(0)), BinaryOp("=", Id("a"), BinaryOp("+", Id("a"), IntLiteral(1))), Dowhile([BinaryOp("=", Id("a"), BinaryOp("-", Id("a"), IntLiteral(1)))], BinaryOp(">", Id("a"), IntLiteral(0)))), Return(Id("a"))])), FuncDecl(Id("main"), [], VoidType(
    #     ), Block([VarDecl(Id("a"), IntType()), VarDecl(Id("b"), ArrayType(10, IntType())), VarDecl(Id("i"), IntType()), BinaryOp("=", Id("a"), IntLiteral(10)), For(BinaryOp("=", Id("i"), IntLiteral(0)), BinaryOp("<", Id("i"), IntLiteral(10)), BinaryOp("=", Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), BinaryOp("=", ArrayCell(Id("b"), Id("i")), CallExpr(Id("foo"), [Id("a")]))), Return()]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    # def test_11(self):
    #     """ """
    #     input = """int main(){int a,b,c,d;}"""
    #     expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([VarDecl(Id("a"), IntType()), VarDecl(
    #         Id("b"), IntType()), VarDecl(Id("c"), IntType()), VarDecl(Id("d"), IntType())]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    # def test_12(self):
    #     """ """
    #     input = """int main(){int a[10],b,c,d;}"""
    #     expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([VarDecl(Id("a"), ArrayType(
    #         10, IntType())), VarDecl(Id("b"), IntType()), VarDecl(Id("c"), IntType()), VarDecl(Id("d"), IntType())]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    # def test_13(self):
    #     """ """
    #     input = """int main(){int a[10];}"""
    #     expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block(
    #         [VarDecl(Id("a"), ArrayType(10, IntType()))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    # def test_14(self):
    #     """ """
    #     input = """int main(){float a,b,c,d[10];}"""
    #     expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([VarDecl(Id("a"), FloatType()), VarDecl(
    #         Id("b"), FloatType()), VarDecl(Id("c"), FloatType()), VarDecl(Id("d"), ArrayType(10, FloatType()))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    # def test_15(self):
    #     """ """
    #     input = """void foo(int i){}
    #             int child_of_foo(float f)
    #             {
    #     }"""
    #     expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("i"), IntType())], VoidType(), Block(
    #         [])), FuncDecl(Id("child_of_foo"), [VarDecl(Id("f"), FloatType())], IntType(), Block([]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    # def test_16(self):
    #     """ """
    #     input = """int[] foo(int a,float b[]) {
    #             int c[3];
    #             if(a>0) foo(a-1,b);
    #             else return c;
    #     }"""
    #     expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), IntType()), VarDecl(Id("b"), ArrayPointerType(FloatType()))], ArrayPointerType(IntType()), Block([VarDecl(
    #         Id("c"), ArrayType(3, IntType())), If(BinaryOp(">", Id("a"), IntLiteral(0)), CallExpr(Id("foo"), [BinaryOp("-", Id("a"), IntLiteral(1)), Id("b")]), Return(Id("c")))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    # def test_17(self):
    #     """ """
    #     input = """int main(){
    #         boolean boo; boo[2]=false;
    #     }"""
    #     expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([VarDecl(Id("boo"), BoolType(
    #     )), BinaryOp("=", ArrayCell(Id("boo"), IntLiteral(2)), BooleanLiteral(False))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    # def test_18(self):
    #     """ """
    #     input = """int main(){
    #         boolean c;
    #         int i;
    #         i=a+3;
    #         if (i>0){
    #             int d;
    #             d=i+3;
    #             putInt(d);
    #         }
    #         return i;
    #     }"""
    #     expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([VarDecl(Id("c"), BoolType()), VarDecl(Id("i"), IntType()), BinaryOp("=", Id("i"), BinaryOp("+", Id("a"), IntLiteral(3))), If(
    #         BinaryOp(">", Id("i"), IntLiteral(0)), Block([VarDecl(Id("d"), IntType()), BinaryOp("=", Id("d"), BinaryOp("+", Id("i"), IntLiteral(3))), CallExpr(Id("putInt"), [Id("d")])])), Return(Id("i"))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    # def test_19(self):
    #     """ """
    #     input = """int main(){
    #         int a[1];
    #         a=foo(2)[3+x]=a[b[2]]+3;
    #     }"""
    #     expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([VarDecl(Id("a"), ArrayType(1, IntType())), BinaryOp("=", Id("a"), BinaryOp("=", ArrayCell(CallExpr(
    #         Id("foo"), [IntLiteral(2)]), BinaryOp("+", IntLiteral(3), Id("x"))), BinaryOp("+", ArrayCell(Id("a"), ArrayCell(Id("b"), IntLiteral(2))), IntLiteral(3))))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    # def test_20(self):
    #     """ """
    #     input = """int main(){
    #         int n;
    #         n=10;
    #         if (n>10)
    #         {
    #             printName();
    #         }
    #         else{
    #             n=n+1;
    #         }
    #     }"""
    #     expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([VarDecl(Id("n"), IntType()), BinaryOp("=", Id("n"), IntLiteral(10)), If(BinaryOp(
    #         ">", Id("n"), IntLiteral(10)), Block([CallExpr(Id("printName"), [])]), Block([BinaryOp("=", Id("n"), BinaryOp("+", Id("n"), IntLiteral(1)))]))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    # def test_1(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    # def test_2(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    # def test_3(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    # def test_4(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    # def test_5(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    # def test_6(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    # def test_7(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    # def test_8(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    # def test_9(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    # def test_10(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    # def test_1(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    # def test_2(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    # def test_3(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    # def test_4(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    # def test_5(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    # def test_6(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    # def test_7(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    # def test_8(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    # def test_9(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    # def test_10(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    # def test_1(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    # def test_2(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    # def test_3(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    # def test_4(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    # def test_5(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    # def test_6(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    # def test_7(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    # def test_8(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    # def test_9(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    # def test_10(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    # def test_1(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    # def test_2(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    # def test_3(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    # def test_4(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    # def test_5(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    # def test_6(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    # def test_7(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    # def test_8(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    # def test_9(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    # def test_10(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    # def test_1(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    # def test_2(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    # def test_3(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    # def test_4(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    # def test_5(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    # def test_6(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    # def test_7(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    # def test_8(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    # def test_9(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    # def test_10(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    # def test_1(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    # def test_2(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    # def test_3(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    # def test_4(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    # def test_5(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    # def test_6(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    # def test_7(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    # def test_8(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    # def test_9(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    # def test_10(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    # def test_1(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    # def test_2(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    # def test_3(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    # def test_4(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    # def test_5(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    # def test_6(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    # def test_7(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    # def test_8(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    # def test_9(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    # def test_10(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    # def test_1(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    # def test_2(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    # def test_3(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    # def test_4(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    # def test_5(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    # def test_6(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    # def test_7(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    # def test_8(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    # def test_9(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    # def test_10(self):
    #     """ """
    #     input = """"""
    #     expect = str()
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    # def test_simple_program(self):
    #     """Simple program: int main() {}"""
    #     input = """int main() {}"""
    #     expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,398))

    # def test_more_complex_program(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(4);
    #     }"""
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,399))

    # def test_call_without_parameter(self):
    #     """More complex program"""
    #     input = """int main () {
    #         getIntLn();
    #     }"""
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("getIntLn"),[])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,400))
