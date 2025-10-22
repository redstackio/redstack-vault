---
id: bcd3a873-4866-4024-8b1c-d7fcffc05f36
name: Directory Brute Force
type: command
executor: bash
data: gobuster dir -u http://evil-website.tld -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
  -x php,html
output: null
created_at: '2023-04-06T03:56:31.692963+00:00'
updated_at: '2023-04-10T20:23:06.681072+00:00'
---

# Directory Brute Force

```bash
gobuster dir -u http://evil-website.tld -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html
```
