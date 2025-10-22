---
id: 8b6b574f-330e-440e-ba1b-eaf446808c95
name: Dirb directory brute force
type: command
executor: bash
data: dirb http:/$_TARGET_IP $_WORDLIST -r
output: "root@kali:~# dirb http://10.10.10.10 common.txt -r\n\n-----------------\n\
  DIRB v2.22    \nBy The Dark Raver\n-----------------\n\nSTART_TIME: Fri Sep 13 21:43:08\
  \ 2019\nURL_BASE: http://10.10.10.10/\nWORDLIST_FILES: common.txt\nOPTION: Not Recursive\n\
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
  \        \n                                                                    \
  \                                                                              \
  \   \n-----------------\nEND_TIME: Fri Sep 13 21:43:09 2019\nDOWNLOADED: 4593 -\
  \ FOUND: 2\n"
created_at: '2019-09-14T01:56:14.220988+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Dirb directory brute force

```bash
dirb http:/$_TARGET_IP $_WORDLIST -r
```

## Expected Output

```
root@kali:~# dirb http://10.10.10.10 common.txt -r

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Fri Sep 13 21:43:08 2019
URL_BASE: http://10.10.10.10/
WORDLIST_FILES: common.txt
OPTION: Not Recursive

-----------------

GENERATED WORDS: 4593                                                          

---- Scanning URL: http://10.10.10.10/ ----
==> DIRECTORY: http://10.10.10.10/api/                                                                                                               
==> DIRECTORY: http://10.10.10.10/backups/                                                                                                           
==> DIRECTORY: http://10.10.10.10/dev/                                                                                                               
+ http://10.10.10.10/index.html (CODE:200|SIZE:10918)                                                                                                
+ http://10.10.10.10/server-status (CODE:403|SIZE:276)                                                                                               
==> DIRECTORY: http://10.10.10.10/var/                                                                                                               

-----------------
END_TIME: Fri Sep 13 21:43:09 2019
DOWNLOADED: 4593 - FOUND: 2

```
