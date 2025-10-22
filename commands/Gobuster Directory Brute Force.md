---
id: 21cc125b-0be7-4d96-9228-eb144900a21f
name: Gobuster Directory Brute Force
type: command
executor: bash
data: gobuster dir -w $_WORDLIST -u http://$_TARGET_IP
output: 'root@kali:~# gobuster dir -w common.txt -u http://10.10.10.10

  ===============================================================

  Gobuster v3.0.1

  by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)

  ===============================================================

  [+] Url:            http://10.10.10.10

  [+] Threads:        10

  [+] Wordlist:       common.txt

  [+] Status codes:   200,204,301,302,307,401,403

  [+] User Agent:     gobuster/3.0.1

  [+] Timeout:        10s

  ===============================================================

  2019/09/13 20:20:35 Starting gobuster

  ===============================================================

  /.htpasswd (Status: 403)

  /.hta (Status: 403)

  /.htaccess (Status: 403)

  /api (Status: 301)

  /backups (Status: 301)

  /dev (Status: 301)

  /index.html (Status: 200)

  /server-status (Status: 403)

  /var (Status: 301)

  ===============================================================

  2019/09/13 20:20:36 Finished

  ==============================================================='
created_at: '2019-09-14T01:56:14.216810+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Gobuster Directory Brute Force

```bash
gobuster dir -w $_WORDLIST -u http://$_TARGET_IP
```

## Expected Output

```
root@kali:~# gobuster dir -w common.txt -u http://10.10.10.10
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.10.10
[+] Threads:        10
[+] Wordlist:       common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2019/09/13 20:20:35 Starting gobuster
===============================================================
/.htpasswd (Status: 403)
/.hta (Status: 403)
/.htaccess (Status: 403)
/api (Status: 301)
/backups (Status: 301)
/dev (Status: 301)
/index.html (Status: 200)
/server-status (Status: 403)
/var (Status: 301)
===============================================================
2019/09/13 20:20:36 Finished
===============================================================
```
