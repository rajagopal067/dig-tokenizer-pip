import os
import sys
import imp
import pip
import rowTokenizer

def main():
    spark_home = os.getenv("SPARK_HOME")
    cwd_path = os.path.dirname(rowTokenizer.__file__)
    if spark_home is not None:
        filePath = ' --py-files ' + cwd_path + '/tokenizer.zip ' + cwd_path + '/tokenizer.py '
        #print filePath
        args = sys.argv[1:]
        args =  filePath + ' '.join(args)
        os.system("spark-submit " + args)
        #print 'done'
    else:
        print 'please set spark_home home path'
#how about call spark-submit script from here

if __name__ == '__main__':
    main()