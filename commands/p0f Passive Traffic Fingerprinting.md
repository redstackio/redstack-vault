---
id: 4509bd7b-a62e-4dd0-899e-49661bcccf24
name: p0f Passive Traffic Fingerprinting
type: command
executor: bash
data: p0f -i $_INTERFACE -p -o $_OUTPUT.log
output: 'root@kali:~# p0f -i eth0 -p -o output.log

  --- p0f 3.09b by Michal Zalewski <lcamtuf@coredump.cx> ---

  [+] Closed 1 file descriptor.

  [+] Loaded 322 signatures from ''/etc/p0f/p0f.fp''.

  [+] Intercepting traffic on interface ''eth0''.

  [+] Default packet filtering configured [+VLAN].

  [+] Log file ''output.log'' opened for writing.

  [+] Entered main event loop.

  .-[ 10.10.10.11/57962 -> 10.10.10.10/199 (syn) ]-

  |

  | client   = 10.10.10.10/57962

  | app      = NMap SYN scan

  | dist     = <= 16

  | params   = random_ttl

  | raw_sig  = 4:48+16:0:1460:1024,0:mss::0

  ...

  ...'
created_at: '2019-09-12T18:07:35.196374+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# p0f Passive Traffic Fingerprinting

```bash
p0f -i $_INTERFACE -p -o $_OUTPUT.log
```

## Expected Output

```
root@kali:~# p0f -i eth0 -p -o output.log
--- p0f 3.09b by Michal Zalewski <lcamtuf@coredump.cx> ---

[+] Closed 1 file descriptor.
[+] Loaded 322 signatures from '/etc/p0f/p0f.fp'.
[+] Intercepting traffic on interface 'eth0'.
[+] Default packet filtering configured [+VLAN].
[+] Log file 'output.log' opened for writing.
[+] Entered main event loop.

.-[ 10.10.10.11/57962 -> 10.10.10.10/199 (syn) ]-
|
| client   = 10.10.10.10/57962
| app      = NMap SYN scan
| dist     = <= 16
| params   = random_ttl
| raw_sig  = 4:48+16:0:1460:1024,0:mss::0
...
...
```
