#!/usr/bin/python

import sys, getopt
from icu import Transliterator

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'zg-my.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
         outputfile = "converted_" + inputfile
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   print 'Input file is ', inputfile
   print 'Output file is ', outputfile

   uni = Transliterator.createInstance('Zawgyi-my')

   f = open(inputfile, "r")

   converted = uni.transliterate(f.read())

   f.close()

   fo = open(outputfile, "w")
   fo.write(converted.encode('utf8'))
   fo.close()

if __name__ == "__main__":
   main(sys.argv[1:])
