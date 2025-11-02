---
id: 39018158-e103-41aa-a0e1-2b03fef209ee
name: Create a Netcat Listener
type: command
executor: bash
data: nc -lvnp $_PORT
output: 'root@kali:~# nc -lvnp 443

  Ncat: Version 7.80 ( https://nmap.org/ncat )

  Ncat: Listening on :::443

  Ncat: Listening on 0.0.0.0:443'
created_at: '2020-03-17T00:17:21.484805+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Netcat]]'
- '[[Nmap]]'
---

# Create a Netcat Listener

```bash
nc -lvnp $_PORT
```

## Expected Output

```
root@kali:~# nc -lvnp 443
Ncat: Version 7.80 ( https://nmap.org/ncat )
Ncat: Listening on :::443
Ncat: Listening on 0.0.0.0:443
```


