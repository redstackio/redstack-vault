---
id: c6cecdaa-c0de-4d93-a247-8030bcf0950f
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:25.662893+00:00'
updated_at: '2023-04-10T20:25:36.373961+00:00'
---

# Code Snippet c6cecdaa

**Language**: Powershell

```powershell
WORDLIST_PERMUTATION="./Altdns/words.txt"
python2.7 ./Altdns/altdns.py -i /tmp/inputdomains.txt -o /tmp/out.txt -w $WORDLIST_PERMUTATION
```


