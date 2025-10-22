---
id: 21962dd1-f2b8-45b5-b2e1-7bc6f4432aad
name: pspy Monitor Processes and Commands
type: command
executor: bash
data: pspy
output: "bob@host:$ ./pspy \npspy - version: v1.2.0 - Commit SHA: 9c63e5d6c58f7bcdc235db663f5e3fe1c33b8855\n\
  \                                                                              \
  \                                                  \n\n     ██▓███    ██████  ██▓███\
  \ ▓██   ██▓\n    ▓██░  ██▒▒██    ▒ ▓██░  ██▒▒██  ██▒\n    ▓██░ ██▓▒░ ▓██▄   ▓██░\
  \ ██▓▒ ▒██ ██░\n    ▒██▄█▓▒ ▒  ▒   ██▒▒██▄█▓▒ ▒ ░ ▐██▓░\n    ▒██▒ ░  ░▒██████▒▒▒██▒\
  \ ░  ░ ░ ██▒▓░\n    ▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░  ██▒▒▒ \n    ░▒ ░     ░ ░▒  ░ ░░▒\
  \ ░     ▓██ ░▒░ \n    ░░       ░  ░  ░  ░░       ▒ ▒ ░░  \n                   ░\
  \           ░ ░     \n                               ░ ░     \n\n2019/11/05 18:58:44\
  \ CMD: UID=0    PID=1445   | /usr/sbin/vmtoolsd \n2019/11/05 18:58:44 CMD: UID=0\
  \    PID=14     | \n2019/11/05 18:58:44 CMD: UID=0    PID=1305   | /usr/sbin/rsyslogd\n\
  2019/11/05 18:59:01 CMD: UID=0    PID=2221   | /usr/sbin/CRON \n2019/11/05 18:59:01\
  \ CMD: UID=0    PID=2222   | /bin/sh -c /root/bin/cleanup.pl >/dev/null 2>&1 \n"
created_at: '2019-11-06T00:02:27.757627+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# pspy Monitor Processes and Commands

```bash
pspy
```

## Expected Output

```
bob@host:$ ./pspy 
pspy - version: v1.2.0 - Commit SHA: 9c63e5d6c58f7bcdc235db663f5e3fe1c33b8855

     ██▓███    ██████  ██▓███ ▓██   ██▓
    ▓██░  ██▒▒██    ▒ ▓██░  ██▒▒██  ██▒
    ▓██░ ██▓▒░ ▓██▄   ▓██░ ██▓▒ ▒██ ██░
    ▒██▄█▓▒ ▒  ▒   ██▒▒██▄█▓▒ ▒ ░ ▐██▓░
    ▒██▒ ░  ░▒██████▒▒▒██▒ ░  ░ ░ ██▒▓░
    ▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░  ██▒▒▒ 
    ░▒ ░     ░ ░▒  ░ ░░▒ ░     ▓██ ░▒░ 
    ░░       ░  ░  ░  ░░       ▒ ▒ ░░  
                   ░           ░ ░     
                               ░ ░     

2019/11/05 18:58:44 CMD: UID=0    PID=1445   | /usr/sbin/vmtoolsd 
2019/11/05 18:58:44 CMD: UID=0    PID=14     | 
2019/11/05 18:58:44 CMD: UID=0    PID=1305   | /usr/sbin/rsyslogd
2019/11/05 18:59:01 CMD: UID=0    PID=2221   | /usr/sbin/CRON 
2019/11/05 18:59:01 CMD: UID=0    PID=2222   | /bin/sh -c /root/bin/cleanup.pl >/dev/null 2>&1 

```
