---
id: 2b0adb8b-027d-4708-82e1-78f7db1265e5
name: dnsenum Brute Force DNS Subdomains
type: command
executor: ''
data: dnsenum -r $_TARGET_DOMAIN -f $_DICTIONARY
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
  \          7200     IN    MX               10\n\nBrute forcing with words.txt:\n\
  ______________________________\n\nowa.testsite.com                300    IN    \
  \ A         109.64.224.85\nintns1.testsite.com             86400  IN     A     \
  \    82.64.74.22\nvpn.testsite.com                28800  IN     A         188.24.86.169\n\
  www.testsite.com                86430  IN     A         3.23.54.21\n"
created_at: '2019-09-20T18:53:20.016940+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# dnsenum Brute Force DNS Subdomains

```bash
dnsenum -r $_TARGET_DOMAIN -f $_DICTIONARY
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

Brute forcing with words.txt:
______________________________

owa.testsite.com                300    IN     A         109.64.224.85
intns1.testsite.com             86400  IN     A         82.64.74.22
vpn.testsite.com                28800  IN     A         188.24.86.169
www.testsite.com                86430  IN     A         3.23.54.21

```
