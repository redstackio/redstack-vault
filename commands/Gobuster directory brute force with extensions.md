---
id: 0f8e473b-de9e-40b9-b350-c8b4522c6dab
name: Gobuster Directory Brute Force with Extensions
type: command
executor: bash
data: gobuster dir -w $_WORDLIST -u http://$_TARGET_IP -f -e -x '$_EXT1,$_EXT2,$_EXT3'
output: 'root@kali:~# gobuster dir -w /opt/SecLists/Discovery/Web-Content/common.txt
  -u http://10.10.10.10 -f -e -x ''php,txt,html,sh''

  ===============================================================

  Gobuster v3.0.1

  by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)

  ===============================================================

  [+] Url:            http://10.10.10.10

  [+] Threads:        10

  [+] Wordlist:       /opt/SecLists/Discovery/Web-Content/common.txt

  [+] Status codes:   200,204,301,302,307,401,403

  [+] User Agent:     gobuster/3.0.1

  [+] Extensions:     php,txt,html,sh

  [+] Add Slash:      true

  [+] Expanded:       true

  [+] Timeout:        10s

  ===============================================================

  2019/10/10 17:26:15 Starting gobuster

  ===============================================================

  http://10.10.10.10/cgi-bin/ (Status: 403)

  http://10.10.10.10/cgi-bin// (Status: 403)

  http://10.10.10.10/cgi-bin/.html (Status: 403)

  http://10.10.10.10/index.html (Status: 200)

  http://10.10.10.10/server-status/ (Status: 403)

  ===============================================================

  2019/10/10 17:28:54 Finished

  ==============================================================='
created_at: '2019-10-10T21:55:34.546563+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Gobuster Directory Brute Force with Extensions

```bash
gobuster dir -w $_WORDLIST -u http://$_TARGET_IP -f -e -x '$_EXT1,$_EXT2,$_EXT3'
```

## Expected Output

```
root@kali:~# gobuster dir -w /opt/SecLists/Discovery/Web-Content/common.txt -u http://10.10.10.10 -f -e -x 'php,txt,html,sh'
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.10.10
[+] Threads:        10
[+] Wordlist:       /opt/SecLists/Discovery/Web-Content/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     php,txt,html,sh
[+] Add Slash:      true
[+] Expanded:       true
[+] Timeout:        10s
===============================================================
2019/10/10 17:26:15 Starting gobuster
===============================================================
http://10.10.10.10/cgi-bin/ (Status: 403)
http://10.10.10.10/cgi-bin// (Status: 403)
http://10.10.10.10/cgi-bin/.html (Status: 403)
http://10.10.10.10/index.html (Status: 200)
http://10.10.10.10/server-status/ (Status: 403)
===============================================================
2019/10/10 17:28:54 Finished
===============================================================
```


