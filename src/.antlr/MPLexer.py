# Generated from c:\Users\Administrator\Documents\191\PPL\assignment2\initial\src\mp.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u0257\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\34\7\34")
        buf.write("\u00f8\n\34\f\34\16\34\u00fb\13\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\7\35\u0104\n\35\f\35\16\35\u0107\13\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\7\36\u0111\n")
        buf.write("\36\f\36\16\36\u0114\13\36\3\36\3\36\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3")
        buf.write("&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write(")\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3.\3")
        buf.write(".\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3<\3<\3")
        buf.write("=\3=\3=\3=\3>\3>\3>\3?\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3")
        buf.write("C\3D\3D\3D\3E\3E\3E\3E\3F\3F\3F\3F\3G\3G\3H\3H\3I\3I\3")
        buf.write("J\3J\3K\3K\3L\3L\3L\3M\3M\3M\3M\3M\3N\3N\3O\3O\3P\3P\3")
        buf.write("P\3Q\6Q\u01f2\nQ\rQ\16Q\u01f3\3R\3R\5R\u01f8\nR\3R\6R")
        buf.write("\u01fb\nR\rR\16R\u01fc\3R\5R\u0200\nR\3S\5S\u0203\nS\3")
        buf.write("S\3S\3S\3S\3S\5S\u020a\nS\3T\3T\5T\u020e\nT\3T\3T\3U\3")
        buf.write("U\3V\3V\5V\u0216\nV\3W\3W\3W\3W\3W\3X\3X\3X\3X\3X\3X\3")
        buf.write("Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\5Y\u0233")
        buf.write("\nY\3Z\3Z\3Z\7Z\u0238\nZ\fZ\16Z\u023b\13Z\3Z\3Z\3[\3[")
        buf.write("\3[\3[\3\\\3\\\3\\\3\\\3]\3]\7]\u0249\n]\f]\16]\u024c")
        buf.write("\13]\3^\6^\u024f\n^\r^\16^\u0250\3^\3^\3_\3_\3_\4\u00f9")
        buf.write("\u0105\2`\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2")
        buf.write("\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61")
        buf.write("\2\63\2\65\2\67\39\4;\5=\6?\7A\bC\tE\nG\13I\fK\rM\16O")
        buf.write("\17Q\20S\21U\22W\23Y\24[\25]\26_\27a\30c\31e\32g\33i\34")
        buf.write("k\35m\36o\37q s!u\"w#y${%}&\177\'\u0081(\u0083)\u0085")
        buf.write("*\u0087+\u0089,\u008b-\u008d.\u008f/\u0091\60\u0093\61")
        buf.write("\u0095\62\u0097\63\u0099\64\u009b\65\u009d\66\u009f\67")
        buf.write("\u00a18\u00a39\u00a5\2\u00a7\2\u00a9\2\u00ab:\u00ad;\u00af")
        buf.write("<\u00b1\2\u00b3=\u00b5>\u00b7?\u00b9@\u00bbA\u00bdB\3")
        buf.write("\2#\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4")
        buf.write("\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOo")
        buf.write("o\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2")
        buf.write("VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\|")
        buf.write("|\4\2\f\f\17\17\3\2\62;\7\2\n\f\16\17$$))^^\6\2\n\13\16")
        buf.write("\16))^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2")
        buf.write("\u024e\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2")
        buf.write("\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b3")
        buf.write("\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2")
        buf.write("\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2\2\3\u00bf\3\2\2\2\5\u00c1")
        buf.write("\3\2\2\2\7\u00c3\3\2\2\2\t\u00c5\3\2\2\2\13\u00c7\3\2")
        buf.write("\2\2\r\u00c9\3\2\2\2\17\u00cb\3\2\2\2\21\u00cd\3\2\2\2")
        buf.write("\23\u00cf\3\2\2\2\25\u00d1\3\2\2\2\27\u00d3\3\2\2\2\31")
        buf.write("\u00d5\3\2\2\2\33\u00d7\3\2\2\2\35\u00d9\3\2\2\2\37\u00db")
        buf.write("\3\2\2\2!\u00dd\3\2\2\2#\u00df\3\2\2\2%\u00e1\3\2\2\2")
        buf.write("\'\u00e3\3\2\2\2)\u00e5\3\2\2\2+\u00e7\3\2\2\2-\u00e9")
        buf.write("\3\2\2\2/\u00eb\3\2\2\2\61\u00ed\3\2\2\2\63\u00ef\3\2")
        buf.write("\2\2\65\u00f1\3\2\2\2\67\u00f3\3\2\2\29\u0101\3\2\2\2")
        buf.write(";\u010c\3\2\2\2=\u0117\3\2\2\2?\u011d\3\2\2\2A\u0126\3")
        buf.write("\2\2\2C\u012a\3\2\2\2E\u012d\3\2\2\2G\u0134\3\2\2\2I\u0137")
        buf.write("\3\2\2\2K\u013a\3\2\2\2M\u013f\3\2\2\2O\u0144\3\2\2\2")
        buf.write("Q\u014b\3\2\2\2S\u0151\3\2\2\2U\u0157\3\2\2\2W\u015b\3")
        buf.write("\2\2\2Y\u0164\3\2\2\2[\u016e\3\2\2\2]\u0172\3\2\2\2_\u0178")
        buf.write("\3\2\2\2a\u0181\3\2\2\2c\u0189\3\2\2\2e\u018c\3\2\2\2")
        buf.write("g\u0191\3\2\2\2i\u0199\3\2\2\2k\u01a1\3\2\2\2m\u01a8\3")
        buf.write("\2\2\2o\u01ad\3\2\2\2q\u01af\3\2\2\2s\u01b1\3\2\2\2u\u01b3")
        buf.write("\3\2\2\2w\u01b5\3\2\2\2y\u01b9\3\2\2\2{\u01bd\3\2\2\2")
        buf.write("}\u01c0\3\2\2\2\177\u01c3\3\2\2\2\u0081\u01c5\3\2\2\2")
        buf.write("\u0083\u01c7\3\2\2\2\u0085\u01c9\3\2\2\2\u0087\u01cc\3")
        buf.write("\2\2\2\u0089\u01cf\3\2\2\2\u008b\u01d3\3\2\2\2\u008d\u01d7")
        buf.write("\3\2\2\2\u008f\u01d9\3\2\2\2\u0091\u01db\3\2\2\2\u0093")
        buf.write("\u01dd\3\2\2\2\u0095\u01df\3\2\2\2\u0097\u01e1\3\2\2\2")
        buf.write("\u0099\u01e4\3\2\2\2\u009b\u01e9\3\2\2\2\u009d\u01eb\3")
        buf.write("\2\2\2\u009f\u01ed\3\2\2\2\u00a1\u01f1\3\2\2\2\u00a3\u01ff")
        buf.write("\3\2\2\2\u00a5\u0209\3\2\2\2\u00a7\u020b\3\2\2\2\u00a9")
        buf.write("\u0211\3\2\2\2\u00ab\u0215\3\2\2\2\u00ad\u0217\3\2\2\2")
        buf.write("\u00af\u021c\3\2\2\2\u00b1\u0232\3\2\2\2\u00b3\u0234\3")
        buf.write("\2\2\2\u00b5\u023e\3\2\2\2\u00b7\u0242\3\2\2\2\u00b9\u0246")
        buf.write("\3\2\2\2\u00bb\u024e\3\2\2\2\u00bd\u0254\3\2\2\2\u00bf")
        buf.write("\u00c0\t\2\2\2\u00c0\4\3\2\2\2\u00c1\u00c2\t\3\2\2\u00c2")
        buf.write("\6\3\2\2\2\u00c3\u00c4\t\4\2\2\u00c4\b\3\2\2\2\u00c5\u00c6")
        buf.write("\t\5\2\2\u00c6\n\3\2\2\2\u00c7\u00c8\t\6\2\2\u00c8\f\3")
        buf.write("\2\2\2\u00c9\u00ca\t\7\2\2\u00ca\16\3\2\2\2\u00cb\u00cc")
        buf.write("\t\b\2\2\u00cc\20\3\2\2\2\u00cd\u00ce\t\t\2\2\u00ce\22")
        buf.write("\3\2\2\2\u00cf\u00d0\t\n\2\2\u00d0\24\3\2\2\2\u00d1\u00d2")
        buf.write("\t\13\2\2\u00d2\26\3\2\2\2\u00d3\u00d4\t\f\2\2\u00d4\30")
        buf.write("\3\2\2\2\u00d5\u00d6\t\r\2\2\u00d6\32\3\2\2\2\u00d7\u00d8")
        buf.write("\t\16\2\2\u00d8\34\3\2\2\2\u00d9\u00da\t\17\2\2\u00da")
        buf.write("\36\3\2\2\2\u00db\u00dc\t\20\2\2\u00dc \3\2\2\2\u00dd")
        buf.write("\u00de\t\21\2\2\u00de\"\3\2\2\2\u00df\u00e0\t\22\2\2\u00e0")
        buf.write("$\3\2\2\2\u00e1\u00e2\t\23\2\2\u00e2&\3\2\2\2\u00e3\u00e4")
        buf.write("\t\24\2\2\u00e4(\3\2\2\2\u00e5\u00e6\t\25\2\2\u00e6*\3")
        buf.write("\2\2\2\u00e7\u00e8\t\26\2\2\u00e8,\3\2\2\2\u00e9\u00ea")
        buf.write("\t\27\2\2\u00ea.\3\2\2\2\u00eb\u00ec\t\30\2\2\u00ec\60")
        buf.write("\3\2\2\2\u00ed\u00ee\t\31\2\2\u00ee\62\3\2\2\2\u00ef\u00f0")
        buf.write("\t\32\2\2\u00f0\64\3\2\2\2\u00f1\u00f2\t\33\2\2\u00f2")
        buf.write("\66\3\2\2\2\u00f3\u00f4\7*\2\2\u00f4\u00f5\7,\2\2\u00f5")
        buf.write("\u00f9\3\2\2\2\u00f6\u00f8\13\2\2\2\u00f7\u00f6\3\2\2")
        buf.write("\2\u00f8\u00fb\3\2\2\2\u00f9\u00fa\3\2\2\2\u00f9\u00f7")
        buf.write("\3\2\2\2\u00fa\u00fc\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc")
        buf.write("\u00fd\7,\2\2\u00fd\u00fe\7+\2\2\u00fe\u00ff\3\2\2\2\u00ff")
        buf.write("\u0100\b\34\2\2\u01008\3\2\2\2\u0101\u0105\7}\2\2\u0102")
        buf.write("\u0104\13\2\2\2\u0103\u0102\3\2\2\2\u0104\u0107\3\2\2")
        buf.write("\2\u0105\u0106\3\2\2\2\u0105\u0103\3\2\2\2\u0106\u0108")
        buf.write("\3\2\2\2\u0107\u0105\3\2\2\2\u0108\u0109\7\177\2\2\u0109")
        buf.write("\u010a\3\2\2\2\u010a\u010b\b\35\2\2\u010b:\3\2\2\2\u010c")
        buf.write("\u010d\7\61\2\2\u010d\u010e\7\61\2\2\u010e\u0112\3\2\2")
        buf.write("\2\u010f\u0111\n\34\2\2\u0110\u010f\3\2\2\2\u0111\u0114")
        buf.write("\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113")
        buf.write("\u0115\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u0116\b\36\2")
        buf.write("\2\u0116<\3\2\2\2\u0117\u0118\5\5\3\2\u0118\u0119\5%\23")
        buf.write("\2\u0119\u011a\5\13\6\2\u011a\u011b\5\3\2\2\u011b\u011c")
        buf.write("\5\27\f\2\u011c>\3\2\2\2\u011d\u011e\5\7\4\2\u011e\u011f")
        buf.write("\5\37\20\2\u011f\u0120\5\35\17\2\u0120\u0121\5)\25\2\u0121")
        buf.write("\u0122\5\23\n\2\u0122\u0123\5\35\17\2\u0123\u0124\5+\26")
        buf.write("\2\u0124\u0125\5\13\6\2\u0125@\3\2\2\2\u0126\u0127\5\r")
        buf.write("\7\2\u0127\u0128\5\37\20\2\u0128\u0129\5%\23\2\u0129B")
        buf.write("\3\2\2\2\u012a\u012b\5)\25\2\u012b\u012c\5\37\20\2\u012c")
        buf.write("D\3\2\2\2\u012d\u012e\5\t\5\2\u012e\u012f\5\37\20\2\u012f")
        buf.write("\u0130\5/\30\2\u0130\u0131\5\35\17\2\u0131\u0132\5)\25")
        buf.write("\2\u0132\u0133\5\37\20\2\u0133F\3\2\2\2\u0134\u0135\5")
        buf.write("\t\5\2\u0135\u0136\5\37\20\2\u0136H\3\2\2\2\u0137\u0138")
        buf.write("\5\23\n\2\u0138\u0139\5\r\7\2\u0139J\3\2\2\2\u013a\u013b")
        buf.write("\5)\25\2\u013b\u013c\5\21\t\2\u013c\u013d\5\13\6\2\u013d")
        buf.write("\u013e\5\35\17\2\u013eL\3\2\2\2\u013f\u0140\5\13\6\2\u0140")
        buf.write("\u0141\5\31\r\2\u0141\u0142\5\'\24\2\u0142\u0143\5\13")
        buf.write("\6\2\u0143N\3\2\2\2\u0144\u0145\5%\23\2\u0145\u0146\5")
        buf.write("\13\6\2\u0146\u0147\5)\25\2\u0147\u0148\5+\26\2\u0148")
        buf.write("\u0149\5%\23\2\u0149\u014a\5\35\17\2\u014aP\3\2\2\2\u014b")
        buf.write("\u014c\5/\30\2\u014c\u014d\5\21\t\2\u014d\u014e\5\23\n")
        buf.write("\2\u014e\u014f\5\31\r\2\u014f\u0150\5\13\6\2\u0150R\3")
        buf.write("\2\2\2\u0151\u0152\5\5\3\2\u0152\u0153\5\13\6\2\u0153")
        buf.write("\u0154\5\17\b\2\u0154\u0155\5\23\n\2\u0155\u0156\5\35")
        buf.write("\17\2\u0156T\3\2\2\2\u0157\u0158\5\13\6\2\u0158\u0159")
        buf.write("\5\35\17\2\u0159\u015a\5\t\5\2\u015aV\3\2\2\2\u015b\u015c")
        buf.write("\5\r\7\2\u015c\u015d\5+\26\2\u015d\u015e\5\35\17\2\u015e")
        buf.write("\u015f\5\7\4\2\u015f\u0160\5)\25\2\u0160\u0161\5\23\n")
        buf.write("\2\u0161\u0162\5\37\20\2\u0162\u0163\5\35\17\2\u0163X")
        buf.write("\3\2\2\2\u0164\u0165\5!\21\2\u0165\u0166\5%\23\2\u0166")
        buf.write("\u0167\5\37\20\2\u0167\u0168\5\7\4\2\u0168\u0169\5\13")
        buf.write("\6\2\u0169\u016a\5\t\5\2\u016a\u016b\5+\26\2\u016b\u016c")
        buf.write("\5%\23\2\u016c\u016d\5\13\6\2\u016dZ\3\2\2\2\u016e\u016f")
        buf.write("\5-\27\2\u016f\u0170\5\3\2\2\u0170\u0171\5%\23\2\u0171")
        buf.write("\\\3\2\2\2\u0172\u0173\5\3\2\2\u0173\u0174\5%\23\2\u0174")
        buf.write("\u0175\5%\23\2\u0175\u0176\5\3\2\2\u0176\u0177\5\63\32")
        buf.write("\2\u0177^\3\2\2\2\u0178\u0179\5\3\2\2\u0179\u017a\5\35")
        buf.write("\17\2\u017a\u017b\5\t\5\2\u017b\u017c\7\"\2\2\u017c\u017d")
        buf.write("\5)\25\2\u017d\u017e\5\21\t\2\u017e\u017f\5\13\6\2\u017f")
        buf.write("\u0180\5\35\17\2\u0180`\3\2\2\2\u0181\u0182\5\37\20\2")
        buf.write("\u0182\u0183\5%\23\2\u0183\u0184\7\"\2\2\u0184\u0185\5")
        buf.write("\13\6\2\u0185\u0186\5\31\r\2\u0186\u0187\5\'\24\2\u0187")
        buf.write("\u0188\5\13\6\2\u0188b\3\2\2\2\u0189\u018a\5\37\20\2\u018a")
        buf.write("\u018b\5\r\7\2\u018bd\3\2\2\2\u018c\u018d\5%\23\2\u018d")
        buf.write("\u018e\5\13\6\2\u018e\u018f\5\3\2\2\u018f\u0190\5\31\r")
        buf.write("\2\u0190f\3\2\2\2\u0191\u0192\5\5\3\2\u0192\u0193\5\37")
        buf.write("\20\2\u0193\u0194\5\37\20\2\u0194\u0195\5\31\r\2\u0195")
        buf.write("\u0196\5\13\6\2\u0196\u0197\5\3\2\2\u0197\u0198\5\35\17")
        buf.write("\2\u0198h\3\2\2\2\u0199\u019a\5\23\n\2\u019a\u019b\5\35")
        buf.write("\17\2\u019b\u019c\5)\25\2\u019c\u019d\5\13\6\2\u019d\u019e")
        buf.write("\5\17\b\2\u019e\u019f\5\13\6\2\u019f\u01a0\5%\23\2\u01a0")
        buf.write("j\3\2\2\2\u01a1\u01a2\5\'\24\2\u01a2\u01a3\5)\25\2\u01a3")
        buf.write("\u01a4\5%\23\2\u01a4\u01a5\5\23\n\2\u01a5\u01a6\5\35\17")
        buf.write("\2\u01a6\u01a7\5\17\b\2\u01a7l\3\2\2\2\u01a8\u01a9\5/")
        buf.write("\30\2\u01a9\u01aa\5\23\n\2\u01aa\u01ab\5)\25\2\u01ab\u01ac")
        buf.write("\5\21\t\2\u01acn\3\2\2\2\u01ad\u01ae\7-\2\2\u01aep\3\2")
        buf.write("\2\2\u01af\u01b0\7/\2\2\u01b0r\3\2\2\2\u01b1\u01b2\7,")
        buf.write("\2\2\u01b2t\3\2\2\2\u01b3\u01b4\7\61\2\2\u01b4v\3\2\2")
        buf.write("\2\u01b5\u01b6\5\35\17\2\u01b6\u01b7\5\37\20\2\u01b7\u01b8")
        buf.write("\5)\25\2\u01b8x\3\2\2\2\u01b9\u01ba\5\3\2\2\u01ba\u01bb")
        buf.write("\5\35\17\2\u01bb\u01bc\5\t\5\2\u01bcz\3\2\2\2\u01bd\u01be")
        buf.write("\5\37\20\2\u01be\u01bf\5%\23\2\u01bf|\3\2\2\2\u01c0\u01c1")
        buf.write("\7>\2\2\u01c1\u01c2\7@\2\2\u01c2~\3\2\2\2\u01c3\u01c4")
        buf.write("\7?\2\2\u01c4\u0080\3\2\2\2\u01c5\u01c6\7>\2\2\u01c6\u0082")
        buf.write("\3\2\2\2\u01c7\u01c8\7@\2\2\u01c8\u0084\3\2\2\2\u01c9")
        buf.write("\u01ca\7>\2\2\u01ca\u01cb\7?\2\2\u01cb\u0086\3\2\2\2\u01cc")
        buf.write("\u01cd\7@\2\2\u01cd\u01ce\7?\2\2\u01ce\u0088\3\2\2\2\u01cf")
        buf.write("\u01d0\5\t\5\2\u01d0\u01d1\5\23\n\2\u01d1\u01d2\5-\27")
        buf.write("\2\u01d2\u008a\3\2\2\2\u01d3\u01d4\5\33\16\2\u01d4\u01d5")
        buf.write("\5\37\20\2\u01d5\u01d6\5\t\5\2\u01d6\u008c\3\2\2\2\u01d7")
        buf.write("\u01d8\7]\2\2\u01d8\u008e\3\2\2\2\u01d9\u01da\7_\2\2\u01da")
        buf.write("\u0090\3\2\2\2\u01db\u01dc\7*\2\2\u01dc\u0092\3\2\2\2")
        buf.write("\u01dd\u01de\7+\2\2\u01de\u0094\3\2\2\2\u01df\u01e0\7")
        buf.write("=\2\2\u01e0\u0096\3\2\2\2\u01e1\u01e2\7\60\2\2\u01e2\u01e3")
        buf.write("\7\60\2\2\u01e3\u0098\3\2\2\2\u01e4\u01e5\7\"\2\2\u01e5")
        buf.write("\u01e6\7\60\2\2\u01e6\u01e7\7\60\2\2\u01e7\u01e8\7\"\2")
        buf.write("\2\u01e8\u009a\3\2\2\2\u01e9\u01ea\7.\2\2\u01ea\u009c")
        buf.write("\3\2\2\2\u01eb\u01ec\7<\2\2\u01ec\u009e\3\2\2\2\u01ed")
        buf.write("\u01ee\7<\2\2\u01ee\u01ef\7?\2\2\u01ef\u00a0\3\2\2\2\u01f0")
        buf.write("\u01f2\t\35\2\2\u01f1\u01f0\3\2\2\2\u01f2\u01f3\3\2\2")
        buf.write("\2\u01f3\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u00a2")
        buf.write("\3\2\2\2\u01f5\u01f7\5\u00a5S\2\u01f6\u01f8\5\u00a7T\2")
        buf.write("\u01f7\u01f6\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u0200\3")
        buf.write("\2\2\2\u01f9\u01fb\t\35\2\2\u01fa\u01f9\3\2\2\2\u01fb")
        buf.write("\u01fc\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fc\u01fd\3\2\2\2")
        buf.write("\u01fd\u01fe\3\2\2\2\u01fe\u0200\5\u00a7T\2\u01ff\u01f5")
        buf.write("\3\2\2\2\u01ff\u01fa\3\2\2\2\u0200\u00a4\3\2\2\2\u0201")
        buf.write("\u0203\5\u00a1Q\2\u0202\u0201\3\2\2\2\u0202\u0203\3\2")
        buf.write("\2\2\u0203\u0204\3\2\2\2\u0204\u0205\7\60\2\2\u0205\u020a")
        buf.write("\5\u00a1Q\2\u0206\u0207\5\u00a1Q\2\u0207\u0208\7\60\2")
        buf.write("\2\u0208\u020a\3\2\2\2\u0209\u0202\3\2\2\2\u0209\u0206")
        buf.write("\3\2\2\2\u020a\u00a6\3\2\2\2\u020b\u020d\5\13\6\2\u020c")
        buf.write("\u020e\5\u00a9U\2\u020d\u020c\3\2\2\2\u020d\u020e\3\2")
        buf.write("\2\2\u020e\u020f\3\2\2\2\u020f\u0210\5\u00a1Q\2\u0210")
        buf.write("\u00a8\3\2\2\2\u0211\u0212\7/\2\2\u0212\u00aa\3\2\2\2")
        buf.write("\u0213\u0216\5\u00adW\2\u0214\u0216\5\u00afX\2\u0215\u0213")
        buf.write("\3\2\2\2\u0215\u0214\3\2\2\2\u0216\u00ac\3\2\2\2\u0217")
        buf.write("\u0218\5)\25\2\u0218\u0219\5%\23\2\u0219\u021a\5+\26\2")
        buf.write("\u021a\u021b\5\13\6\2\u021b\u00ae\3\2\2\2\u021c\u021d")
        buf.write("\5\r\7\2\u021d\u021e\5\3\2\2\u021e\u021f\5\31\r\2\u021f")
        buf.write("\u0220\5\'\24\2\u0220\u0221\5\13\6\2\u0221\u00b0\3\2\2")
        buf.write("\2\u0222\u0223\7^\2\2\u0223\u0233\7d\2\2\u0224\u0225\7")
        buf.write("^\2\2\u0225\u0233\7h\2\2\u0226\u0227\7^\2\2\u0227\u0233")
        buf.write("\7t\2\2\u0228\u0229\7^\2\2\u0229\u0233\7p\2\2\u022a\u022b")
        buf.write("\7^\2\2\u022b\u0233\7v\2\2\u022c\u022d\7^\2\2\u022d\u0233")
        buf.write("\7)\2\2\u022e\u022f\7^\2\2\u022f\u0233\7$\2\2\u0230\u0231")
        buf.write("\7^\2\2\u0231\u0233\7^\2\2\u0232\u0222\3\2\2\2\u0232\u0224")
        buf.write("\3\2\2\2\u0232\u0226\3\2\2\2\u0232\u0228\3\2\2\2\u0232")
        buf.write("\u022a\3\2\2\2\u0232\u022c\3\2\2\2\u0232\u022e\3\2\2\2")
        buf.write("\u0232\u0230\3\2\2\2\u0233\u00b2\3\2\2\2\u0234\u0239\7")
        buf.write("$\2\2\u0235\u0238\n\36\2\2\u0236\u0238\5\u00b1Y\2\u0237")
        buf.write("\u0235\3\2\2\2\u0237\u0236\3\2\2\2\u0238\u023b\3\2\2\2")
        buf.write("\u0239\u0237\3\2\2\2\u0239\u023a\3\2\2\2\u023a\u023c\3")
        buf.write("\2\2\2\u023b\u0239\3\2\2\2\u023c\u023d\bZ\3\2\u023d\u00b4")
        buf.write("\3\2\2\2\u023e\u023f\5\u00b3Z\2\u023f\u0240\t\37\2\2\u0240")
        buf.write("\u0241\b[\4\2\u0241\u00b6\3\2\2\2\u0242\u0243\5\u00b3")
        buf.write("Z\2\u0243\u0244\7$\2\2\u0244\u0245\b\\\5\2\u0245\u00b8")
        buf.write("\3\2\2\2\u0246\u024a\t \2\2\u0247\u0249\t!\2\2\u0248\u0247")
        buf.write("\3\2\2\2\u0249\u024c\3\2\2\2\u024a\u0248\3\2\2\2\u024a")
        buf.write("\u024b\3\2\2\2\u024b\u00ba\3\2\2\2\u024c\u024a\3\2\2\2")
        buf.write("\u024d\u024f\t\"\2\2\u024e\u024d\3\2\2\2\u024f\u0250\3")
        buf.write("\2\2\2\u0250\u024e\3\2\2\2\u0250\u0251\3\2\2\2\u0251\u0252")
        buf.write("\3\2\2\2\u0252\u0253\b^\2\2\u0253\u00bc\3\2\2\2\u0254")
        buf.write("\u0255\13\2\2\2\u0255\u0256\b_\6\2\u0256\u00be\3\2\2\2")
        buf.write("\23\2\u00f9\u0105\u0112\u01f3\u01f7\u01fc\u01ff\u0202")
        buf.write("\u0209\u020d\u0215\u0232\u0237\u0239\u024a\u0250\7\b\2")
        buf.write("\2\3Z\2\3[\3\3\\\4\3_\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT_1 = 1
    COMMENT_2 = 2
    COMENT_3 = 3
    BREAK = 4
    CONTINUE = 5
    FOR = 6
    TO = 7
    DOWNTO = 8
    DO = 9
    IF = 10
    THEN = 11
    ELSE = 12
    RETURN = 13
    WHILE = 14
    BEGIN = 15
    END = 16
    FUNCTION = 17
    PROCEDURE = 18
    VAR = 19
    ARRAY = 20
    ANDTHEN = 21
    ORELSE = 22
    OF = 23
    REAL = 24
    BOOLEAN = 25
    INTEGER = 26
    STRING = 27
    WITH = 28
    ADD = 29
    SUB = 30
    MULTIPLICATION = 31
    DIVISION = 32
    NOT = 33
    AND = 34
    OR = 35
    NOT_EQUAL = 36
    EQUAL = 37
    LESS_THAN = 38
    GREATER_THAN = 39
    LESS_THAN_EQUAL = 40
    GREATER_THAN_EQUAL = 41
    DIV = 42
    MOD = 43
    LSB = 44
    RSB = 45
    LB = 46
    RB = 47
    SEMI = 48
    DD = 49
    DD2 = 50
    COMMA = 51
    COLON = 52
    ASSIGN = 53
    INTLIT = 54
    FLOATLIT = 55
    BOOL_LIT = 56
    TRUE = 57
    FALSE = 58
    UNCLOSE_STRING = 59
    ILLEGAL_ESCAPE = 60
    STRING_LIT = 61
    ID = 62
    WS = 63
    ERROR_CHAR = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'<>'", "'='", "'<'", "'>'", "'<='", 
            "'>='", "'['", "']'", "'('", "')'", "';'", "'..'", "' .. '", 
            "','", "':'", "':='" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT_1", "COMMENT_2", "COMENT_3", "BREAK", "CONTINUE", "FOR", 
            "TO", "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURN", "WHILE", 
            "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", "ARRAY", "ANDTHEN", 
            "ORELSE", "OF", "REAL", "BOOLEAN", "INTEGER", "STRING", "WITH", 
            "ADD", "SUB", "MULTIPLICATION", "DIVISION", "NOT", "AND", "OR", 
            "NOT_EQUAL", "EQUAL", "LESS_THAN", "GREATER_THAN", "LESS_THAN_EQUAL", 
            "GREATER_THAN_EQUAL", "DIV", "MOD", "LSB", "RSB", "LB", "RB", 
            "SEMI", "DD", "DD2", "COMMA", "COLON", "ASSIGN", "INTLIT", "FLOATLIT", 
            "BOOL_LIT", "TRUE", "FALSE", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "STRING_LIT", "ID", "WS", "ERROR_CHAR" ]

    ruleNames = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z", "COMMENT_1", "COMMENT_2", "COMENT_3", 
                  "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", 
                  "THEN", "ELSE", "RETURN", "WHILE", "BEGIN", "END", "FUNCTION", 
                  "PROCEDURE", "VAR", "ARRAY", "ANDTHEN", "ORELSE", "OF", 
                  "REAL", "BOOLEAN", "INTEGER", "STRING", "WITH", "ADD", 
                  "SUB", "MULTIPLICATION", "DIVISION", "NOT", "AND", "OR", 
                  "NOT_EQUAL", "EQUAL", "LESS_THAN", "GREATER_THAN", "LESS_THAN_EQUAL", 
                  "GREATER_THAN_EQUAL", "DIV", "MOD", "LSB", "RSB", "LB", 
                  "RB", "SEMI", "DD", "DD2", "COMMA", "COLON", "ASSIGN", 
                  "INTLIT", "FLOATLIT", "FRACPART", "EXPOPART", "SIGN", 
                  "BOOL_LIT", "TRUE", "FALSE", "LEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "STRING_LIT", "ID", "WS", "ERROR_CHAR" ]

    grammarFileName = "mp.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[88] = self.UNCLOSE_STRING_action 
            actions[89] = self.ILLEGAL_ESCAPE_action 
            actions[90] = self.STRING_LIT_action 
            actions[93] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             raise IllegalEscape(self.text[1:])
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


