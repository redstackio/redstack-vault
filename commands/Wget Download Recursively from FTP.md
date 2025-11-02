---
id: e330ca36-9514-4fdd-b8a3-baaa58f75367
name: Wget Download Recursively from FTP
type: command
executor: bash
data: wget -r --no-passive --no-parent -m ftp://$_TARGET_IP
output: "root@kali:~# wget -r --no-passive --no-parent -m ftp://10.10.10.10 \n--2019-11-05\
  \ 19:41:24--  ftp://10.10.10.10/\n           => '10.10.10.10/.listing'\nConnecting\
  \ to 10.10.10.10:21... connected.\nLogging in as anonymous ... Logged in!\n==> SYST\
  \ ... done.    ==> PWD ... done.\n==> TYPE I ... done.  ==> CWD not needed.\n==>\
  \ PORT ... done.    ==> LIST ... done.\n\n10.10.10.10/BOOTNXT            100%[===============================>]\
  \ \n\n2019-11-05 19:41:26 (131 KB/s) - ‘10.10.10.10/BOOTNXT’ saved [1] \n\n10.10.10.10/.listing\
  \               [ <=>                            ]     782  --.-KB/s    in 0s"
created_at: '2019-10-25T23:22:29.819127+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Wget]]'
- '[[type]]'
---

# Wget Download Recursively from FTP

```bash
wget -r --no-passive --no-parent -m ftp://$_TARGET_IP
```

## Expected Output

```
root@kali:~# wget -r --no-passive --no-parent -m ftp://10.10.10.10 
--2019-11-05 19:41:24--  ftp://10.10.10.10/
           => '10.10.10.10/.listing'
Connecting to 10.10.10.10:21... connected.
Logging in as anonymous ... Logged in!
==> SYST ... done.    ==> PWD ... done.
==> TYPE I ... done.  ==> CWD not needed.
==> PORT ... done.    ==> LIST ... done.

10.10.10.10/BOOTNXT            100%[===============================>] 

2019-11-05 19:41:26 (131 KB/s) - ‘10.10.10.10/BOOTNXT’ saved [1] 

10.10.10.10/.listing               [ <=>                            ]     782  --.-KB/s    in 0s
```


