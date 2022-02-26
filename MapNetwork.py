import subprocess
import traceback

def map_network(drive,path,userid,passwd):
    try:
        subprocess.call(r'net use {}: /del'.format(drive), shell=True)
        print(f'Disconnected drive {drive}')
        subprocess.call(r'net use {}: {} /user:{} {}'.format(drive,path,userid,passwd), shell=True)
        print(f'Mapped network drive {drive} successfully...')
    except:
        print(f'Error in mapping network {drive}')
        print(traceback.print_exc())

if __name__ == '__main__':
    map_network('X',r"\\machinename\sharename\foldername1",r"domain_name\username","password")
    map_network('Y',r"\\machinename\sharename\foldername2",r"domain_name\username","password")
    map_network('Z',r"\\machinename\sharename\foldername3",r"domain_name\username","password")


     