---
id: af1e58b4-84b4-4714-8e55-6302c2310baa
name: Dirb directory brute force through a Burp proxy
type: command
executor: null
data: dirb http://10.10.10.10 common.txt -r -p 127.0.0.1:8080
output: "root@kali:~# dirb http://10.10.10.10 common.txt -r -p 127.0.0.1:8080\n\n\
  -----------------\nDIRB v2.22    \nBy The Dark Raver\n-----------------\n\nSTART_TIME:\
  \ Fri Sep 13 21:50:27 2019\nURL_BASE: http://10.10.10.10/\nWORDLIST_FILES: common.txt\n\
  PROXY: 127.0.0.1:8080\nOPTION: Not Recursive\n\n-----------------\n\nGENERATED WORDS:\
  \ 4593                                                          \n\n---- Scanning\
  \ URL: http://10.10.10.10/ ----\n==> DIRECTORY: http://10.10.10.10/api/        \
  \                                                                              \
  \                         \n==> DIRECTORY: http://10.10.10.10/backups/         \
  \                                                                              \
  \                    \n==> DIRECTORY: http://10.10.10.10/dev/                  \
  \                                                                              \
  \               \n+ http://10.10.10.10/index.html (CODE:200|SIZE:10918)        \
  \                                                                              \
  \          \n+ http://10.10.10.10/server-status (CODE:403|SIZE:276)            \
  \                                                                              \
  \     \n==> DIRECTORY: http://10.10.10.10/var/                                 \
  \                                                                              \n\
  \                                                                              \
  \                                                                       \n-----------------\n\
  END_TIME: Fri Sep 13 21:52:17 2019\nDOWNLOADED: 4593 - FOUND: 2\n"
created_at: '2019-09-14T01:56:14.223570+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Dirb directory brute force through a Burp proxy

```bash
dirb http://10.10.10.10 common.txt -r -p 127.0.0.1:8080
```

## Expected Output

```
root@kali:~# dirb http://10.10.10.10 common.txt -r -p 127.0.0.1:8080

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Fri Sep 13 21:50:27 2019
URL_BASE: http://10.10.10.10/
WORDLIST_FILES: common.txt
PROXY: 127.0.0.1:8080
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
END_TIME: Fri Sep 13 21:52:17 2019
DOWNLOADED: 4593 - FOUND: 2

```


