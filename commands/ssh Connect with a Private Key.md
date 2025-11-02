---
id: e082f026-1d48-4bf9-86cb-3ee56718cfb2
name: ssh Connect with a Private Key
type: command
executor: bash
data: ssh -i $_PRIVATE_KEY -l $_USER $_TARGET_IP
output: "root@kali:~# ssh -i id_rsa -l bob 10.10.10.10\nThe authenticity of host '10.10.10.10\
  \ (10.10.10.10)' can't be established. \nECDSA key fingerprint is SHA256:lwH7db30salekhX8rTgJTq79lawse2cXftewhu8LsEs.\n\
  Are you sure you want to continue connecting (yes/no)? yes\nWarning: Permanently\
  \ added '10.10.10.10' (ECDSA) to the list of known hosts.\nWelcome to Ubuntu 12.04\
  \ LTS (GNU/Linux 3.2.0-23-generic x86_64)\n\n * Documentation:  https://help.ubuntu.com/\
  \ \nNew release '14.04.5 LTS' available.                                       \
  \                            \nRun 'do-release-upgrade' to upgrade to it. \n\nLast\
  \ login:Fri Feb 16 14:50:29 2018 from 10.10.14.3                               \
  \                     "
created_at: '2019-11-25T20:01:51.811071+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[host]]'
- '[[ssh]]'
---

# ssh Connect with a Private Key

```bash
ssh -i $_PRIVATE_KEY -l $_USER $_TARGET_IP
```

## Expected Output

```
root@kali:~# ssh -i id_rsa -l bob 10.10.10.10
The authenticity of host '10.10.10.10 (10.10.10.10)' can't be established. 
ECDSA key fingerprint is SHA256:lwH7db30salekhX8rTgJTq79lawse2cXftewhu8LsEs.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '10.10.10.10' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 12.04 LTS (GNU/Linux 3.2.0-23-generic x86_64)

 * Documentation:  https://help.ubuntu.com/ 
New release '14.04.5 LTS' available.                                                                   
Run 'do-release-upgrade' to upgrade to it. 

Last login:Fri Feb 16 14:50:29 2018 from 10.10.14.3                                                    
```


