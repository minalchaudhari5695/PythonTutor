__author__='minal'
def file_open():
    fout=open('outputfile.txt','w')
    print fout
    sample_string='sample string for writing\n'
    fout.write(sample_string)
    fout.close()
if __name__=='main':
    file_open()