---
id: b90bf6c8-e5b9-4e7a-a59c-d128636082c3
name: Find List All Files with Setuid Permissions Set
type: command
executor: bash
data: find / -perm -4000 -ls 2>/dev/null
output: "user@ubuntu18x64:~$ find / -perm -4000 -ls 2>/dev/null\n  1180389     40\
  \ -rwsr-xr-x   1 root     root        40344 Jan 25  2018 /usr/bin/newgrp\n  1180169\
  \     44 -rwsr-xr-x   1 root     root        44528 Jan 25  2018 /usr/bin/chsh\n\
  \  1180390     40 -rwsr-xr-x   1 root     root        37136 Jan 25  2018 /usr/bin/newuidmap\n\
  \  1180572     20 -rwsr-xr-x   1 root     root        18448 Mar  9  2017 /usr/bin/traceroute6.iputils\n\
  \  1185912     24 -rwsr-xr-x   1 root     root        22520 Mar 27  2019 /usr/bin/pkexec\n\
  \  1180407     60 -rwsr-xr-x   1 root     root        59640 Jan 25  2018 /usr/bin/passwd\n\
  \  1180116     52 -rwsr-sr-x   1 daemon   daemon      51464 Feb 20  2018 /usr/bin/at\n\
  \  1180536    148 -rwsr-xr-x   1 root     root       149080 Jan 18  2018 /usr/bin/sudo\n\
  \  1181285   2612 -rwsr-xr-x   1 root     root      2671240 Jun  6 17:31 /usr/bin/vim.basic"
created_at: '2019-10-11T21:24:57.011696+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Find List All Files with Setuid Permissions Set

```bash
find / -perm -4000 -ls 2>/dev/null
```

## Expected Output

```
user@ubuntu18x64:~$ find / -perm -4000 -ls 2>/dev/null
  1180389     40 -rwsr-xr-x   1 root     root        40344 Jan 25  2018 /usr/bin/newgrp
  1180169     44 -rwsr-xr-x   1 root     root        44528 Jan 25  2018 /usr/bin/chsh
  1180390     40 -rwsr-xr-x   1 root     root        37136 Jan 25  2018 /usr/bin/newuidmap
  1180572     20 -rwsr-xr-x   1 root     root        18448 Mar  9  2017 /usr/bin/traceroute6.iputils
  1185912     24 -rwsr-xr-x   1 root     root        22520 Mar 27  2019 /usr/bin/pkexec
  1180407     60 -rwsr-xr-x   1 root     root        59640 Jan 25  2018 /usr/bin/passwd
  1180116     52 -rwsr-sr-x   1 daemon   daemon      51464 Feb 20  2018 /usr/bin/at
  1180536    148 -rwsr-xr-x   1 root     root       149080 Jan 18  2018 /usr/bin/sudo
  1181285   2612 -rwsr-xr-x   1 root     root      2671240 Jun  6 17:31 /usr/bin/vim.basic
```
