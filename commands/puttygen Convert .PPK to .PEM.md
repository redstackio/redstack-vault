---
id: 666616da-b594-46b2-964d-717c731df471
name: puttygen Convert .PPK to .PEM
type: command
executor: bash
data: puttygen $_KEY.ppk -O private-openssh -o $_KEY.pem
output: root@kali:~# puttygen private.ppk -O private-openssh -o private.pem
created_at: '2019-12-15T23:15:10.039400+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# puttygen Convert .PPK to .PEM

```bash
puttygen $_KEY.ppk -O private-openssh -o $_KEY.pem
```

## Expected Output

```
root@kali:~# puttygen private.ppk -O private-openssh -o private.pem
```


