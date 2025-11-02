---
id: f9216db1-e39e-4235-9415-1120d98e2577
name: host Query a DNS Server for Mail Servers
type: command
executor: ''
data: host -t mx $_TARGET_HOST
output: 'root@kali:~# host -t mx testsite.com

  testsite.com mail is handled by 10 MX1.TESTSITE.COM.

  testsite.com mail is handled by 10 MX2.TESTSITE.COM.'
created_at: '2019-09-19T00:39:41.661794+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[host]]'
---

# host Query a DNS Server for Mail Servers

```bash
host -t mx $_TARGET_HOST
```

## Expected Output

```
root@kali:~# host -t mx testsite.com
testsite.com mail is handled by 10 MX1.TESTSITE.COM.
testsite.com mail is handled by 10 MX2.TESTSITE.COM.
```


