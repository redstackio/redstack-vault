---
id: 43e757fe-1c68-4d56-8029-f4c75d19ccdc
name: Gobuster Command to Find Existent Directories
type: command
executor: ''
data: gobuster -w list.txt -u http://192.168.1.11/vcart/
output: 'Gobuster v1.4.1              OJ Reeves (@TheColonial)

  =====================================================

  =====================================================

  [+] Mode         : dir

  [+] Url/Domain   : http://192.168.1.11/vcart/

  [+] Threads      : 10

  [+] Wordlist     : list.txt

  [+] Status codes : 307,200,204,301,302

  =====================================================

  /js (Status: 301)

  /images (Status: 301)

  /admin (Status: 301)

  ====================================================='
created_at: '2020-08-31T18:06:27.192074+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Gobuster]]'
- '[[dir]]'
- '[[find]]'
---

# Gobuster Command to Find Existent Directories

```bash
gobuster -w list.txt -u http://192.168.1.11/vcart/
```

## Expected Output

```
Gobuster v1.4.1              OJ Reeves (@TheColonial)
=====================================================
=====================================================
[+] Mode         : dir
[+] Url/Domain   : http://192.168.1.11/vcart/
[+] Threads      : 10
[+] Wordlist     : list.txt
[+] Status codes : 307,200,204,301,302
=====================================================
/js (Status: 301)
/images (Status: 301)
/admin (Status: 301)
=====================================================
```


