---
id: a50e5264-3dfb-4fcb-8ad2-96f8bb4ea3ef
name: CEWL Generate a Password List Using a Website's Content
type: command
executor: bash
data: cewl $_TARGET_IP -d $_DEPTH -m $_MAX_SIZE -w $_WORDLIST
output: 'root@kali:~# cewl -d 2 -m 5 http://10.10.10.10 -w  words.txt

  CeWL 5.4.3 (Arkanoid) Robin Wood (robin@digi.ninja) (https://digi.ninja/)'
created_at: '2019-09-24T22:00:40.485122+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[CeWL]]'
---

# CEWL Generate a Password List Using a Website's Content

```bash
cewl $_TARGET_IP -d $_DEPTH -m $_MAX_SIZE -w $_WORDLIST
```

## Expected Output

```
root@kali:~# cewl -d 2 -m 5 http://10.10.10.10 -w  words.txt
CeWL 5.4.3 (Arkanoid) Robin Wood (robin@digi.ninja) (https://digi.ninja/)
```


