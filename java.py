#!/usr/bin/env python3
# ./listBuilder.py ; cat lists.js

def main():
    # UNTIL MACHINE LEARNING MODEL,
    #  THIS WILL HELP RENEW OUR LISTS

    DEV = "testFile.txt"
    # PROD = "lists.java"

    PATH_URLS = "lists/Urls/"
    PATH_KEYWORDS = "lists/Keywords/"

    # w = [over]write, a = append
    outputFile = open(DEV, "w")

    header = "// PorNo!\n"
    header += "// lists.java THIS FILE WAS GENERATED WITH java.py\n"
    header += "// Thank you:\n"
    header += "// https://github.com/ninjayoto/PornList/blob/master/PornList.txt\n"
    header += "// https://github.com/Bon-Appetit/porn-domains/blob/master/domains.txt\n"
    header += "// https://pastebin.com/gpHmA8X5\n"
    header += "// Alexa web ranking service for that good 7-day free trial\n"
    header += "// People who've triggered PorNo!'s capture system\n"
    header += "\n"

    header += "package us.mrvivacio.porno;\n\n"
    header += "import android.util.Log;\n"
    header += "import java.util.HashMap;\n"
    header += "import java.util.Map;\n\n"

    header += "public class Domains {"
    header += """
    \tstatic Map<String, Boolean> dict = new HashMap<String, Boolean>();
    \tstatic String TAG = "!! Domains";

    \tpublic static Map<String, Boolean> init() {
    \t\t// Add lists here, addA() addB() addC() etc
    """

    outputFile.write(header)

    s = "let pornMap={"
    for c in "0123456789abcdefghijklmnopqrstuvwxyz":
        name = PATH_URLS + c + ".txt"
        urls = open(name, "r")

        for url in urls:
            urlWithoutNewLine = "\"" + url[:-1] + "\":!0"
            s += urlWithoutNewLine + ","

    s = s[:-1]
    s += "};\n"

    #outputFile.write(s)

    s = "let bannedWordsList=["
    for c in "abcdefghijklmnopqrstuvwxyz":
        name = PATH_KEYWORDS + c + ".txt"
        urls = open(name, "r")

        for url in urls:
            urlWithoutNewLine = "\"" + url[:-1] + "\""
            s += urlWithoutNewLine + ","

    s = s[:-1]
    s += "];\n"

    #outputFile.write(s)
    outputFile.close()

if (__name__ == "__main__"):
    main()