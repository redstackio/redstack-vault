---
id: 4db2ada1-febb-4c14-a715-b99c2e8189ff
name: ncat reverse shell output
type: command
executor: ''
data: ncat -lvp 9999
output: 'Ncat: Version 7.80 ( https://nmap.org/ncat )

  Ncat: Listening on :::9999

  Ncat: Listening on 0.0.0.0:9999

  Ncat: Connection from 192.168.11.7.

  Ncat: Connection from 192.168.11.7:56753.'
created_at: '2020-08-01T18:06:44.460210+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# ncat reverse shell output

```bash
ncat -lvp 9999
```

## Expected Output

```
Ncat: Version 7.80 ( https://nmap.org/ncat )
Ncat: Listening on :::9999
Ncat: Listening on 0.0.0.0:9999
Ncat: Connection from 192.168.11.7.
Ncat: Connection from 192.168.11.7:56753.
```


