---
id: db64dfe2-fb0e-4847-89f0-67efd91474ac
name: Wfuzz Directory Brute Force with Burp Proxy
type: command
executor: bash
data: wfuzz --hc 404 -c -w common.txt -u http://$_TARGET_IP/FUZZ -p 127.0.0.1:8080:HTML
output: "root@kali:~# wfuzz --hc 404 -w common.txt -u http://10.10.10.10/FUZZ -p 127.0.0.1:8080:HTML\n\
  \n********************************************************\n* Wfuzz 2.3.3 - The\
  \ Web Fuzzer                         *\n********************************************************\n\
  \nTarget: http://10.10.10.10/FUZZ\nTotal requests: 4594\n\n==================================================================\n\
  ID   Response   Lines      Word         Chars          Payload    \n==================================================================\n\
  \n000573:  C=301      9 L\t      28 W\t    308 Ch\t  \"api\"\n000706:  C=301   \
  \   9 L\t      28 W\t    312 Ch\t  \"backups\"\n001348:  C=301      9 L\t      28\
  \ W\t    308 Ch\t  \"dev\"\n002094:  C=200    375 L\t     964 W\t  10918 Ch\t  \"\
  index.html\"\n004244:  C=301      9 L\t      28 W\t    308 Ch\t  \"var\"\n\nTotal\
  \ time: 32.40853\nProcessed Requests: 4594\nFiltered Requests: 4589\nRequests/sec.:\
  \ 141.7527"
created_at: '2019-09-13T23:40:37.680161+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Wfuzz Directory Brute Force with Burp Proxy

```bash
wfuzz --hc 404 -c -w common.txt -u http://$_TARGET_IP/FUZZ -p 127.0.0.1:8080:HTML
```

## Expected Output

```
root@kali:~# wfuzz --hc 404 -w common.txt -u http://10.10.10.10/FUZZ -p 127.0.0.1:8080:HTML

********************************************************
* Wfuzz 2.3.3 - The Web Fuzzer                         *
********************************************************

Target: http://10.10.10.10/FUZZ
Total requests: 4594

==================================================================
ID   Response   Lines      Word         Chars          Payload    
==================================================================

000573:  C=301      9 L	      28 W	    308 Ch	  "api"
000706:  C=301      9 L	      28 W	    312 Ch	  "backups"
001348:  C=301      9 L	      28 W	    308 Ch	  "dev"
002094:  C=200    375 L	     964 W	  10918 Ch	  "index.html"
004244:  C=301      9 L	      28 W	    308 Ch	  "var"

Total time: 32.40853
Processed Requests: 4594
Filtered Requests: 4589
Requests/sec.: 141.7527
```


