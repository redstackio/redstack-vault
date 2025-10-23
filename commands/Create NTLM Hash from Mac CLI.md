---
id: 1d221e35-25a0-49a7-abd3-223fc19f97ea
name: Create NTLM Hash from Mac CLI
type: command
executor: bash
data: 'echo -n password | iconv -t UTF-16LE | openssl md4

  '
output: null
created_at: '2020-07-14T18:21:12.928765+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Create NTLM Hash from Mac CLI

```bash
echo -n password | iconv -t UTF-16LE | openssl md4

```


