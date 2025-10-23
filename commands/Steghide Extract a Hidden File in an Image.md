---
id: 9ebf17c1-858d-4ddc-8f97-4c48229f2000
name: Steghide Extract a Hidden File in an Image
type: command
executor: bash
data: steghide extract -sf $_COVER
output: "root@kali:~# steghide extract -sf wallpaper.jpg \nEnter passphrase: \nwrote\
  \ extracted data to \"id_rsa.pub\"."
created_at: '2019-10-10T00:34:20.345057+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Steghide Extract a Hidden File in an Image

```bash
steghide extract -sf $_COVER
```

## Expected Output

```
root@kali:~# steghide extract -sf wallpaper.jpg 
Enter passphrase: 
wrote extracted data to "id_rsa.pub".
```


