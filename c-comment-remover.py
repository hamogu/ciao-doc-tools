from __future__ import print_function
import sys, re, os

# for Python 2.7
# Use and modification permitted without limit; credit to NerdFever.com requested.

# thanks to zvoase at http://stackoverflow.com/questions/241327/python-snippet-to-remove-c-and-c-comments
# and Lawrence Johnston at http://stackoverflow.com/questions/1140958/whats-a-quick-one-liner-to-remove-empty-lines-from-a-python-string
def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " " # note: a space and not an empty string
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    
    r1 = re.sub(pattern, replacer, text)
    
    return os.linesep.join([s for s in r1.splitlines() if s.strip()])


def NoComment(infile, outfile):
        
    root, ext = os.path.splitext(infile)
    
    valid = [".c", ".cpp", ".h", ".hpp"]
    
    if ext.lower() in valid:
           
        inf = open(infile, "r")

        dirty = inf.read()
        clean = comment_remover(dirty)

        inf.close()
        
        outf = open(outfile, "wb") # 'b' avoids 0d 0d 0a line endings in Windows
        outf.write(clean)
        outf.close()
        
        print("Comments removed:", infile, ">>>", outfile)
        
    else:

        print("Did nothing:     ", infile)

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("")

        print("C/C++ comment stripper v1.00 (c) 2015 Nerdfever.com")
    
        print("Syntax: nocomments path")

        sys.exit()
        
    root = sys.argv[1]
    
    for root, folders, fns in os.walk(root):

        for fn in fns:
    
            filePath = os.path.join(root, fn)
            NoComment(filePath, filePath)
    
