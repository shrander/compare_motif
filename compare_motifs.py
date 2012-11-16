from Bio import SeqIO
from Bio import AlignIO
import sys

class Motif:
    def __init__(self, fasta_file):
        # file name from which the fasta info was generated
        self.fasta_file = fasta_file
        #list of promoters in a motif
        self.motif = []
    
    def add_promoter(self, promoter):
        """
        adds a promoter to the motif list
        promoter - sequence object from SeqIO
        """
        self.motif.append(promoter)
    
    def remove_promoter(self, promoter):
        """
        remove a promoter from the list
        promoter - sequence object from SeqIO
        TODO: don't think I will need this.  not implemented
        """
        raise Exception('Function not Implemented')
        
    def _get_object_string(self)
        """
        builds a string output representation of the the Motif object
        """
        output = 'This is the list of promtore in this motif:\n'
        output += '\n'
        output += "The motif was generated from " + self.fasta_file +"\n'
        for each in self.motif:
             output+=str(each)+'\n'
        return output
        
    def __unicode__(self):
        return self._get_object_string()
        
    def __str__(self):
        return unicode(self).encode('utf-8')
        
class DNA:
    def __init__(self, genbank_file):
        #file name from which the genbank data was derived
        self.genbank_file = genbank_file
        #list of sequences
        self.sequence = []
        for each in SeqIO.parse(genbank_file, "genbank"):
            self.add_sequence(each)
            
    def add_sequence(self, sequence):
        """
        adds a sequence object to the sequnce list
        sequence - sequence object from SeqIO
        """
        self.sequence.append(sequence)
      
    def remove_sequence(self, sequence):
        """
        remove a sequence from the list
        sequence - sequence object from SeqIO
        TODO: not implemented.  don't think I will need this
        """
        raise Exception('Function not implemented')
        
    def _get_object_string(self)
        """
        builds a string output representation of the the Motif object
        """
        output = ''
        for each in self.sequence:
            output += str(each)
        return output
        
    def __unicode__(self):
        return self._get_object_string()
        
    def __str__(self):
        return unicode(self).encode('utf-8')
        
class app:
    def __init__(self):
        self.motif1 = None
        self.motif2 = None
        self.seq_data = None
        self.m1_file = ''
        self.m2_file = ''
        self.genbank_file = ''
    
    def usage(self):
        print 'USAGE: compareMotif.py [options]'
        print 'An explanation of the program'
        print '     -m1 [fasta_file]             File that contains the motif information (Fasta format)'
        print '     -m2 [fasta_file]             File that contains the motif information (Fasta format)'
        print '     -g [genbank_file]       File that contains the genbank information (genbank format)'
        print '\n'
        sys.exit(0)

    def parse_motifs(self):
        pssm_tmp = {'A':[],'C':[],'G':[],'T':[]}
        for key in pssm.get_keys():
            pssm_tmp[key] = [0]*len(self.motif1)

        pssm1 = pssm_tmp
        i=0
        while(i<len(self.motif1)):
            pssm1[self.motif1[i]][i]+=1
            i+=1
            
        pssm2 = pssm_tmp
        i=0
        while(i<len(self.motif2)):
            pssm2[self.motif2[i]][i]+=1
            i+=1
            
    def parse_motifs_with_background(self):
        raise Exception('Function not implemented')
        
    def parse_args(self, args):
        i=0
        try:
            while( i<=len(args)-1 ):
                if args[i] == '-m1':
                    i+=1
                    self.m1_file = args[i]
                elif args[i] == '-m2':
                    i+=1
                    self.m2_file = args[i]
                elif args[i] == '-g' or args[i] == '--genbank':
                    i+=1
                    self.genbank_file = args[i]
                else:
                    raise Exception('Arg parsing error')
                i+=1
        except:
            print 'ERROR: '+' '.join(sys.argv) + '\n'
            self.usage()
        
    def initialize_data(self):
        self.motif1 = Motif(self.m1_file)
        motif = open(self.m1_file, 'r')
        for each in AlignIO.parse(fasta, "fasta")
            self.motif1.add_promoter(each)
        motif.close()
        
        self.motif2 = Motif(self.m2_file)
        motif = open(self.m2_file, 'r')
        for each in AlignIO.parse(fasta, "fasta")
            self.motif2.add_promoter(each)
        motif.close()
        
        self.seq_data = DNA(self.genbank_file)
        
    def main(self, args):
        self.parse_args(args)
        self.initialize_data()
        if genbank_file == '':
            self.parse_motifs()
        else:
            self.parse_motifs_with_background()

if __name__=='__main__':
    try:
        a=app()
        a.main(sys.argv)
    except KeyboardInterrupt:
        sys.exit(0)