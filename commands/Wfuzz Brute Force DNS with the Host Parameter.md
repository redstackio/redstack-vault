---
id: 786edeca-ad67-400a-9890-0a9848f5be77
name: Wfuzz Brute Force DNS with the Host Parameter
type: command
executor: bash
data: 'wfuzz --hc 404 -c -w $_WORDLIST -u http://$_TARGET_IP -H ''Host: FUZZ.$_DOMAIN'''
output: "root@kali:~# wfuzz --hc 404 -c -w fierce-hostlist.txt -u http://10.10.10.10\
  \ -H 'Host: FUZZ.testcorp.net'\n\n********************************************************\n\
  * Wfuzz 2.3.4 - The Web Fuzzer                         *\n********************************************************\n\
  \nTarget: http://10.10.10.10/\nTotal requests: 2280\n\n==================================================================\n\
  ID   Response   Lines      Word         Chars          Payload    \n==================================================================\n\
  \n001158:  C=403     29 L\t      92 W\t   1233 Ch\t  \"member\"\n\nTotal time: 17.08417\n\
  Processed Requests: 2280\nFiltered Requests: 2279\nRequests/sec.: 133.4568\n"
created_at: '2019-10-17T21:12:55.974250+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Wfuzz Brute Force DNS with the Host Parameter

```bash
wfuzz --hc 404 -c -w $_WORDLIST -u http://$_TARGET_IP -H 'Host: FUZZ.$_DOMAIN'
```

## Expected Output

```
root@kali:~# wfuzz --hc 404 -c -w fierce-hostlist.txt -u http://10.10.10.10 -H 'Host: FUZZ.testcorp.net'

********************************************************
* Wfuzz 2.3.4 - The Web Fuzzer                         *
********************************************************

Target: http://10.10.10.10/
Total requests: 2280

==================================================================
ID   Response   Lines      Word         Chars          Payload    
==================================================================

001158:  C=403     29 L	      92 W	   1233 Ch	  "member"

Total time: 17.08417
Processed Requests: 2280
Filtered Requests: 2279
Requests/sec.: 133.4568

```
