import os ,shutil

def MoveFiles():
    SourcePath = r'D:\Tutorials\SourceDir\SampleFile.txt'
    lstDestDir = [r'D:\Tutorials\DestDir\Folder1',r'D:\Tutorials\DestDir\Folder2']
    for dir_name in lstDestDir:
        try:
            shutil.copy(SourcePath,dir_name)
            print(f'Successfully Moved to {dir_name}')
        except:
            print(f'Error on moving to {dir_name}')

if __name__ == '__main__':
    MoveFiles()