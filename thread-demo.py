import threading

def main():
    print threading.active_count() #no. of active thread
    print threading.enumerate() #no of threading process
    print threading.current_thread()

if __name__=='__main__':
    main()