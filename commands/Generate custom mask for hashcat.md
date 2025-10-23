---
id: 4f3af83a-188a-4125-9881-6120675c4acc
name: Generate custom mask for hashcat
type: command
executor: bash
data: '$ python2 statsgen.py ../hashcat.potfile -o hashcat.mask

  $ python2 maskgen.py hashcat.mask --targettime 3600 --optindex -q -o hashcat_1H.hcmask'
output: null
created_at: '2023-04-06T03:56:04.096865+00:00'
updated_at: '2023-04-10T20:26:22.286747+00:00'
---

# Generate custom mask for hashcat

```bash
$ python2 statsgen.py ../hashcat.potfile -o hashcat.mask
$ python2 maskgen.py hashcat.mask --targettime 3600 --optindex -q -o hashcat_1H.hcmask
```


