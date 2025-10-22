---
id: 428fcd77-5685-4824-83c6-ae15b4aedab3
name: John the Ripper Mutate a Password List Using Rules
type: command
executor: ''
data: john --wordlist=$_WORDLIST --rules --stdout > $_MUTATED_WORDLIST
output: "root@kali:~# john --wordlist=wordlist.txt --rules --stdout > mutated.wordlist.txt\n\
  Press 'q' or Ctrl-C to abort, almost any other key for status\n500p 0:00:00:00 100.00%\
  \ (2019-09-24 17:49) 16666p/s Portsing\nroot@kali:~# wc -w mutated.wordlist.txt\
  \ wordlist.txt\n 500 mutated.wordlist.txt\n  10 wordlist.txt\n 510 total"
created_at: '2019-09-24T22:00:40.479915+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# John the Ripper Mutate a Password List Using Rules

```bash
john --wordlist=$_WORDLIST --rules --stdout > $_MUTATED_WORDLIST
```

## Expected Output

```
root@kali:~# john --wordlist=wordlist.txt --rules --stdout > mutated.wordlist.txt
Press 'q' or Ctrl-C to abort, almost any other key for status
500p 0:00:00:00 100.00% (2019-09-24 17:49) 16666p/s Portsing
root@kali:~# wc -w mutated.wordlist.txt wordlist.txt
 500 mutated.wordlist.txt
  10 wordlist.txt
 510 total
```
