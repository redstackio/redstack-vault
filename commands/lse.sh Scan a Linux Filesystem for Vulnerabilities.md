---
id: 111ae502-6b1f-4390-9462-081070d30d29
name: lse.sh Scan a Linux Filesystem for Vulnerabilities
type: command
executor: bash
data: 'lse.sh '
output: "root@hackers:~/git/linux-smart-enumeration# ./lse.sh \n---\nIf you know the\
  \ current user password, write it here for better results: \n---\n\n        User:\
  \ root\n     User ID: 0\n    Password: none\n        Home: /root\n        Path:\
  \ /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\n       umask: 0022\n\
  \n    Hostname: hackers\n       Linux: 4.19.0-kali4-amd64\nDistribution: Kali GNU/Linux\
  \ Rolling\nArchitecture: x86_64\n\n==================================================================(\
  \ users )=====\n[i] usr000 Current user groups.............................................\
  \ yes!\n[*] usr010 Is current user in an administrative group?.....................\
  \ nope\n[*] usr020 Are there other users in an administrative groups?..............\
  \ nope\n[*] usr030 Other users with shell..........................................\
  \ yes!\n[i] usr040 Environment information.........................................\
  \ skip\n[i] usr050 Groups for other users..........................................\
  \ skip\n[i] usr060 Other users.....................................................\
  \ skip\n===================================================================( sudo\
  \ )=====\n[!] sud000 Can we sudo without a password?.................................\
  \ yes!\n---\nuid=0(root) gid=0(root) groups=0(root)\n---\n[*] sud040 Can we read\
  \ /etc/sudoers?....................................... yes!\n[*] sud050 Do we know\
  \ if any other users used sudo?........................ nope\n\n.... CUT ....\n"
created_at: '2019-09-17T06:34:44.725288+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# lse.sh Scan a Linux Filesystem for Vulnerabilities

```bash
lse.sh 
```

## Expected Output

```
root@hackers:~/git/linux-smart-enumeration# ./lse.sh 
---
If you know the current user password, write it here for better results: 
---

        User: root
     User ID: 0
    Password: none
        Home: /root
        Path: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
       umask: 0022

    Hostname: hackers
       Linux: 4.19.0-kali4-amd64
Distribution: Kali GNU/Linux Rolling
Architecture: x86_64

==================================================================( users )=====
[i] usr000 Current user groups............................................. yes!
[*] usr010 Is current user in an administrative group?..................... nope
[*] usr020 Are there other users in an administrative groups?.............. nope
[*] usr030 Other users with shell.......................................... yes!
[i] usr040 Environment information......................................... skip
[i] usr050 Groups for other users.......................................... skip
[i] usr060 Other users..................................................... skip
===================================================================( sudo )=====
[!] sud000 Can we sudo without a password?................................. yes!
---
uid=0(root) gid=0(root) groups=0(root)
---
[*] sud040 Can we read /etc/sudoers?....................................... yes!
[*] sud050 Do we know if any other users used sudo?........................ nope

.... CUT ....

```


