---
id: 47a74aa6-9738-48d9-a46a-9b0a8107cfbd
name: hashcat Crack mscachev2 format (extremely slow)
type: command
executor: bash
data: 'hashcat -m 2100 -a 0 mscachev2.dump ./wordlists/* -r rules/dive.rule

  '
output: null
created_at: '2020-07-14T18:21:34.529683+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# hashcat Crack mscachev2 format (extremely slow)

```bash
hashcat -m 2100 -a 0 mscachev2.dump ./wordlists/* -r rules/dive.rule

```
