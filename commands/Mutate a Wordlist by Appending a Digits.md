---
id: 6ddbb863-04bb-44ca-951c-78e01b4370ef
name: Mutate a Wordlist by Appending a Digits
type: command
executor: ''
data: hashcat -a 6 --stdout $_WORDLIST ?d > $_WORDLIST.mutated
output: root@kali:~# hashcat -a 6 --stdout wordlist.txt  ?d > output.txt
created_at: '2020-03-18T23:35:23.625297+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Mutate a Wordlist by Appending a Digits

```bash
hashcat -a 6 --stdout $_WORDLIST ?d > $_WORDLIST.mutated
```

## Expected Output

```
root@kali:~# hashcat -a 6 --stdout wordlist.txt  ?d > output.txt
```
