---
id: 6aaac1ca-041c-41ee-b21a-b5fc134b6989
name: ps-list-all-running-processes
type: command
executor: bash
data: ps aux
output: >-
  USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME
  COMMAND                              

  root          1  0.0  0.2  24432  2416 ?        Ss   08:56   0:00
  /sbin/init                           

  root          2  0.0  0.0      0     0 ?        S    08:56   0:00 [kthreadd]  

  root       1839  0.0  0.0      0     0 ?        S    09:17   0:00
  [kworker/0:1]

  root       1852  0.0  0.0      0     0 ?        S    09:22   0:00
  [kworker/0:2]

  www-data   1965  0.0  0.8 113992  8636 ?        S    09:25   0:00
  /usr/sbin/apache2 -k start

  www-data   2414  0.0  0.8 113884  8680 ?        S    09:28   0:00
  /usr/sbin/apache2 -k start

  www-data   2415  0.0  0.8 113868  8452 ?        S    09:28   0:00
  /usr/sbin/apache2 -k start
created_at: '2019-11-25T19:44:10.696221+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - process
  - enumeration
verified: true
validated: true
---

# ps-list-all-running-processes

## Command

```bash
ps aux
```

## Description

Lists all running processes on the system with detailed information, including the user owning the process, PID, CPU and memory usage, virtual memory size (VSZ), resident set size (RSS), terminal (TTY), process state (STAT), start time, CPU time, and the full command line. This is useful for enumerating active processes during reconnaissance or debugging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| a | Lift the BSD-style "only yourself" restriction, which is imposed upon the set of all processes when some BSD-style (without "-") options are used or when the ps personality setting is BSD-like. The set of processes selected in this manner is in addition to the set of processes selected by other means. | Built-in |
| u | Display user-oriented format. | Built-in |
| x | Lift the BSD-style "must have a tty" restriction, which is imposed upon the set of all processes when some BSD-style (without "-") options are used or when the ps personality setting is BSD-like. | Built-in |

## Examples

### Basic Usage

```bash
ps aux
```

### Advanced Usage

```bash
ps aux | grep apache
```

## Expected Output

A tabular output showing process details:

USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND                              
root          1  0.0  0.2  24432  2416 ?        Ss   08:56   0:00 /sbin/init                           
root          2  0.0  0.0      0     0 ?        S    08:56   0:00 [kthreadd]  
root       1839  0.0  0.0      0     0 ?        S    09:17   0:00 [kworker/0:1]
root       1852  0.0  0.0      0     0 ?        S    09:22   0:00 [kworker/0:2]
www-data   1965  0.0  0.8 113992  8636 ?        S    09:25   0:00 /usr/sbin/apache2 -k start
www-data   2414  0.0  0.8 113884  8680 ?        S    09:28   0:00 /usr/sbin/apache2 -k start
www-data   2415  0.0  0.8 113868  8452 ?        S    09:28   0:00 /usr/sbin/apache2 -k start

## Related

- [[procedures/list-running-processes]]
