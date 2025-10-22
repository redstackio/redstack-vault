---
id: dccc3cd3-b8f0-41bb-9663-cd4f63f7fb5c
name: bruteforce webdirectories and files by extention
type: command
executor: bash
data: 'gobuster dir -u http://target-ip -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
  -x php,txt -t 30

  '
output: null
created_at: '2020-07-14T18:14:42.945355+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# bruteforce webdirectories and files by extention

```bash
gobuster dir -u http://target-ip -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,txt -t 30

```
