from mtranslate import translate
import codecs
import sys

wr = codecs.open(str(sys.argv[1])+"-eng.txt", "w", "utf-8")
with open(str(sys.argv[1])+".txt") as i:
    for line in i:
        wr.write(translate(line, "en", "auto"))
        wr.write("\n")
        print(translate(line, "en", "auto"))
    wr.close()
    i.close()
