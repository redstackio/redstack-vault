---
id: fc804e2a-639c-4787-93cc-3e049415a9a4
name: Nmap Command to Find Response Headers
type: command
executor: ''
data: nmap -sV --script=http-headers 192.168.1.11
output: "Starting Nmap 7.70 ( https://nmap.org ) at 2020-09-01 00:20 IST\nNmap scan\
  \ report for 192.168.1.11\nHost is up (0.00019s latency).\nNot shown: 500 closed\
  \ ports, 497 filtered ports\nPORT     STATE SERVICE  VERSION\n80/tcp   open  http\
  \     Apache httpd 2.4.41 ((Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3)\n\
  | http-headers: \n|   Date: Mon, 31 Aug 2020 18:51:07 GMT\n|   Server: Apache/2.4.41\
  \ (Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3\n|   Last-Modified:\
  \ Sat, 26 Oct 2019 05:14:41 GMT\n|   ETag: \"1d96-595c958015240\"\n|   Accept-Ranges:\
  \ bytes\n|   Content-Length: 7574\n|   Connection: close\n|   Content-Type: text/html\n\
  |   \n|_  (Request type: HEAD)\n|_http-server-header: Apache/2.4.41 (Unix) OpenSSL/1.1.1d\
  \ PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3\n443/tcp  open  ssl/http Apache httpd\
  \ 2.4.41 ((Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3)\n| http-headers:\
  \ \n|   Date: Mon, 31 Aug 2020 18:51:07 GMT\n|   Server: Apache/2.4.41 (Unix) OpenSSL/1.1.1d\
  \ PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3\n|   Last-Modified: Sat, 26 Oct 2019\
  \ 05:14:41 GMT\n|   ETag: \"1d96-595c958015240\"\n|   Accept-Ranges: bytes\n|  \
  \ Content-Length: 7574\n|   Connection: close\n|   Content-Type: text/html\n|  \
  \ \n|_  (Request type: HEAD)\n|_http-server-header: Apache/2.4.41 (Unix) OpenSSL/1.1.1d\
  \ PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3"
created_at: '2020-08-31T19:08:46.847809+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Command to Find Response Headers

```bash
nmap -sV --script=http-headers 192.168.1.11
```

## Expected Output

```
Starting Nmap 7.70 ( https://nmap.org ) at 2020-09-01 00:20 IST
Nmap scan report for 192.168.1.11
Host is up (0.00019s latency).
Not shown: 500 closed ports, 497 filtered ports
PORT     STATE SERVICE  VERSION
80/tcp   open  http     Apache httpd 2.4.41 ((Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3)
| http-headers: 
|   Date: Mon, 31 Aug 2020 18:51:07 GMT
|   Server: Apache/2.4.41 (Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3
|   Last-Modified: Sat, 26 Oct 2019 05:14:41 GMT
|   ETag: "1d96-595c958015240"
|   Accept-Ranges: bytes
|   Content-Length: 7574
|   Connection: close
|   Content-Type: text/html
|   
|_  (Request type: HEAD)
|_http-server-header: Apache/2.4.41 (Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3
443/tcp  open  ssl/http Apache httpd 2.4.41 ((Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3)
| http-headers: 
|   Date: Mon, 31 Aug 2020 18:51:07 GMT
|   Server: Apache/2.4.41 (Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3
|   Last-Modified: Sat, 26 Oct 2019 05:14:41 GMT
|   ETag: "1d96-595c958015240"
|   Accept-Ranges: bytes
|   Content-Length: 7574
|   Connection: close
|   Content-Type: text/html
|   
|_  (Request type: HEAD)
|_http-server-header: Apache/2.4.41 (Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3
```


