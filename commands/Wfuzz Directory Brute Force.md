---
id: 583fd646-28c6-4614-9ee3-fd82b366694a
name: Wfuzz Directory Brute Force
type: command
executor: bash
data: wfuzz --hc 404 -c -w common.txt -u http://$_TARGET_IP/FUZZ
output: "root@kali:~# wfuzz --hc 404 -c -w common.txt -u http://10.10.10.10/FUZZ\n\
  \n********************************************************\n* Wfuzz 2.3.3 - The\
  \ Web Fuzzer                         *\n********************************************************\n\
  \nTarget: http://10.10.10.10/FUZZ\nTotal requests: 4594\n\n==================================================================\n\
  ID   Response   Lines      Word         Chars          Payload    \n==================================================================\n\
  \n000010:  C=403      9 L\t      28 W\t    276 Ch\t  \".hta\"\n000011:  C=403  \
  \    9 L\t      28 W\t    276 Ch\t  \".htaccess\"\n000012:  C=403      9 L\t   \
  \   28 W\t    276 Ch\t  \".htpasswd\"\n000573:  C=301      9 L\t      28 W\t   \
  \ 308 Ch\t  \"api\"\n000706:  C=301      9 L\t      28 W\t    312 Ch\t  \"backups\"\
  \n001348:  C=301      9 L\t      28 W\t    308 Ch\t  \"dev\"\n002094:  C=200   \
  \ 375 L\t     964 W\t  10918 Ch\t  \"index.html\"\n003598:  C=403      9 L\t   \
  \   28 W\t    276 Ch\t  \"server-status\"\n004244:  C=301      9 L\t      28 W\t\
  \    308 Ch\t  \"var\"\n\nTotal time: 5.518419\nProcessed Requests: 4594\nFiltered\
  \ Requests: 4585\nRequests/sec.: 832.4847"
created_at: '2019-09-13T23:40:37.674346+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Wfuzz Directory Brute Force

```bash
wfuzz --hc 404 -c -w common.txt -u http://$_TARGET_IP/FUZZ
```

## Expected Output

```
root@kali:~# wfuzz --hc 404 -c -w common.txt -u http://10.10.10.10/FUZZ

********************************************************
* Wfuzz 2.3.3 - The Web Fuzzer                         *
********************************************************

Target: http://10.10.10.10/FUZZ
Total requests: 4594

==================================================================
ID   Response   Lines      Word         Chars          Payload    
==================================================================

000010:  C=403      9 L	      28 W	    276 Ch	  ".hta"
000011:  C=403      9 L	      28 W	    276 Ch	  ".htaccess"
000012:  C=403      9 L	      28 W	    276 Ch	  ".htpasswd"
000573:  C=301      9 L	      28 W	    308 Ch	  "api"
000706:  C=301      9 L	      28 W	    312 Ch	  "backups"
001348:  C=301      9 L	      28 W	    308 Ch	  "dev"
002094:  C=200    375 L	     964 W	  10918 Ch	  "index.html"
003598:  C=403      9 L	      28 W	    276 Ch	  "server-status"
004244:  C=301      9 L	      28 W	    308 Ch	  "var"

Total time: 5.518419
Processed Requests: 4594
Filtered Requests: 4585
Requests/sec.: 832.4847
```


