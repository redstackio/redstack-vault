---
id: 1e5cd029-2df5-4bd0-85e7-0767dc9516c5
name: host Attempt a DNS Zone Transfer and List All Records
type: command
executor: ''
data: host -a -l $_DOMAIN_NAME $_TARGET_HOST
output: "root@kali:~# host -a -l testsite.com nsztm2.testsite.com.\n\nTrying \"testsite.com\"\
  \nUsing domain server:\nName: nsztm2.testsite.com.\nAddress: 34.225.33.2#53\nAliases:\n\
  \n;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 38338\n;; flags: qr aa; QUERY:\
  \ 1, ANSWER: 48, AUTHORITY: 0, ADDITIONAL: 0\n\n;; QUESTION SECTION:\n;testsite.com.\
  \               IN      AXFR\n\ntestsite.com.        7200    IN      MX      0 \
  \ MX1.TESTSITE.COM. \ntestsite.com.        7200    IN      MX      10 MX2.TESTSITE.COM.\
  \ \noffice.testsite.com. 7200    IN      A       192.178.50.101\nowa.testsite.com.\
  \    7200    IN      A       192.178.50.102\ndev.testsite.com.     302    IN   \
  \   TXT     \"development\"\n\n\nReceived 1864 bytes from 34.225.33.2#53 in 105\
  \ ms"
created_at: '2019-09-19T00:39:41.673772+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[host]]'
---

# host Attempt a DNS Zone Transfer and List All Records

```bash
host -a -l $_DOMAIN_NAME $_TARGET_HOST
```

## Expected Output

```
root@kali:~# host -a -l testsite.com nsztm2.testsite.com.

Trying "testsite.com"
Using domain server:
Name: nsztm2.testsite.com.
Address: 34.225.33.2#53
Aliases:

;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 38338
;; flags: qr aa; QUERY: 1, ANSWER: 48, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;testsite.com.               IN      AXFR

testsite.com.        7200    IN      MX      0  MX1.TESTSITE.COM. 
testsite.com.        7200    IN      MX      10 MX2.TESTSITE.COM. 
office.testsite.com. 7200    IN      A       192.178.50.101
owa.testsite.com.    7200    IN      A       192.178.50.102
dev.testsite.com.     302    IN      TXT     "development"


Received 1864 bytes from 34.225.33.2#53 in 105 ms
```


