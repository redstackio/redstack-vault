---
id: 1170ea53-45da-448e-a79b-ed025fff07bc
name: Wfuzz directory brute force with extensions
type: command
executor: null
data: wfuzz --hc 404 -w common.txt -w extlist.txt -u http://10.10.10.10/FUZZ.FUZ2Z
output: "root@kali:~# wfuzz --hc 404,403 -w common.txt -w extlist.txt -u http://10.10.10.10/FUZZ.FUZ2Z\
  \ \n\n********************************************************\n* Wfuzz 2.3.3 -\
  \ The Web Fuzzer                         *\n********************************************************\n\
  \nTarget: http://10.10.10.10/FUZZ.FUZ2Z\nTotal requests: 27564\n\n==================================================================\n\
  ID   Response   Lines      Word         Chars          Payload    \n==================================================================\n\
  \n012551:  C=200    375 L\t     964 W\t  10918 Ch\t  \"index - html\"\n021322: \
  \ C=200      0 L\t       0 W\t      0 Ch\t  \"secret - txt\"\n\nTotal time: 27.40219\n\
  Processed Requests: 27564\nFiltered Requests: 27562\nRequests/sec.: 1005.904\n"
created_at: '2019-09-13T23:40:37.644764+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Wfuzz]]'
---

# Wfuzz directory brute force with extensions

```bash
wfuzz --hc 404 -w common.txt -w extlist.txt -u http://10.10.10.10/FUZZ.FUZ2Z
```

## Expected Output

```
root@kali:~# wfuzz --hc 404,403 -w common.txt -w extlist.txt -u http://10.10.10.10/FUZZ.FUZ2Z 

********************************************************
* Wfuzz 2.3.3 - The Web Fuzzer                         *
********************************************************

Target: http://10.10.10.10/FUZZ.FUZ2Z
Total requests: 27564

==================================================================
ID   Response   Lines      Word         Chars          Payload    
==================================================================

012551:  C=200    375 L	     964 W	  10918 Ch	  "index - html"
021322:  C=200      0 L	       0 W	      0 Ch	  "secret - txt"

Total time: 27.40219
Processed Requests: 27564
Filtered Requests: 27562
Requests/sec.: 1005.904

```


