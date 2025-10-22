---
id: e0e0534d-9f84-4fd5-abea-0829e874617e
name: Altdns permutation
type: command
executor: bash
data: 'WORDLIST_PERMUTATION="./Altdns/words.txt"

  python2.7 ./Altdns/altdns.py -i /tmp/inputdomains.txt -o /tmp/out.txt -w $WORDLIST_PERMUTATION'
output: null
created_at: '2023-04-06T03:56:25.662999+00:00'
updated_at: '2023-04-10T20:25:36.373522+00:00'
---

# Altdns permutation

```bash
WORDLIST_PERMUTATION="./Altdns/words.txt"
python2.7 ./Altdns/altdns.py -i /tmp/inputdomains.txt -o /tmp/out.txt -w $WORDLIST_PERMUTATION
```
