---
id: 74027deb-aee5-4eed-9d25-879abbe42b19
name: linuxprivchecker.py Scan a Linux Filesystem for Vulnerabilities
type: command
executor: bash
data: python linuxprivchecker.py
output: "root@hackers:~/git/linuxprivchecker# python linuxprivchecker.py \n=================================================================================================\n\
  LINUX PRIVILEGE ESCALATION CHECKER\n=================================================================================================\n\
  \n[*] GETTING BASIC SYSTEM INFO...\n\n[+] Kernel\n    Linux version 4.19.0-kali4-amd64\
  \ (devel@kali.org) (gcc version 8.3.0 (Debian 8.3.0-2)) #1 SMP Debian 4.19.28-2kali1\
  \ (2019-03-18)\n\n[+] Hostname\n    hackers\n\n[+] Operating System\n    Kali GNU/Linux\
  \ Rolling \\n \\l\n\n.... CUT ....\n"
created_at: '2019-09-17T06:34:44.714301+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# linuxprivchecker.py Scan a Linux Filesystem for Vulnerabilities

```bash
python linuxprivchecker.py
```

## Expected Output

```
root@hackers:~/git/linuxprivchecker# python linuxprivchecker.py 
=================================================================================================
LINUX PRIVILEGE ESCALATION CHECKER
=================================================================================================

[*] GETTING BASIC SYSTEM INFO...

[+] Kernel
    Linux version 4.19.0-kali4-amd64 (devel@kali.org) (gcc version 8.3.0 (Debian 8.3.0-2)) #1 SMP Debian 4.19.28-2kali1 (2019-03-18)

[+] Hostname
    hackers

[+] Operating System
    Kali GNU/Linux Rolling \n \l

.... CUT ....

```


