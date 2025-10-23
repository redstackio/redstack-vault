---
id: 226523b5-4712-40b6-a671-43d78e5d341f
name: Wfuzz recursive directory brute force
type: command
executor: null
data: wfuzz --hc 404,403 -R5 -w common.txt -u http://10.10.10.10/FUZZ
output: "root@kali:~# wfuzz --hc 404,403 -R5 -w common.txt -u http://10.10.10.10/FUZZ\n\
  \nWarning: Pycurl is not compiled against Openssl. Wfuzz might not work correctly\
  \ when fuzzing SSL sites. Check Wfuzz's documentation for more information.\n\n\
  ********************************************************\n* Wfuzz 2.3.3 - The Web\
  \ Fuzzer                         *\n********************************************************\n\
  \nTarget: http://10.10.10.10/FUZZ\nTotal requests: 4594\n\n==================================================================\n\
  ID   Response   Lines      Word         Chars          Payload    \n==================================================================\n\
  \n000573:  C=301      9 L\t      28 W\t    308 Ch\t  \"api\"\n |_  Enqueued response\
  \ for recursion (level=1)\n000706:  C=301      9 L\t      28 W\t    312 Ch\t  \"\
  backups\"\n |_  Enqueued response for recursion (level=1)\n001348:  C=301      9\
  \ L\t      28 W\t    308 Ch\t  \"dev\"\n |_  Enqueued response for recursion (level=1)\n\
  002094:  C=200    375 L\t     964 W\t  10918 Ch\t  \"index.html\"\n004244:  C=301\
  \      9 L\t      28 W\t    308 Ch\t  \"var\"\n |_  Enqueued response for recursion\
  \ (level=1)\n016493:  C=301      9 L\t      28 W\t    316 Ch\t  \"backups - new\"\
  \n |_  Enqueued response for recursion (level=2)\n016567:  C=301      9 L\t    \
  \  28 W\t    316 Ch\t  \"backups - old\"\n |_  Enqueued response for recursion (level=2)\n\
  017475:  C=301      9 L\t      28 W\t    317 Ch\t  \"backups - site\"\n |_  Enqueued\
  \ response for recursion (level=2)\n025012:  C=200      1 L\t      12 W\t    366\
  \ Ch\t  \"backups - old - id_rsa\"\n\nTotal time: 25.59737\nProcessed Requests:\
  \ 36752\nFiltered Requests: 36743\nRequests/sec.: 1435.772"
created_at: '2019-09-14T01:56:14.217445+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Wfuzz recursive directory brute force

```bash
wfuzz --hc 404,403 -R5 -w common.txt -u http://10.10.10.10/FUZZ
```

## Expected Output

```
root@kali:~# wfuzz --hc 404,403 -R5 -w common.txt -u http://10.10.10.10/FUZZ

Warning: Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.

********************************************************
* Wfuzz 2.3.3 - The Web Fuzzer                         *
********************************************************

Target: http://10.10.10.10/FUZZ
Total requests: 4594

==================================================================
ID   Response   Lines      Word         Chars          Payload    
==================================================================

000573:  C=301      9 L	      28 W	    308 Ch	  "api"
 |_  Enqueued response for recursion (level=1)
000706:  C=301      9 L	      28 W	    312 Ch	  "backups"
 |_  Enqueued response for recursion (level=1)
001348:  C=301      9 L	      28 W	    308 Ch	  "dev"
 |_  Enqueued response for recursion (level=1)
002094:  C=200    375 L	     964 W	  10918 Ch	  "index.html"
004244:  C=301      9 L	      28 W	    308 Ch	  "var"
 |_  Enqueued response for recursion (level=1)
016493:  C=301      9 L	      28 W	    316 Ch	  "backups - new"
 |_  Enqueued response for recursion (level=2)
016567:  C=301      9 L	      28 W	    316 Ch	  "backups - old"
 |_  Enqueued response for recursion (level=2)
017475:  C=301      9 L	      28 W	    317 Ch	  "backups - site"
 |_  Enqueued response for recursion (level=2)
025012:  C=200      1 L	      12 W	    366 Ch	  "backups - old - id_rsa"

Total time: 25.59737
Processed Requests: 36752
Filtered Requests: 36743
Requests/sec.: 1435.772
```


