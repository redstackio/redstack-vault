---
id: 2cd5d0e0-202a-439d-a9e1-5d3ff1e62daf
name: Hashcat Mutate a Wordlist Using Rules
type: command
executor: bash
data: hashcat -a 0 words.txt --stdout -r rules.txt > $_OUTPUT.txt
output: "root@kali:~# hashcat -a 0 words.txt --stdout -r rules.txt \nDavidson\nnosdivaD\n\
  vidsonDa\nDavidson1985\n321Davidson\nDAVIDSON\npassword\ndrowssap\nsswordpa\npassword1985\n\
  321password\nPASSWORD\n"
created_at: '2019-10-18T00:45:16.427214+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Hashcat]]'
---

# Hashcat Mutate a Wordlist Using Rules

```bash
hashcat -a 0 words.txt --stdout -r rules.txt > $_OUTPUT.txt
```

## Expected Output

```
root@kali:~# hashcat -a 0 words.txt --stdout -r rules.txt 
Davidson
nosdivaD
vidsonDa
Davidson1985
321Davidson
DAVIDSON
password
drowssap
sswordpa
password1985
321password
PASSWORD

```


