---
id: 1bebc11b-c88f-4573-b1c2-7e61e1170b55
name: wfuzz
type: cheatsheet
verified: false
created_at: '2020-07-14T18:15:01.580936+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# wfuzz



**Command** ([[bruteforce web parameter]]):

```bash
wfuzz -u http://target-ip/path/index.php?param=FUZZ -w /usr/share/wordlists/rockyou.txt

```







**Command** ([[bruteforce post data (login)]]):

```bash
wfuzz -u http://target-ip/path/index.php?action=authenticate -d 'username=admin&password=FUZZ' -w /usr/share/wordlists/rockyou.txt

```






