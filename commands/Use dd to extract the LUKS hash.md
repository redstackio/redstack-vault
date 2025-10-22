---
id: 18069d74-ae8e-4391-a7b1-df39c745e801
name: Use dd to extract the LUKS hash
type: command
executor: null
data: dd if=encrypted.img of=luks.hash bs=512 count=4097
output: null
created_at: '2019-09-11T22:47:55.914436+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Use dd to extract the LUKS hash

```bash
dd if=encrypted.img of=luks.hash bs=512 count=4097
```
