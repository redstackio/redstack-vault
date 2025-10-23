---
id: 3ce20c20-0472-4455-9d20-6ad15b039219
name: fcrackzip Dictionary Brute Force a Zip File
type: command
executor: bash
data: fcrackzip -v -u $FILENAME -D -p $WORDLIST
output: "root@kali:~# fcrackzip -v -u secret.zip -D -p /usr/share/wordlists/rockyou.txt\
  \ \nfound file 'id_rsa', (size cp/uc   1379/  1811, flags 9, chk 930e)\n\n\nPASSWORD\
  \ FOUND!!!!: pw == princess1"
created_at: '2019-09-24T22:44:39.876065+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# fcrackzip Dictionary Brute Force a Zip File

```bash
fcrackzip -v -u $FILENAME -D -p $WORDLIST
```

## Expected Output

```
root@kali:~# fcrackzip -v -u secret.zip -D -p /usr/share/wordlists/rockyou.txt 
found file 'id_rsa', (size cp/uc   1379/  1811, flags 9, chk 930e)


PASSWORD FOUND!!!!: pw == princess1
```


