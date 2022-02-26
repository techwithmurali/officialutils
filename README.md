# officialutils
**Simple Official Utilities**

1) **Moving Files from a source directory to multiple destination directories on a click.**

   **FileName**   : MoveFiles.py
   
   **Prerequiste**: Specify the Source Folder name and Destination Folder names in Movefiles.py.
   
   
2) **Retreiving frequently used passwords for different applications**
   
   **FileName**:getPassword.py
   
   Replace MyPassword!!!! with desired password and create shortcut in a desktop.
   
   On double click of the file, the password will be copied to clipboard and can be pasted in the desired location.
   
   pyperclip library needs to be installed using command - pip install pyperclip 
    
3) **Quickly open the frequently used URLs in the browser.**

   **FileName**: openbrowser.py
   
   Frequently used URLS can be stored in this program and on executing this, the urls are opened in the browser.
   
   webbrowser module is used for the same.
   
4) **Mapping the network directories  to the system**.
   **FileName**: MapNetwork.py
   
   Often we may need to map multiple networks to our system for ease of access and at many a times, we may need to enter the credentials.
   This program disconnects and maps the credentials to the system automatically based on the credentials given.
   
5) **Exposing a Directory contents over the network using simple http server.**
   python -m http.server <portno> command when executed from a command window exposes the current directory contents which can be accessed using the ipaddress and port number from the same network.
   The shared batch file contains code to expose a specific directory at a given port.
   **FileName**: httpServer.bat [Rename the txt file to bat and use the same ] 
