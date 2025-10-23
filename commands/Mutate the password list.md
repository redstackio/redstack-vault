---
id: b5613680-e2ee-4aa4-b153-1910c03126b8
name: Mutate the password list
type: command
executor: bash
data: 'john --wordlist=$domain.txt --rules --stdout > $domain-mutated.txt

  '
output: null
created_at: '2020-07-14T18:14:45.643199+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Mutate the password list

```bash
john --wordlist=$domain.txt --rules --stdout > $domain-mutated.txt

```


