---
id: 907a97a2-9d1c-4620-b51b-34d57d8cb938
name: login with older ciphers
type: command
executor: bash
data: 'ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -c aes128-cbc username@target-ip

  '
output: null
created_at: '2020-07-14T18:14:34.725553+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# login with older ciphers

```bash
ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -c aes128-cbc username@target-ip

```
