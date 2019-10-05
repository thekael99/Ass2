import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_indentifier_1(self):
        """test identifiers 1"""
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 101))

    def test_indentifier_2(self):
        """test identifiers 2"""
        self.assertTrue(TestLexer.checkLexeme("_abc_", "_abc_,<EOF>", 102))

    def test_indentifier_3(self):
        """test identifiers 3"""
        self.assertTrue(TestLexer.checkLexeme("A1_Bc", "A1_Bc,<EOF>", 103))

    def test_indentifier_4(self):
        """test identifiers 4"""
        self.assertTrue(TestLexer.checkLexeme(
            "123abc123", "123,abc123,<EOF>", 104))

    def test_indentifier_5(self):
        """test identifiers 5"""
        self.assertTrue(TestLexer.checkLexeme("int123", "int123,<EOF>", 105))

    def test_indentifier_6(self):
        """test identifiers 6"""
        self.assertTrue(TestLexer.checkLexeme("12a3int", "12,a3int,<EOF>", 106))

    def test_indentifier_7(self):
        """test identifiers 7"""
        self.assertTrue(TestLexer.checkLexeme(
            "123if1else", "123,if1else,<EOF>", 107))

    def test_indentifier_8(self):
        """test identifiers 7"""
        self.assertTrue(TestLexer.checkLexeme(
            "arrayInt[]", "arrayInt,[,],<EOF>", 108))

    def test_indentifier_9(self):
        """test identifiers 7"""
        self.assertTrue(TestLexer.checkLexeme(
            " foo(array[limit])", "foo,(,array,[,limit,],),<EOF>", 109))

    def test_keyword_1(self):
        """test keywords 1"""
        self.assertTrue(TestLexer.checkLexeme("boolean break continue else for float if int return void do while true false string",
                                              "boolean,break,continue,else,for,float,if,int,return,void,do,while,true,false,string,<EOF>", 110))



    def test_keyword_2(self):
        """test keywords 2"""
        self.assertTrue(TestLexer.checkLexeme(
            "12e3e-1string", "12e3,e,-,1,string,<EOF>", 111))

    def test_keyword_3(self):
        """test keywords 3"""
        self.assertTrue(TestLexer.checkLexeme(
            "1while-2do*3continue", "1,while,-,2,do,*,3,continue,<EOF>", 112))

    def test_interger_1(self):
        """test intergers 1"""
        self.assertTrue(TestLexer.checkLexeme("01", "01,<EOF>", 113))

    def test_interger_2(self):
        """test intergers 2"""
        self.assertTrue(TestLexer.checkLexeme("-69", "-,69,<EOF>", 114))

    def test_interger_3(self):
        """test intergers 3"""
        self.assertTrue(TestLexer.checkLexeme("0x123", "0,x123,<EOF>", 115))

    def test_interger_4(self):
        """test intergers 4"""
        self.assertTrue(TestLexer.checkLexeme(
            "1a2-1", "1,a2,-,1,<EOF>", 116))

    def test_float_1(self):
        """test float 1"""
        self.assertTrue(TestLexer.checkLexeme("1e.1e2", "1,e,.1e2,<EOF>", 117))

    def test_float_2(self):
        """test float 2"""
        self.assertTrue(TestLexer.checkLexeme(
            ".1.1.1.", ".1,.1,.1,Error Token .", 118))

    def test_float_3(self):
        """test float 3"""
        self.assertTrue(TestLexer.checkLexeme(
            "1.1.1e1.1", "1.1,.1e1,.1,<EOF>", 119))

    def test_float_4(self):
        """test float 4"""
        self.assertTrue(TestLexer.checkLexeme(
            "1.1 1. .1 1.1e1 1.e1 .1e1 1E1", "1.1,1.,.1,1.1e1,1.e1,.1e1,1E1,<EOF>", 120))

    def test_float_5(self):
        """test float 5"""
        self.assertTrue(TestLexer.checkLexeme(
            "01e01.0", "01e01,.0,<EOF>", 121))

    def test_float_6(self):
        """test float 6"""
        self.assertTrue(TestLexer.checkLexeme(
            "1e1e1e1e1", "1e1,e1e1e1,<EOF>", 122))

    def test_float_7(self):
        """test float 7"""
        self.assertTrue(TestLexer.checkLexeme(
            "-1e-1.1e-1.1", "-,1e-1,.1e-1,.1,<EOF>", 123))

    def test_float_8(self):
        """test float 8"""
        self.assertTrue(TestLexer.checkLexeme("1.2 1. .1 1e2 1.2E-2 9.0 12e8 0.33E-3 128e-42",
                                              "1.2,1.,.1,1e2,1.2E-2,9.0,12e8,0.33E-3,128e-42,<EOF>", 124))

    def test_float_9(self):
        """test float 9"""
        self.assertTrue(TestLexer.checkLexeme(
            "e-12 10.e-100 10.E10", "e,-,12,10.e-100,10.E10,<EOF>", 125))

    def test_float_10(self):
        """test float 10"""
        self.assertTrue(TestLexer.checkLexeme(
            "1e-12 10.e-100 10.E10", "1e-12,10.e-100,10.E10,<EOF>", 126))

    def test_float_11(self):
        """test float 11"""
        self.assertTrue(TestLexer.checkLexeme(".e-10", "Error Token .", 127))

    def test_float_12(self):
        """test float 12"""
        self.assertTrue(TestLexer.checkLexeme("e.1", "e,.1,<EOF>", 128))

    def test_float_13(self):
        """test float 13"""
        self.assertTrue(TestLexer.checkLexeme(
            "1.1.1.e", "1.1,.1,Error Token .", 129))

    def test_float_14(self):
        """test float 14"""
        self.assertTrue(TestLexer.checkLexeme(
            "abc123.321", "abc123,.321,<EOF>", 130))

    def test_float_15(self):
        """test float 17"""
        self.assertTrue(TestLexer.checkLexeme(
            "321.4E_tf17", "321.4,E_tf17,<EOF>", 131))

    def test_boolean_1(self):
        """test boolean 1"""
        self.assertTrue(TestLexer.checkLexeme("true", "true,<EOF>", 132))

    def test_boolean_2(self):
        """test boolean 2"""
        self.assertTrue(TestLexer.checkLexeme("false", "false,<EOF>", 133))

    def test_boolean_3(self):
        """test boolean 3"""
        self.assertTrue(TestLexer.checkLexeme(
            "truefalse", "truefalse,<EOF>", 134))

    def test_boolean_4(self):
        """test boolean 4"""
        self.assertTrue(TestLexer.checkLexeme(
            "0123.4true.2e-10", "0123.4,true,.2e-10,<EOF>", 135))

    def test_boolean_5(self):
        """test boolean 5"""
        self.assertTrue(TestLexer.checkLexeme(
            "truefalseboolean", "truefalseboolean,<EOF>", 136))

    def test_operator_1(self):
        """test operators 1"""
        self.assertTrue(TestLexer.checkLexeme(
            "+ - * / ! % || && != == < > <= >= =", "+,-,*,/,!,%,||,&&,!=,==,<,>,<=,>=,=,<EOF>", 137))

    def test_operator_2(self):
        """test operators 2"""
        self.assertTrue(TestLexer.checkLexeme(
            "var == (1+2)/3*4", "var,==,(,1,+,2,),/,3,*,4,<EOF>", 138))

    def test_operator_3(self):
        """test operators 3"""
        self.assertTrue(TestLexer.checkLexeme(
            "var = a = b * c", "var,=,a,=,b,*,c,<EOF>", 139))

    def test_operator_4(self):
        """test operators 4"""
        self.assertTrue(TestLexer.checkLexeme(
            "var = 0.1e.b", "var,=,0.1,e,Error Token .", 140))

    def test_operator_5(self):
        """test operators 5"""
        self.assertTrue(TestLexer.checkLexeme(
            "(a && b || c >= d)", "(,a,&&,b,||,c,>=,d,),<EOF>", 141))

    def test_operator_6(self):
        """test operators 5"""
        self.assertTrue(TestLexer.checkLexeme(
            'myName = "Thanghandsome" + "manly"', "myName,=,Thanghandsome,+,manly,<EOF>", 142))

    def test_comment_1(self):
        """test comments 1"""
        self.assertTrue(TestLexer.checkLexeme(
            "//this is comment line", "<EOF>", 143))

    def test_comment_2(self):
        """test comments 2"""
        self.assertTrue(TestLexer.checkLexeme(
            "// /* yes, this is cmt line \\n */", "<EOF>", 144))

    def test_comment_3(self):
        """test comments 3"""
        self.assertTrue(TestLexer.checkLexeme(
            "//still cmt line\\nsmile\nsad", "sad,<EOF>", 145))

    def test_comment_4(self):
        """test comments 4"""
        self.assertTrue(TestLexer.checkLexeme(
            "/*this is block cmt lines */", "<EOF>", 146))

    def test_comment_5(self):
        """test comments 5"""
        self.assertTrue(TestLexer.checkLexeme(
            "/* here we go again \\n \\n \\n i am here, man */", "<EOF>", 147))

    def test_comment_6(self):
        """test comments 6"""
        self.assertTrue(TestLexer.checkLexeme(
            "/* // thit's not cmn line.  Yeah, that's right \\n */ stament", "stament,<EOF>", 148))

    def test_comment_7(self):
        """test comments 7"""
        self.assertTrue(TestLexer.checkLexeme(
            "/* Still block cmt lines \\n\\t\\r\\f I'm OK */", "<EOF>", 149))

    def test_string_1(self):
        """test strings 1"""
        self.assertTrue(TestLexer.checkLexeme(
            '"You are my love"', "You are my love,<EOF>", 150))

    def test_string_2(self):
        """test strings 2"""
        self.assertTrue(TestLexer.checkLexeme(
            '"You are my love', "Unclosed String: You are my love", 151))

    def test_string_3(self):
        """test strings 3"""
        self.assertTrue(TestLexer.checkLexeme(
            '"You are my love\\u"', "Illegal Escape In String: You are my love\\u", 152))

    def test_string_4(self):
        """test strings 4"""
        self.assertTrue(TestLexer.checkLexeme(
            '"\\"\\"\\"You are my love\\"\\"\\"', 'Unclosed String: \\"\\"\\"You are my love\\"\\"\\"', 153))

    def test_string_5(self):
        """test strings 5"""
        self.assertTrue(TestLexer.checkLexeme(
            '"\\"\\"\\"You are my love\\"\\"\\""', '\\"\\"\\"You are my love\\"\\"\\",<EOF>', 154))

    def test_string_6(self):
        """test strings 6"""
        self.assertTrue(TestLexer.checkLexeme(
            '"Hello\\n\\rnWorld"', "Hello\\n\\rnWorld,<EOF>", 155))

    def test_string_7(self):
        """test strings 7"""
        self.assertTrue(TestLexer.checkLexeme(
            '"Hello\\aWorld"', "Illegal Escape In String: Hello\\a", 156))

    def test_string_8(self):
        """test strings 8"""
        self.assertTrue(TestLexer.checkLexeme(
            '"Hello\\\\bWorld"', "Hello\\\\bWorld,<EOF>", 157))

    def test_string_9(self):
        """test strings 9"""
        self.assertTrue(TestLexer.checkLexeme(
            '"Hello\\nWorld"', "Hello\\nWorld,<EOF>", 158))

    def test_string_10(self):
        """test strings 10"""
        self.assertTrue(TestLexer.checkLexeme(
            '"Hello\\\\nWorld"', "Hello\\\\nWorld,<EOF>", 159))

    def test_string_11(self):
        """test strings 11"""
        self.assertTrue(TestLexer.checkLexeme(
            '"Hello\\\\World"', "Hello\\\\World,<EOF>", 160))

    def test_string_12(self):
        """test strings 12"""
        self.assertTrue(TestLexer.checkLexeme(
            '"Hello\\"World\\"\\""', 'Hello\\"World\\"\\",<EOF>', 161))

    def test_string_13(self):
        """test strings 13"""
        self.assertTrue(TestLexer.checkLexeme(
            '"Hello\\nWorld"', "Hello\\nWorld,<EOF>", 162))

    def test_string_14(self):
        """test strings 15"""
        self.assertTrue(TestLexer.checkLexeme(
            '"/* this is string */"', "/* this is string */,<EOF>", 163))

    def test_string_15(self):
        """test strings 15"""
        self.assertTrue(TestLexer.checkLexeme(
            '"this is string"\\"', "this is string,Error Token \\", 164))

    def test_separator_1(self):
        """test separators 1"""
        self.assertTrue(TestLexer.checkLexeme(
            'a;b;c;d;e;f;', "a,;,b,;,c,;,d,;,e,;,f,;,<EOF>", 165))

    def test_separator_2(self):
        """test separators 2"""
        self.assertTrue(TestLexer.checkLexeme(
            '(a)(x){b}[c];', "(,a,),(,x,),{,b,},[,c,],;,<EOF>", 166))

    def test_separator_3(self):
        """test separators 3"""
        self.assertTrue(TestLexer.checkLexeme(
            '(a,b,c)', "(,a,,,b,,,c,),<EOF>", 167))

    def test_separator_4(self):
        """test separators 4"""
        self.assertTrue(TestLexer.checkLexeme(
            '{a[b(c)];}', "{,a,[,b,(,c,),],;,},<EOF>", 168))

    def test_separator_5(self):
        """test separators 5"""
        self.assertTrue(TestLexer.checkLexeme(
            'a(x){b}[c];', "a,(,x,),{,b,},[,c,],;,<EOF>", 169))

    def test_separator_6(self):
        """test separators 6"""
        self.assertTrue(TestLexer.checkLexeme('int a; float b; void main(a,b,c,d);',
                                              "int,a,;,float,b,;,void,main,(,a,,,b,,,c,,,d,),;,<EOF>", 170))

    def test_all_1(self):
        """test all 1"""
        self.assertTrue(TestLexer.checkLexeme(
            "int a,b; float f; string str; int array[1]", "int,a,,,b,;,float,f,;,string,str,;,int,array,[,1,],<EOF>", 171))

    def test_all_2(self):
        """test all 2"""
        self.assertTrue(TestLexer.checkLexeme(
            "int a,b,c[10]; float num[100]", "int,a,,,b,,,c,[,10,],;,float,num,[,100,],<EOF>", 172))

    def test_all_3(self):
        """test all 3"""
        self.assertTrue(TestLexer.checkLexeme(
            "void main(){};", "void,main,(,),{,},;,<EOF>", 173))

    def test_all_4(self):
        """test all 4"""
        self.assertTrue(TestLexer.checkLexeme("int[] functionInt(float f[]);",
                                              "int,[,],functionInt,(,float,f,[,],),;,<EOF>", 174))

    def test_all_5(self):
        """test all 5"""
        self.assertTrue(TestLexer.checkLexeme(
            "int a[1]; //too tired ", "int,a,[,1,],;,<EOF>", 175))

    def test_all_6(self):
        """test all 6"""
        self.assertTrue(TestLexer.checkLexeme(
            "//{void main();}", "<EOF>", 176))

    def test_all_7(self):
        """test all 7"""
        self.assertTrue(TestLexer.checkLexeme(
            "if (1e1) b; else c;", "if,(,1e1,),b,;,else,c,;,<EOF>", 177))

    def test_all_8(self):
        """test all 8"""
        self.assertTrue(TestLexer.checkLexeme(
            "1a.4e-10", "1,a,.4e-10,<EOF>", 178))

    def test_all_9(self):
        """test all 9"""
        self.assertTrue(TestLexer.checkLexeme(
            '"string\\nstring"', "string\\nstring,<EOF>", 179))

    def test_all_10(self):
        """test all 10"""
        self.assertTrue(TestLexer.checkLexeme(
            "1true 2if 3while 4do", "1,true,2,if,3,while,4,do,<EOF>", 180))

    def test_all_11(self):
        """test all 11"""
        self.assertTrue(TestLexer.checkLexeme(
            '/* spam */1+"string"', "1,+,string,<EOF>", 181))

    def test_all_12(self):
        """test all 12"""
        self.assertTrue(TestLexer.checkLexeme(
            '"abcd"abc"ab', "abcd,abc,Unclosed String: ab", 182))

    def test_all_13(self):
        """test all 13"""
        self.assertTrue(TestLexer.checkLexeme('"123e-10-1234.E10"\\a',
                                              "123e-10-1234.E10,Error Token \\", 183))

    def test_all_14(self):
        """test all 14"""
        self.assertTrue(TestLexer.checkLexeme(
            '"@@"', "@@,<EOF>", 184))

    def test_all_15(self):
        """test all 15"""
        self.assertTrue(TestLexer.checkLexeme(
            "a==!b==-c", "a,==,!,b,==,-,c,<EOF>", 185))

    def test_all_16(self):
        """test all 16"""
        self.assertTrue(TestLexer.checkLexeme('"Hello\\iMyNameIsThang"',
                                              "Illegal Escape In String: Hello\i", 186))

    def test_all_17(self):
        """test all 17"""
        self.assertTrue(TestLexer.checkLexeme(
            'do{int a;}{"string\\n"}while(true);', "do,{,int,a,;,},{,string\\n,},while,(,true,),;,<EOF>", 187))

    def test_all_18(self):
        """test all 18"""
        self.assertTrue(TestLexer.checkLexeme(
            'a+1+float+b[1]', "a,+,1,+,float,+,b,[,1,],<EOF>", 188))

    def test_all_19(self):
        """test all 19"""
        self.assertTrue(TestLexer.checkLexeme(
            '_a123-53.e-1 _.E10', "_a123,-,53.e-1,_,Error Token .", 189))

    def test_all_20(self):
        """test all 20"""
        self.assertTrue(TestLexer.checkLexeme(
            'array[((iter))];', "array,[,(,(,iter,),),],;,<EOF>", 190))

    def test_program_1(self):
        """test program token 1"""
        self.assertTrue(TestLexer.checkLexeme(
            ''' 
            int a[1], b;
            void main(){
                int i, temp;
                for(i=1;i<10;i=i+1)
                    {
                        if(temp<10)
                            temp=temp+1;
                    }
                return;
            }
            ''', "int,a,[,1,],,,b,;,void,main,(,),{,int,i,,,temp,;,for,(,i,=,1,;,i,<,10,;,i,=,i,+,1,),{,if,(,temp,<,10,),temp,=,temp,+,1,;,},return,;,},<EOF>", 191))
    
    def test_program_2(self):
        """test program token 2"""
        self.assertTrue(TestLexer.checkLexeme(
            ''' 
            int foo(int a[])
            {
                return a[0];
            };
            void main(){
                int arr[10];
                float f;
                f = 0;
                do f=f+foo(arr); f=f+1; while foo(arr)+f<100;
                return;
            }
            ''', "int,foo,(,int,a,[,],),{,return,a,[,0,],;,},;,void,main,(,),{,int,arr,[,10,],;,float,f,;,f,=,0,;,do,f,=,f,+,foo,(,arr,),;,f,=,f,+,1,;,while,foo,(,arr,),+,f,<,100,;,return,;,},<EOF>", 192))
    
    def test_program_3(self):
        """test program token 3"""
        self.assertTrue(TestLexer.checkLexeme(
            ''' 
            int a;
            float b;
            string c;
            int d[10]
            void main(){
                {

                }
                return;
            }
            ''' , "int,a,;,float,b,;,string,c,;,int,d,[,10,],void,main,(,),{,{,},return,;,},<EOF>", 193))

    def test_program_4(self):
        """test program token 4"""
        self.assertTrue(TestLexer.checkLexeme(
            ''' 
            void main(){
                {
                    int a,b;
                    boolean c,d;
                    a = 10 ;
                    b = 5;
                    c = true;
                    d = c == (a>b);
                }
                {
                    a = a+b; 
                }
                return;
            }
            ''' , "void,main,(,),{,{,int,a,,,b,;,boolean,c,,,d,;,a,=,10,;,b,=,5,;,c,=,true,;,d,=,c,==,(,a,>,b,),;,},{,a,=,a,+,b,;,},return,;,},<EOF>", 194))

    def test_program_5(self):
        """test program token 5"""
        self.assertTrue(TestLexer.checkLexeme(
            ''' 
            int[] foo(){
                int a[5];
                return a;
            }
            void main(){
                foo();
                return;
            }
            ''' , "int,[,],foo,(,),{,int,a,[,5,],;,return,a,;,},void,main,(,),{,foo,(,),;,return,;,},<EOF>", 195))
    
    def test_program_6(self):
        """test program token 6"""
        self.assertTrue(TestLexer.checkLexeme(
            ''' 
            void main(){
                return;
            }
            int a;
            int b;
            ''' , "void,main,(,),{,return,;,},int,a,;,int,b,;,<EOF>", 196))
        
    def test_program_7(self):
        """test program token 7"""
        self.assertTrue(TestLexer.checkLexeme(
            ''' 
            void main(){
                string str = "Chery Chery Lady\\n"
                int a = 10;
                return;
            }
            ''', "void,main,(,),{,string,str,=,Chery Chery Lady\\n,int,a,=,10,;,return,;,},<EOF>", 197))


    def test_program_8(self):
        """test program token 8"""
        self.assertTrue(TestLexer.checkLexeme(
            ''' 
            void main(){
                int foo(){
                    return 1;
                }
                int a;
                a=foo();
                return;
            }
            ''' , "void,main,(,),{,int,foo,(,),{,return,1,;,},int,a,;,a,=,foo,(,),;,return,;,},<EOF>", 198))

    def test_program_9(self):
        """test program token 9"""
        self.assertTrue(TestLexer.checkLexeme(
            ''' 
            void main(){
                int a;
                {a =1;}
                if(a==1)
                    return;
                else                
                    return;
            }
            ''', "void,main,(,),{,int,a,;,{,a,=,1,;,},if,(,a,==,1,),return,;,else,return,;,},<EOF>", 199))

    def test_program_10(self):
        """test program token 10"""
        self.assertTrue(TestLexer.checkLexeme(
            ''' 
            int foo(int a){
                if((a%2)==0)
                    a+=1;
                else
                    do a=a-1;
                    while a > 0;
                return a;
            }
            void main(){
                int a,b[10],i;
                a=10;
                for(i=0;i<10;i=i+1)
                    b[i]=foo(a);                
                return;
            }
            ''', "int,foo,(,int,a,),{,if,(,(,a,%,2,),==,0,),a,+,=,1,;,else,do,a,=,a,-,1,;,while,a,>,0,;,return,a,;,},void,main,(,),{,int,a,,,b,[,10,],,,i,;,a,=,10,;,for,(,i,=,0,;,i,<,10,;,i,=,i,+,1,),b,[,i,],=,foo,(,a,),;,return,;,},<EOF>", 200))
