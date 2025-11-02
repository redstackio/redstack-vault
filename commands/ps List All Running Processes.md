---
id: 6aaac1ca-041c-41ee-b21a-b5fc134b6989
name: ps List All Running Processes
type: command
executor: bash
data: ps aux
output: "bob@host:~$ ps aux\n\nUSER        PID %CPU %MEM    VSZ   RSS TTY      STAT\
  \ START   TIME COMMAND                              \nroot          1  0.0  0.2\
  \  24432  2416 ?        Ss   08:56   0:00 /sbin/init                           \n\
  root          2  0.0  0.0      0     0 ?        S    08:56   0:00 [kthreadd]  \n\
  root       1839  0.0  0.0      0     0 ?        S    09:17   0:00 [kworker/0:1]\n\
  root       1852  0.0  0.0      0     0 ?        S    09:22   0:00 [kworker/0:2]\n\
  www-data   1965  0.0  0.8 113992  8636 ?        S    09:25   0:00 /usr/sbin/apache2\
  \ -k start\nwww-data   2414  0.0  0.8 113884  8680 ?        S    09:28   0:00 /usr/sbin/apache2\
  \ -k start\nwww-data   2415  0.0  0.8 113868  8452 ?        S    09:28   0:00 /usr/sbin/apache2\
  \ -k start"
created_at: '2019-11-25T19:44:10.696221+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[host]]'
- '[[ps]]'
---

# ps List All Running Processes

```bash
ps aux
```

## Expected Output

```
bob@host:~$ ps aux

USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND                              
root          1  0.0  0.2  24432  2416 ?        Ss   08:56   0:00 /sbin/init                           
root          2  0.0  0.0      0     0 ?        S    08:56   0:00 [kthreadd]  
root       1839  0.0  0.0      0     0 ?        S    09:17   0:00 [kworker/0:1]
root       1852  0.0  0.0      0     0 ?        S    09:22   0:00 [kworker/0:2]
www-data   1965  0.0  0.8 113992  8636 ?        S    09:25   0:00 /usr/sbin/apache2 -k start
www-data   2414  0.0  0.8 113884  8680 ?        S    09:28   0:00 /usr/sbin/apache2 -k start
www-data   2415  0.0  0.8 113868  8452 ?        S    09:28   0:00 /usr/sbin/apache2 -k start
```


