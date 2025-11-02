---
id: 7d25831d-b45d-4548-8898-410456010c32
name: Nmap HTTP Methods Script
type: command
executor: nmap
data: nmap --script http-methods demo.testfire.net
output: 'PORT   STATE SERVICE REASON

  80/tcp open  http    syn-ack

  | http-methods:

  |_  Supported Methods: GET HEAD POST OPTIONS TRACE'
created_at: '2020-07-19T06:50:16.838896+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Nmap]]'
---

# Nmap HTTP Methods Script

```nmap
nmap --script http-methods demo.testfire.net
```

## Expected Output

```
PORT   STATE SERVICE REASON
80/tcp open  http    syn-ack
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS TRACE
```


