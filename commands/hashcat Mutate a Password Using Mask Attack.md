---
id: 3b9398f6-d668-4b69-863d-5fd65f5a1020
name: hashcat Mutate a Password Using Mask Attack
type: command
executor: ''
data: hashcat --stdout -a 3 $_BASE_PASSWORD?d?d?d?s > $_WORDLIST
output: "root@kali:~# hashcat --stdout -a 3 foobar?d?d?d?s > wordlist.txt\nroot@kali:~#\
  \ head wordlist.txt \nfoobar123.\nfoobar234.\nfoobar000.\nfoobar345.\nfoobar889*\n\
  foobar999*\nfoobar456.\nfoobar789*\nfoobar699*\nfoobar556."
created_at: '2019-09-24T22:00:40.482801+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Hashcat]]'
---

# hashcat Mutate a Password Using Mask Attack

```bash
hashcat --stdout -a 3 $_BASE_PASSWORD?d?d?d?s > $_WORDLIST
```

## Expected Output

```
root@kali:~# hashcat --stdout -a 3 foobar?d?d?d?s > wordlist.txt
root@kali:~# head wordlist.txt 
foobar123.
foobar234.
foobar000.
foobar345.
foobar889*
foobar999*
foobar456.
foobar789*
foobar699*
foobar556.
```


