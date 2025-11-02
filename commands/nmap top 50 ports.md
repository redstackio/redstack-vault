---
id: 5835d697-606f-48b4-bf17-80a993b5d558
name: nmap top 50 ports
type: command
executor: ''
data: nmap -PN -sV --top-ports 50 --open $IPRANGE
output: nmap -PN -sV --top-ports 50 --open 192.168.1.0/24
created_at: '2023-01-11T19:54:18.094938+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Nmap]]'
---

# nmap top 50 ports

```bash
nmap -PN -sV --top-ports 50 --open $IPRANGE
```

## Expected Output

```
nmap -PN -sV --top-ports 50 --open 192.168.1.0/24
```


