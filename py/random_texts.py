import pickle
import random
import sys
from os.path import exists

def random_text(filepath, size, k):
    """
    Given a result size and an integer k,
    returns a randomly generated text using
    probability distributions of markov chains
    of order k dumped in ../results/distribs/distrib_kX.txt 
    files
    """

    # -- Import file
    try:
        f = open(filepath,'r')
    except IOError as err:
        print err
        exit(2)

    # -- Initial string
    if k != 0:
        initial_string = ' '.join(f.readlines())[:k]
    else:
        initial_string = ' '.join(f.readlines())[:1]
    out = initial_string
    f.close()
    
    # -- Import probability distribution
    try:
        p = open('../results/distribs/distrib_k%d.txt'%(k),'r')
    except IOError as err:
        print err
        exit(2)
        
    distrib_matrix = pickle.load(p)
    p.close()

    # -- Generate text following probability distribution
    kuple = initial_string
    for x in xrange(size):
        p = random.uniform(0,1)

        i = 0
        char = ''
        if k!=0:
            dist = distrib_matrix[kuple] # read distribution specific to k-uple string
        else:
            dist = distrib_matrix['']
        for symbol in dist:
            char = symbol
            i = dist[symbol]
            if i > p:
                break # found symbol
    
        out += symbol
        kuple = kuple[1:]+symbol # update k-uple 
        
    return out


if __name__=='__main__':
    
    EXIT_MSG = 'The program will now end.'

    if len(sys.argv) > 1:
        try:
            filepath = sys.argv[1]
        except:
            print '%s: %s' %(sys.exc_type, sys.exc_value)
            print EXIT_MSG
            exit(2)
            
        if len(sys.argv) > 2:    
            try:
                len_text = int(sys.argv[2])
            except:
                print '%s: %s' %(sys.exc_type, sys.exc_value)
                print EXIT_MSG
                exit(2)
        else:
            print 'Default length value 100 taken.' 
            len_text = 100
            
        if exists(filepath):
            k_list = [10]
            for k in k_list:
                print 'k = %d' % k
                print random_text(filepath, len_text, k) + '\n'
        else:
            print 'Error: the given path %s leads to no existing file.' %(filepath)
            print EXIT_MSG
            exit(2)
                            
    else:
        print 'Need file path leading to source text.'
        print EXIT_MSG
        exit(2)
