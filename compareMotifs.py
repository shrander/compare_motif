from Bio import SeqIO
import sys

class Motif:
    def __init__(self):
        #list of promoters in a motif
        self.motif = []
    
    def add_promoter(self, promoter):
        """
        adds a promoter to the motif list
        promoter - string of promoter data
        """
        self.motif.append(promoter):
    
    def remove_promoter(self, promoter):
        """
        remove a promoter from the list
        promoter - string to be removed
        TODO: don't think I will need this.  not implemented
        """
        raise Exception
        
    def __get_object_string(self)
        output = 'This is the list of promtoer in this motif:\n'
        for each in self.motif:
             output+=each+'\n'
        return output
        
    def __unicode__(self):
        return self.__get_object_string()
        
    def __str__(self):
        return unicode(self).encode('utf-8')
        
class app:
    def __init__(self):
        self.motif = Motif()
    
    def usage(self):
        print 'USAGE: hw1-hnatiw.py [options]'
        print '\nThis program takes in a flat txt file corpus and creates a'
        print '   frequency distribution table.'
        print '     -c corpus          File that contains corpus to be scanned'
        print '     -n n-gram size     Depth of the ngram (default: 1=unigram, 2=bigram, etc)'
        #print '     -f [number]        how large of frequency distribution to print out (default: 10)' 
        print '     -l [file]          word list for the frequency distribution. Not specifying a word list'
        print '                         will display the top ten most nGrams'
        print '     -r [number]        create random sentences. [number] is the number of words generated'
        print '                         use the \'-n\' option to modify what depth of ngram to use.'
        print '     -G                 Adds Good-Turing smoothing to the frequency distribution' 
        print '\n'
        sys.exit(0)
        
    def parseArgs(self, args):
        i=0
        try:
            while( i<=len(args)-1 ):
                if args[i] == '-f1' or args[i] == '--fasta-1':
                    i+=1
                    self.fasta_file = args[i]
                if args[i] == '-g' or args[i] == '--genbank':
                    i+=1
                    self.genbank_file = args[i]
                else:
                    print 'ERROR: '+' '.join(sys.argv) + '\n'
                    self.usage()
                i+=1
        except:
            self.usage()
        print '\nCorpus: ' + self.corpus
        print 'n-Gram depth: ' + str(self.n)
        
    def main(self, args):
        self.parse_args(args)


if __name__=='__main__':
    try:
        a=app()
        a.main(sys.argv)
    except Keyboardinterrupt:
        sys.exit(0)