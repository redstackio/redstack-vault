---
id: 5ad3daea-2f71-47db-be57-ab7c437b167a
name: Dirb recursive directory brute force
type: command
executor: null
data: dirb http://10.10.10.10 common.txt
output: "root@kali:~# cat notes \nroot@kali:~# dirb http://10.10.10.10 common.txt\n\
  \n-----------------\nDIRB v2.22    \nBy The Dark Raver\n-----------------\n\nSTART_TIME:\
  \ Fri Sep 13 21:46:31 2019\nURL_BASE: http://10.10.10.10/\nWORDLIST_FILES: common.txt\n\
  \n-----------------\n\nGENERATED WORDS: 4593                                   \
  \                       \n\n---- Scanning URL: http://10.10.10.10/ ----\n==> DIRECTORY:\
  \ http://10.10.10.10/api/                                                      \
  \                                                         \n==> DIRECTORY: http://10.10.10.10/backups/\
  \                                                                              \
  \                             \n==> DIRECTORY: http://10.10.10.10/dev/         \
  \                                                                              \
  \                        \n+ http://10.10.10.10/index.html (CODE:200|SIZE:10918)\
  \                                                                              \
  \                  \n+ http://10.10.10.10/server-status (CODE:403|SIZE:276)    \
  \                                                                              \
  \             \n==> DIRECTORY: http://10.10.10.10/var/                         \
  \                                                                              \
  \        \n..\n..\n---- Entering directory: http://10.10.10.10/backups/old/ ----\n\
  + http://10.10.10.10/backups/old/id_rsa (CODE:200|SIZE:391)                    \
  \                                                                      \n      \
  \                                                                              \
  \                                                                 \n---- Entering\
  \ directory: http://10.10.10.10/backups/site/ ----\n                           \
  \                                                                              \
  \                                            \n-----------------\nEND_TIME: Fri\
  \ Sep 13 21:46:42 2019\nDOWNLOADED: 36744 - FOUND: 3"
created_at: '2019-09-14T01:56:14.222792+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Dirb recursive directory brute force

```bash
dirb http://10.10.10.10 common.txt
```

## Expected Output

```
root@kali:~# cat notes 
root@kali:~# dirb http://10.10.10.10 common.txt

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Fri Sep 13 21:46:31 2019
URL_BASE: http://10.10.10.10/
WORDLIST_FILES: common.txt

-----------------

GENERATED WORDS: 4593                                                          

---- Scanning URL: http://10.10.10.10/ ----
==> DIRECTORY: http://10.10.10.10/api/                                                                                                               
==> DIRECTORY: http://10.10.10.10/backups/                                                                                                           
==> DIRECTORY: http://10.10.10.10/dev/                                                                                                               
+ http://10.10.10.10/index.html (CODE:200|SIZE:10918)                                                                                                
+ http://10.10.10.10/server-status (CODE:403|SIZE:276)                                                                                               
==> DIRECTORY: http://10.10.10.10/var/                                                                                                               
..
..
---- Entering directory: http://10.10.10.10/backups/old/ ----
+ http://10.10.10.10/backups/old/id_rsa (CODE:200|SIZE:391)                                                                                          
                                                                                                                                                     
---- Entering directory: http://10.10.10.10/backups/site/ ----
                                                                                                                                                     
-----------------
END_TIME: Fri Sep 13 21:46:42 2019
DOWNLOADED: 36744 - FOUND: 3
```


