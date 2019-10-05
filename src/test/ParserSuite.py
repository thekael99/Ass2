import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):    

    def test1(self):
        input = """int a[1], b;
            void main(){
                int i, temp;
                for(i=1;i<10;i=i+1)
                    {
                        if(temp<10)
                            temp=temp+1;
                    }
                return;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test2(self):
        input = """int foo(int a[])
            {
                return a[0];
            }
            void main(){
                int arr[10];
                float f;
                f = 0;
                do f=f+foo(arr); f=f+1; while (foo(arr)+f)<100;
                return;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test3(self):
        input = """int a;
            float b;
            string c;
            int d[10];
            void main(){
                {

                }
                return;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))


    def test4(self):
        input = """void main(){
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
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test5(self):
        input = """int[] foo(){
                int a[5];
                return a;
            }
            void main(){
                foo();
                return;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test6(self):
        input = """void main(){
                return;
            }
            int a;
            int b;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test7(self):
        input = """void main(){
                string str = "Chery Chery Lady\\n";
                int a = 10;
                return;
            }"""
        expect = "Error on line 2 col 27: ="
        self.assertTrue(TestParser.checkParser(input, expect, 207))
    
    def test8(self):
        input = """void main(){
                int foo(){
                    return 1;
                }
                int a;
                a=foo();
                return;
            }"""
        expect = "Error on line 2 col 23: ("
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test9(self):
        input = """void main(){
                int a;
                {a =1;}
                if(a==1)
                    return;
                else                
                    return;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test10(self):
        input = """int foo(int a){
                if((a%2)==0)
                    a=a+1;
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
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test11(self):
        input = """int main(){int a,b,c,d;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test12(self):
        input = """int main(){int a[10],b,c,d;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test13(self):
        input = """int main(){int a[];}"""
        expect = "Error on line 1 col 17: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test14(self):
        input = """int main(){float a,b,c,d[]}"""
        expect = "Error on line 1 col 25: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test15(self):
        input = """void foo(int i){
                int child_of_foo(float f){}
        }"""
        expect = "Error on line 2 col 32: ("
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test16(self):
        input = """int[] foo(int a,float b[]) {
                int c[3];
                if(a>0) foo(a-1,b);
                else return c;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test17(self):
        input = """int main(){
            boolean boo[2]={true,false};
        }"""
        expect = "Error on line 2 col 26: ="
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test18(self):
        input = """int main(){
            boolean c;
            int i;
            i=a+3;
            if (i>0){
                int d;
                d=i+3;
                putInt(d);
            }
            return i;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test19(self):
        input = """int main(){
            int a[];
            a=foo(2)[3+x]=a[b[2]]+3;
        }"""
        expect = "Error on line 2 col 18: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test20(self):
        input = """int main(){
            int n;
            n=10;
            if (n>10)
            {
                printName();
            }
            else{
                n=n+1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))


    def test21(self):
        input = """void main( ){ if (a) if (b) if (c) a; else a; else }"""
        expect = "Error on line 1 col 51: }"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test22(self):
        input = """int main(){"return";}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test23(self):
        input = """int main(){
            if (n)
            {
                printName();    
            }
            else
            {

            }
          
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test24(self):
        input = """int main(){
            do{
                int a;
                a=10;
                
            }
            {

            }while("string");
          
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test25(self):
        input = """int main(){
            for (int i=0;i<10;i++)
            {
                print("This is PPL");
            }   
        }"""
        expect = "Error on line 2 col 17: int"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test26(self):
        input = """int main(){
            for (i=0;i<10;i=i+1)
            {
                print("This is PPL");
            }   
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test27(self):
        input = """int main(){
            for (i=0;i<10;i=i+1)
            {
                print("This is PPL");
            }
            {

            } 
            {

            }  
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test28(self):
        input = """int main(){
            for (i=0;i<10;i=i+1)
            {
                print("This is PPL");
                if (i==5)
                {
                    break;
                }
            }             
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test29(self):
        input = """int main(){
            for (i=0;i<10;i=i+1)
            {
                print("This is PPL");
                if (i==5)
                {
                    break
                }
            }
             
        }"""
        expect = "Error on line 8 col 16: }"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test30(self):
        input = """int main(){
            for (i=0;i<10;i=i+1)
            {
                print("This is PPL");
                if (i==5)
                {
                    continue;
                }
            }
             
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))


    def test31(self):
        input = """int main(){
            int i;
            i=10;
            print(i);
            system("pause");
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test32(self):
        input = """int main(){
            i=1;
            i+2;
            100;
            foo(1,2); 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test33(self):
        input = """int main(){
            i=1;
            i+2;
            100
            foo(1,2); 
        }"""
        expect = "Error on line 5 col 12: foo"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test34(self):
        input = """int main(){
            int a,b,c;
            a=b=c=5;
            float f[5];
            if (a==b) f[0]=1.0;      
        }
        {

        }"""
        expect = "Error on line 7 col 8: {"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test35(self):
        input = """int main(){

        }
        {

        }"""
        expect = "Error on line 4 col 8: {"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test36(self):
        input = """int main(){
            boolean check;
            if(!check) print(check);                  
        }
        {
        }"""
        expect = "Error on line 5 col 8: {"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test37(self):
        input = """int main(){ a==b==c;}"""
        expect = "Error on line 1 col 16: =="
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test38(self):
        input = """int main(){ boolean check; check=true;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test39(self):
        input = """int main(){if(b) if (a) if (c) {} else {} else {} }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test40(self):
        input = """int i;
        int f(){
            return 200;
        }
        void main(){
            int test;
            test=f();
            putIntLn(test);
            {
                int i;
                int test;
                int f;
                test=f=i=100;
                putIntLn(i);
                putIntLn(test);
                putIntLn(f);

            }
            putIntLn(test);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test41(self):
        input = """int main(){
        float array[2][2];}"""
        expect = "Error on line 2 col 22: ["
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test42(self):
        input = """void main()
        { 
            c+[a+b];
        }"""
        expect = "Error on line 3 col 14: ["
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test43(self):
        input = """int x,y[8];
        int a,b,c;
        void main(){
            array[d[r[a(10)]]];
        }
        void rescusive(int i,float z){
            int x;
            int c;
            if(exp)
                stamentt;
            else
                stmt;
            for(w;i;z){
                int x;
                if(a==5)
                    x=5;
            
                for (exp1;exp2;exp3) printf();
                int x,y,arr[69];
            }
            return ;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test44(self):
        input = """void func(){if(a<=b) {int a;}} ;}"""
        expect = "Error on line 1 col 31: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test45(self):
        input = """int main({}"""
        expect = "Error on line 1 col 9: {"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test46(self):
        input = """string test(int test[],string test1){
            boolean check;
            check = false;
            if (check==true) 
                a=2; 
            else a=3;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test47(self):
        input = """string test(int test[],string test1){
            if (a>b<c) 
                a=2; else a=3;
        }"""
        expect = "Error on line 2 col 19: <"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test48(self):
        input = """float test(){
            int a[4],b[5],c[6],d;
            {
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test49(self):
        input = """int main(){
            do while a==true;
        }"""
        expect = "Error on line 2 col 15: while"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test50(self):
        input = """int main(){
            do{} while a==true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test51(self):
        input = """int main(){"""
        expect = "Error on line 1 col 11: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test52(self):
        input = """int main(){
            int !a;
        }"""
        expect = "Error on line 2 col 16: !"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test53(self):
        input = """int main(){
            if (a>b) 
                c=a; 
            else c=b; 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test54(self):
        input = """int main(){
            if (a<b) c=a; 
            else 
                if(c<b)
                    c=b;
                else
                    c=b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test55(self):
        input = """int main(){
            for (i=0;i<10;i=i+1) 
                {
                    putInt(1);
                }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test56(self):
        input = """int main(){
             a=b=c;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test57(self):
        input = """int main(){
            a || b || c || d && e && f; 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test58(self):
        input = """int main(){
           foo(2)[x+3];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test59(self):
        input = """int main(){
           foo(foo(2)[x+3]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test60(self):
        input = """int main(){
           foo(2)[x+3][x+4];
        }"""
        expect = "Error on line 2 col 22: ["
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test61(self):
        input = """int main(){
            a+foo(a+b,c*d); 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test62(self):
        input = """int main(){
            a=1/2+3*4-5/6;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test63(self):
        input = """int main(){
            foo(2)[x+3]+2*foo(1)(x-1)-6%3;
        }"""
        expect = "Error on line 2 col 32: ("
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test64(self):
        input = """void main(){
            a[b[c[foo(d)]]];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test65(self):
        input = """int[] a,b,c[1];
        string[] str;
        boolean[] bool;
        float[] f"""
        expect = "Error on line 1 col 7: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test66(self):
        input = """int[] main(){
            int x[];
            funcall();
        }"""
        expect = "Error on line 2 col 18: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test67(self):
        input = """void main(){
            if(a>0) 
                if(!b) 
                    if(b==c) break; 
                    else continue; 
                else return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test68(self):
        input = """int main(){
            do {
                foo(5);
            }
            int a = 5;
        }"""
        expect = "Error on line 5 col 12: int"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test69(self):
        input = """int main(){
            str = "string\\";
            }"""
        expect = 'string\\";'
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test70(self):
        input = """int main(){
            string abc;
            a == b == c;
        }"""
        expect = "Error on line 3 col 19: =="
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test71(self):
        input = """int foo (int a , float b[])
        {
            boolean c ;
            int i ;
            i = a + 3 ;
            if (i > 0)
            {
                int d ;
                d = i + 3;
                putInt(d);
            }
            return i;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test72(self):
        input = """int main()
        {
            a = !b + -a;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test73(self):
        input = """int main()
        {
            a = a * b < (c > d);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test74(self):
        input = """int main() {
            a = a + b < c == d;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test75(self):
        input = """ int main() {
            foo(foo(2))[3+x] = a[b[c[2]]] +3;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test76(self):
        input = """ int[] foo (int b[]){
            int a[69];
            if (b>c)
                return a+1;
            else
                return b-1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test77(self):
        input = """int main(){
            do
            {
                {
                    if (b>c)
                        return a+1;
                    else
                        return b-1;                    
                }
            }
            {
                a+b;
            }
            while (a<5);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test78(self):
        input = """int main(){
            do
            while
                true;
            }"""
        expect = "Error on line 3 col 12: while"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test79(self):
        input = """int main(){
            int a[10];
            return foo(a[10]);	
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test80(self):
        input = """int main(){
                foo(a,b);
            }
            void foo(int a[], float b){
                if (a == 0) 
                    return a;
                else {
                    foo(b,a);
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test81(self):
        input = """int main(){
            string abc;
            a>=b>=c>=d
        }"""
        expect = "Error on line 3 col 16: >="
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test82(self):
        input = """
        int main()
        {
            int fp;
            int c;
            fp = fopen(__FILE__,"r");
            do {
                c = getc(fp);
                putchar(c);
            }
            while(c != EOF);
            fclose(fp);
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test83(self):
        input = """
        int main()
        {
            int i, n, t1, t2, nextTerm;
            printf(\"Enter the number of terms: \");
            scanf(n);
            printf(\"Fibonacci Series: \");
            for (i = 1; i <= n; i=i+1)
            {
                printf(t1);
                nextTerm = t1 + t2;
                t1 = t2;
                t2 = nextTerm;
            }
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test84(self):
        input = """
        int main()
        {
            float number;
            printf(\"Enter a number: \");
            scanf(number);
            if (number <= 0.0)
            {
                if (number == 0.0)
                    printf(\"You entered 0.\");
                else
                    printf(\"You entered a negative number.\");
            }
            else
                printf(\"You entered a positive number.\");
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test85(self):
        input = """
        int main()
        {
            float number;
            printf(\"Enter a number: \");
            scanf(number);
            // true if number is less than 0
            if (number < 0.0)
                printf(\"You entered a negative number.\");
                // true if number is greater than 0
            else 
                if ( number > 0.0)
                    printf(\"You entered a positive number\");
                    // if both test expression is evaluated to false
                else
                    printf(\"You entered 0.\");
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test86(self):
        input = """
        int main()
        {
            int n, i, flag;
            printf(\"Enter a positive integer: \");
            scanf(n);
            for(i = 2; i <= n/2; i=i+1)
                {
                    // condition for nonprime number
                    if((n%i) == 0)
                    {
                        flag = 1;
                        break;
                    }
                }
            if (n == 1) 
                {
                    printf(\"1 is neither a prime nor a composite number.\");
                }
            else 
                {
                    if (flag == 0)
                        printf(n);
                    else
                        printf(n);
                }
    
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test87(self):
        input = """
        int main()
        {
            int low, high, i, flag;
            printf(\"Enter two numbers(intervals): \");
            scanf(low, high);
            printf(low, high);
            do
            {
                flag = 0;
                for(i = 2; i <= low/2; i=i+1)
                {
                    if(low % i == 0)
                        {
                            flag = 1;
                            break;
                        }
                }
                 if (flag == 0)
                    printf(low);
                low=low+1;
            }
            while (low < high);
            return 0;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test88(self):
        input = """
        int main()
        {
            int low, high, i, flag, temp;
            printf(\"Enter two numbers(intevals): \");
            scanf(low, high);
            //swapping numbers if low is greater than high
            if (low > high)
            {
                temp = low;
                low = high;
                high = temp;
            }
            printf(low, high);
            do
            {
                int a;
                for(i = 2; i <= low/2; i=i+1)
                {
                    if(low % i == 0)
                    {
                        flag = 1;
                        break;
                    }
                }                
            }
            {
                flag = 0;
                for(i = 2; i <= low/2; i=i+1)
                {
                    if(low % i == 0)
                    {
                        flag = 1;
                        break;
                    }
                }
                if (flag == 0)
                    printf(low);
                low=low+1;
            }
            while (low < high);
            return 0;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test89(self):
        input = """
        // user-defined function to check prime number
        int checkPrimeNumber(int n)
        {
            int j, flag;
            for(j=2; j <= n/2; j=j+1)
            {
                if (n%j == 0)
                {
                    flag =0;
                    break;
                }
            }
        return flag;
        }

        int main()
        {
            int n1, n2, i, flag;
            printf(\"Enter two positive integers: \");
            scanf(n1, n2);
            printf(n1, n2);
            for(i=n1+1; i<n2; i=i+1)
            {
                // i is a prime number, flag will be equal to 1
                flag = checkPrimeNumber(i);
                if(flag == 1)
                printf(i);
            }
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test90(self):
        input = """
        int main()
        {
            int n1, n2;    
            printf(\"Enter two positive integers: \");
            scanf(n1,n2);
            do
            {
                if(n1 > n2)
                    n1 = n1 - n2;
                else
                    n2 = n2 - n1;
            }
            while(n1!=n2);
            printf(\"GCD = \",n1);
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test91(self):
        input = """
        int addNumbers(int n)
        {
            if(n != 0)
            return n + addNumbers(n-1);
            else
            return n;
        }
        int main()
        {
            int num;
            printf(\"Enter a positive integer: \");
            scanf(num);
            printf(\"Sum = \",addNumbers(num));
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test92(self):
        input = """
        int main()
        {
            int n, i, sum;
    
            printf(\"Enter a positive integer: \");
            scanf(n);
            for(i=1; i <= n; i=i+1)
            {
                sum = sum+i;
            }
            printf(\"Sum = \",sum);
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test93(self):
        input = """
        int main()
        {
            int number, i;
            printf(\"Enter a positive integer: \");
            scanf(number);
            printf(number);
            for(i=1; i <= number; i=i+1)
            {
                if (number%i == 0)
                {
                    printf(i);
                }
            }
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test94(self):
        input = """
        int main()
        {
            int n, reversedInteger, remainder, originalInteger;
            printf(\"Enter an integer: \");
            scanf(n);
            originalInteger = n;
            // reversed integer is stored in variable 
            do
            {
                remainder = n%10;
                reversedInteger = reversedInteger*10 + remainder;
                n = n / 10;
            }
            while( n!=0 );
            // palindrome if orignalInteger and reversedInteger are equal
            if (originalInteger == reversedInteger)
                printf(originalInteger);
            else
                printf(originalInteger);
    
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test95(self):
        input = """
        int main()
        {
            int dividend, divisor, quotient, remainder;
            printf(\"Enter dividend: \");
            scanf(dividend);
            printf(\"Enter divisor: \");
            scanf(divisor);
            // Computes quotient
            quotient = dividend / divisor;
            // Computes remainder
            remainder = dividend % divisor;
            printf(\"Quotient = \", quotient);
            printf(\"Remainder = \", remainder);
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test96(self):
        input = """
        void getFibonacii(int a,int b, int n)
        {   
            int sum;
            if(n>0)
            {
                sum=a+b;
                printf(sum);
                a=b;
                b=sum;
                getFibonacii(a,b,n-1);
            }
        }
        int main()
        {
            int a,b,sum,n;
            int i;
     
            a=0;        //first term
            b=1;        //second term
     
            printf(\"Enter total number of terms: \");
            scanf(n);
     
            printf(\"Fibonacii series is : \");
            //print a and b as first and second terms of series
            printf(a,b);
            //call function with (n-2) terms
            getFibonacii(a,b,n-2);
  
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test97(self):
        input = """
        int getPower(int b,int p)
        {
            int result;
            if(p==0)
                return result;
            result=b*(getPower(b,p-1));  //call function again
        }
        int main()
        {
            int base,power;
            int result;
     
            printf(\"Enter value of base: \");
            scanf(base);
     
            printf(\"Enter value of power: \");
            scanf(power);
     
            result=getPower(base,power);
     
            printf(base,power,result);
     
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))
    
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input, expect, 300))
