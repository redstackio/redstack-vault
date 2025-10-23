---
id: f8baba70-36aa-4ba8-91ec-da667f4483aa
name: Netcat Upload a File with a Listener
type: command
executor: bash
data: nc -lvnp $_PORT < $_FILENAME
output: 'nc -lvnp 443 < /etc/passwd

  Ncat: Version 7.80 ( https://nmap.org/ncat )

  Ncat: Listening on :::443

  Ncat: Listening on 0.0.0.0:443'
created_at: '2019-10-29T22:25:12.709976+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Netcat Upload a File with a Listener

```bash
nc -lvnp $_PORT < $_FILENAME
```

## Expected Output

```
nc -lvnp 443 < /etc/passwd
Ncat: Version 7.80 ( https://nmap.org/ncat )
Ncat: Listening on :::443
Ncat: Listening on 0.0.0.0:443
```


