---
id: 6bd00f85-25fe-4baf-9e7d-569c03046611
name: Netcat Download a File with a Listener
type: command
executor: bash
data: nc -lvnp $_PORT > $_FILENAME
output: 'nc -lvnp 443 > foo

  Ncat: Version 7.80 ( https://nmap.org/ncat )

  Ncat: Listening on :::443

  Ncat: Listening on 0.0.0.0:443'
created_at: '2019-10-29T22:25:12.732336+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Netcat Download a File with a Listener

```bash
nc -lvnp $_PORT > $_FILENAME
```

## Expected Output

```
nc -lvnp 443 > foo
Ncat: Version 7.80 ( https://nmap.org/ncat )
Ncat: Listening on :::443
Ncat: Listening on 0.0.0.0:443
```


