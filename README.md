# File-Checksum-Integrity-Verifier
File Checksum Integrity Verifier

It is a GUI based python application. So, Python3 needs to be installed to run this application.

FCIV can verify Integrity of file:-
  1. residing on same system at different locations.
  2. residing on different systems.

_________________________________________________________________________  
Steps for Use:-

On single system:
1. Run hash.py in Python3 IDLE.
2. Browse File 1 and File 2 in respective fields.
3. Click on "Check Integrity" Button.
4. File Integrity Status and MD5, SHA1 hashes will be displayed.

On two diffrent systems:
1. Run hash.py in Python3 IDLE.
2. Browse File 1 in first fields.
3. Click on "Save State" Button.
4. Save the folder in USB or any removable media.
5. Run hash.py on another system.
6. Browse File 2 in second field.
7. Click on "Check Integrity" Button.
8. File Integrity Status and MD5, SHA1 hashes will be displayed.
__________________________________________________________________________

* It uses MD5 and SHA1 algorithm for double verification of file integrity.
* It can operate on any type of files :text,audio,video,etc.. (operates at binary level).
* It saves the state after operating on file (at one system), and then is able to operate at another file (on another system), No network operation required. 
