---
id: e8900666-a057-4077-a482-bf664b8caabd
name: linPEAS Enumerate a Linux/Unix System with All Checks
type: command
executor: bash
data: linpeas.sh -a
output: "bob@3f01c92204f2:/tmp$ ./linpeas.sh -a                                  \
  \                                                  \n\n\nLinux Privesc Checklist:\
  \ https://book.hacktricks.xyz/linux-unix/linux-privilege-escalation-checklist\n\
  \ LEYEND:\n  RED/YELLOW: 99% a PE vector\n  RED: You must take a look at it\n  LightCyan:\
  \ Users with console\n  Blue: Users without console & mounted devs\n  Green: Common\
  \ things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs)\n  LightMangenta:\
  \ Your username\n..."
created_at: '2020-03-22T20:44:11.639375+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# linPEAS Enumerate a Linux/Unix System with All Checks

```bash
linpeas.sh -a
```

## Expected Output

```
bob@3f01c92204f2:/tmp$ ./linpeas.sh -a                                                                                    

Linux Privesc Checklist: https://book.hacktricks.xyz/linux-unix/linux-privilege-escalation-checklist
 LEYEND:
  RED/YELLOW: 99% a PE vector
  RED: You must take a look at it
  LightCyan: Users with console
  Blue: Users without console & mounted devs
  Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs)
  LightMangenta: Your username
...
```
