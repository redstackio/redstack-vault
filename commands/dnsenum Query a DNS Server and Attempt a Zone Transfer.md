---
id: baf65f95-02ed-4fe8-81e5-32b801ce7b5e
name: dnsenum Query a DNS Server and Attempt a Zone Transfer
type: command
executor: bash
data: dnsenum $_TARGET_DOMAIN
output: "root@kali:~# dnsenum testsite.com\ndnsenum VERSION:1.2.4\n\n-----   testsite.com\
  \   -----\n\n\nHost's addresses:\n__________________\n\ntestsite.com.          \
  \               7199     IN    A      203.22.87.231 \n\n\nName Servers:\n______________\n\
  \nnsztm2.testsite.com.                     10799    IN    A        203.22.87.231\n\
  nsztm1.testsite.com.                     10799    IN    A        203.22..88.232\n\
  \n\nTrying Zone Transfers and getting Bind Versions:\n_________________________________________________\n\
  \n\nTrying Zone Transfer for testsite.com on nsztm2.testsite.com ...\ntestsite.com.\
  \                         7200     IN    SOA               (\ntestsite.com.    \
  \                     300      IN    HINFO        \"Casio\ntestsite.com.       \
  \                  301      IN    TXT               (\ntestsite.com.           \
  \              7200     IN    MX                0\ntestsite.com.               \
  \          7200     IN    MX               10\n\nbrute force file not specified,\
  \ bay.\n"
created_at: '2019-09-20T18:53:20.008696+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# dnsenum Query a DNS Server and Attempt a Zone Transfer

```bash
dnsenum $_TARGET_DOMAIN
```

## Expected Output

```
root@kali:~# dnsenum testsite.com
dnsenum VERSION:1.2.4

-----   testsite.com   -----


Host's addresses:
__________________

testsite.com.                         7199     IN    A      203.22.87.231 


Name Servers:
______________

nsztm2.testsite.com.                     10799    IN    A        203.22.87.231
nsztm1.testsite.com.                     10799    IN    A        203.22..88.232


Trying Zone Transfers and getting Bind Versions:
_________________________________________________


Trying Zone Transfer for testsite.com on nsztm2.testsite.com ...
testsite.com.                         7200     IN    SOA               (
testsite.com.                         300      IN    HINFO        "Casio
testsite.com.                         301      IN    TXT               (
testsite.com.                         7200     IN    MX                0
testsite.com.                         7200     IN    MX               10

brute force file not specified, bay.

```


