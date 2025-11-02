---
id: 151f2192-b29a-461a-bea9-a7dc29e5931f
name: host Attempt a DNS Zone Transfer
type: command
executor: bash
data: host -l $_DOMAIN_NAME $_TARGET_HOST
output: "root@kali:~# host -l testsite.com nsztm1.testsite.com\nUsing domain server:\n\
  Name: nsztm1.testsite.com\nAddress: 192.178.50.100#53\nAliases: \n\ntestsite.com\
  \ has address 192.178.50.100\ntestsite.com name server nsztm1.testsite.com.\ntestsite.com\
  \ name server nsztm2.testsite.com."
created_at: '2019-09-19T00:39:41.674085+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[host]]'
---

# host Attempt a DNS Zone Transfer

```bash
host -l $_DOMAIN_NAME $_TARGET_HOST
```

## Expected Output

```
root@kali:~# host -l testsite.com nsztm1.testsite.com
Using domain server:
Name: nsztm1.testsite.com
Address: 192.178.50.100#53
Aliases: 

testsite.com has address 192.178.50.100
testsite.com name server nsztm1.testsite.com.
testsite.com name server nsztm2.testsite.com.
```


