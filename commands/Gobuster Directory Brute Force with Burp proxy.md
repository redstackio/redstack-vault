---
id: 1f0afd23-daa7-43bc-8a38-0dc4606848ec
name: Gobuster Directory Brute Force with Burp proxy
type: command
executor: bash
data: gobuster dir -w $_WORDLIST -u http://$_TARGET_IP -p http://127.0.0.1:8080
output: 'root@kali:~# gobuster dir -w common.txt -u http://10.10.10.10/ -p http://127.0.0.1:8080

  ===============================================================

  Gobuster v3.0.1

  by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)

  ===============================================================

  [+] Url:            http://10.10.10.10/

  [+] Threads:        10

  [+] Wordlist:       common.txt

  [+] Status codes:   200,204,301,302,307,401,403

  [+] Proxy:          http://127.0.0.1:8080

  [+] User Agent:     gobuster/3.0.1

  [+] Timeout:        10s

  ===============================================================

  2019/09/13 21:16:04 Starting gobuster

  ===============================================================

  /.hta (Status: 403)

  /.htpasswd (Status: 403)

  /.htaccess (Status: 403)

  /api (Status: 301)

  /backups (Status: 301)

  /dev (Status: 301)

  /index.html (Status: 200)

  /server-status (Status: 403)

  /var (Status: 301)

  ===============================================================

  2019/09/13 21:16:33 Finished

  ==============================================================='
created_at: '2019-09-14T01:56:14.218871+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Gobuster Directory Brute Force with Burp proxy

```bash
gobuster dir -w $_WORDLIST -u http://$_TARGET_IP -p http://127.0.0.1:8080
```

## Expected Output

```
root@kali:~# gobuster dir -w common.txt -u http://10.10.10.10/ -p http://127.0.0.1:8080
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.10.10/
[+] Threads:        10
[+] Wordlist:       common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] Proxy:          http://127.0.0.1:8080
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2019/09/13 21:16:04 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htpasswd (Status: 403)
/.htaccess (Status: 403)
/api (Status: 301)
/backups (Status: 301)
/dev (Status: 301)
/index.html (Status: 200)
/server-status (Status: 403)
/var (Status: 301)
===============================================================
2019/09/13 21:16:33 Finished
===============================================================
```
