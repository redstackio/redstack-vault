---
id: b13d8add-e7d2-4c14-a8b9-26f59c2c76d0
name: Nmap Command to Find Trace Method
type: command
executor: ''
data: nmap --script http-trace -p80 192.168.1.3
output: 'Starting Nmap 7.70 ( https://nmap.org ) at 2020-09-01 15:14 IST

  Nmap scan report for 192.168.1.3

  Host is up (0.00048s latency).

  PORT   STATE SERVICE

  80/tcp open  http

  |_http-trace: TRACE is enabled'
created_at: '2020-09-01T16:56:54.515251+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Command to Find Trace Method

```bash
nmap --script http-trace -p80 192.168.1.3
```

## Expected Output

```
Starting Nmap 7.70 ( https://nmap.org ) at 2020-09-01 15:14 IST
Nmap scan report for 192.168.1.3
Host is up (0.00048s latency).

PORT   STATE SERVICE
80/tcp open  http
|_http-trace: TRACE is enabled
```
