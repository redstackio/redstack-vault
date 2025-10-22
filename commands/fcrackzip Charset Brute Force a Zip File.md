---
id: e56b64f1-2f50-4a0e-879d-11a928ad5b0e
name: fcrackzip Charset Brute Force a Zip File
type: command
executor: ''
data: fcrackzip -b -c '$_CHAR1$_CHAR2' -l $_MIN_SIZE-$_MAX_SIZE -u  $_WORDLIST
output: "root@kali:~# fcrackzip -b -c 'a1' -l 3-4 -u secret.zip \n\n\nPASSWORD FOUND!!!!:\
  \ pw == 5555"
created_at: '2019-09-24T22:44:39.881514+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# fcrackzip Charset Brute Force a Zip File

```bash
fcrackzip -b -c '$_CHAR1$_CHAR2' -l $_MIN_SIZE-$_MAX_SIZE -u  $_WORDLIST
```

## Expected Output

```
root@kali:~# fcrackzip -b -c 'a1' -l 3-4 -u secret.zip 

PASSWORD FOUND!!!!: pw == 5555
```
