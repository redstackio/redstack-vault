---
id: 66d0dee8-4b7d-4d06-83de-02c8fa448cd1
name: Mutate a Wordlist with Alphanumeric and Special Characters
type: command
executor: bash
data: hashcat -a 6 --stdout $_WORDLIST ?a?a > $_WORDLIST.mutated
output: root@kali:~# hashcat -a 6 --stdout words.txt ?a?a > mutated.words.txt
created_at: '2019-10-09T18:38:08.468857+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Hashcat]]'
---

# Mutate a Wordlist with Alphanumeric and Special Characters

```bash
hashcat -a 6 --stdout $_WORDLIST ?a?a > $_WORDLIST.mutated
```

## Expected Output

```
root@kali:~# hashcat -a 6 --stdout words.txt ?a?a > mutated.words.txt
```


