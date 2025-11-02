---
id: 11bef415-9d50-4ee3-8500-1221d0793739
name: WPScan Enumerate WordPress Plugins, Users, Themes and TimThumb
type: command
executor: bash
data: wpscan --url http://$_TARGET_IP --enumerate p,t,u,tt
output: "oot@kali:~/Documents# wpscan --url http://10.10.10.10 --enumerate p,t,u,tt\n\
  _______________________________________________________________\n        __    \
  \      _______   _____\n        \\ \\        / /  __ \\ / ____|\n         \\ \\\
  \  /\\  / /| |__) | (___   ___  __ _ _ __ ®\n          \\ \\/  \\/ / |  ___/ \\\
  ___ \\ / __|/ _` | '_ \\\n           \\  /\\  /  | |     ____) | (__| (_| | | |\
  \ |\n            \\/  \\/   |_|    |_____/ \\___|\\__,_|_| |_|\n\n        WordPress\
  \ Security Scanner by the WPScan Team\n                       Version 3.5.3\n  \
  \        Sponsored by Sucuri - https://sucuri.net\n      @_WPScan_, @ethicalhack3r,\
  \ @erwan_lr, @_FireFart_\n_______________________________________________________________\n\
  \n[+] URL: http://10.10.10.10/\n[+] Started: Mon Sep 16 12:56:20 2019\n\nInteresting\
  \ Finding(s):\n\n[+] http://10.10.10.10/\n | Interesting Entries:\n |  - Server:\
  \ Apache/2.4.10 (Debian)\n |  - X-Powered-By: PHP/5.6.31\n | Found By: Headers (Passive\
  \ Detection)\n | Confidence: 100%\n...\n...\n[+] Finished: Mon Sep 16 12:58:11 2019\n\
  [+] Requests Done: 3007\n[+] Cached Requests: 56\n[+] Data Sent: 665.888 KB\n[+]\
  \ Data Received: 758.476 KB\n[+] Memory used: 210.875 MB\n[+] Elapsed time: 00:01:50\n"
created_at: '2019-09-16T17:49:55.971905+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[WPScan]]'
---

# WPScan Enumerate WordPress Plugins, Users, Themes and TimThumb

```bash
wpscan --url http://$_TARGET_IP --enumerate p,t,u,tt
```

## Expected Output

```
oot@kali:~/Documents# wpscan --url http://10.10.10.10 --enumerate p,t,u,tt
_______________________________________________________________
        __          _______   _____
        \ \        / /  __ \ / ____|
         \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
          \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
           \  /\  /  | |     ____) | (__| (_| | | | |
            \/  \/   |_|    |_____/ \___|\__,_|_| |_|

        WordPress Security Scanner by the WPScan Team
                       Version 3.5.3
          Sponsored by Sucuri - https://sucuri.net
      @_WPScan_, @ethicalhack3r, @erwan_lr, @_FireFart_
_______________________________________________________________

[+] URL: http://10.10.10.10/
[+] Started: Mon Sep 16 12:56:20 2019

Interesting Finding(s):

[+] http://10.10.10.10/
 | Interesting Entries:
 |  - Server: Apache/2.4.10 (Debian)
 |  - X-Powered-By: PHP/5.6.31
 | Found By: Headers (Passive Detection)
 | Confidence: 100%
...
...
[+] Finished: Mon Sep 16 12:58:11 2019
[+] Requests Done: 3007
[+] Cached Requests: 56
[+] Data Sent: 665.888 KB
[+] Data Received: 758.476 KB
[+] Memory used: 210.875 MB
[+] Elapsed time: 00:01:50

```


