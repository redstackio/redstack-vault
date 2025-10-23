---
id: 1a3716fe-fe68-4141-99ae-3e3b346f0934
name: host Query a DNS Server for Name Servers
type: command
executor: ''
data: host -t ns $_TARGET_HOST
output: 'root@kali:~# host -t ns testsite.com

  testsite.com name server nsztm1.testsite.com.

  testsite.com name server nsztm2.testsite.com'
created_at: '2019-09-19T00:39:41.661335+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# host Query a DNS Server for Name Servers

```bash
host -t ns $_TARGET_HOST
```

## Expected Output

```
root@kali:~# host -t ns testsite.com
testsite.com name server nsztm1.testsite.com.
testsite.com name server nsztm2.testsite.com
```


