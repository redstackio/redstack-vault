---
id: d00c3b56-7bcb-4183-9733-6d25428faf90
name: cryptsetup Open a LUKS Encrypted Volume
type: command
executor: bash
data: cryptsetup luksOpen $_FILE.img $_CRYPT
output: 'root@kali:~# cryptsetup luksOpen backup.img crypt-backup

  Enter passphrase for backup.img:'
created_at: '2019-10-17T20:33:29.004611+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# cryptsetup Open a LUKS Encrypted Volume

```bash
cryptsetup luksOpen $_FILE.img $_CRYPT
```

## Expected Output

```
root@kali:~# cryptsetup luksOpen backup.img crypt-backup
Enter passphrase for backup.img:
```


