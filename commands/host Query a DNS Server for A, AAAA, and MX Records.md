---
id: 79caf226-249e-41a9-a9a0-3711912924c7
name: host Query a DNS Server for A, AAAA, and MX Records
type: command
executor: ''
data: host $_TARGET_HOST
output: 'root@kali:~# host testsite.com

  testsite.com mail is handled by 10 MX1.TESTSITE.COM.

  testsite.com mail is handled by 10 MX2.TESTSITE.COM.'
created_at: '2019-09-19T00:39:41.647028+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# host Query a DNS Server for A, AAAA, and MX Records

```bash
host $_TARGET_HOST
```

## Expected Output

```
root@kali:~# host testsite.com
testsite.com mail is handled by 10 MX1.TESTSITE.COM.
testsite.com mail is handled by 10 MX2.TESTSITE.COM.
```
