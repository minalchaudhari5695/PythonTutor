__author__='minal'
import threading
def do_this():
    global dead
    x=0
    print 'printing in do this function'
    while (not dead):
        x+=1
        pass
    print x

def main():
    global dead
    dead=False
    our_thread=threading.Thread(target=do_this, name='Thraed:1 ')
    our_thread.start()
    print threading.active_count() #no. of active thread
    #print threading.enumerate() #no of threading process
    print threading.current_thread()
    raw_input('hit enter to terminate program')
    dead=True

if __name__=='__main__':
    main()