---
id: af24c80f-2db9-49c0-b4b0-e0d005f8c23d
name: Httprint Scan a Web Server for Known Signatures
type: command
executor: bash
data: httprint -h http://$_TARGET_IP -s /usr/share/httprint/signatures.txt
output: "root@kali:~# httprint -h http://10.10.10.10 -s /usr/share/httprint/signatures.txt\n\
  httprint v0.301 (beta) - web server fingerprinting tool\n(c) 2003-2005 net-square\
  \ solutions pvt. ltd. - see readme.txt\nhttp://net-square.com/httprint/\nhttprint@net-square.com\n\
  \nFinger Printing on http://10.10.10.10:80/\nFinger Printing Completed on http://10.10.10.10:80/\n\
  --------------------------------------------------\nHost: 10.10.10.10\nDerived Signature:\n\
  Apache/2.4.29 (Ubuntu)\n9E431BC86ED3C295811C9DC5811C9DC5050C5D32505FCFE84276E4BB811C9DC5\n\
  0D7645B5811C9DC5811C9DC5CD37187C11DDC7D7811C9DC5811C9DC52655F350\nFCCC535BE2CE6923E2CE6923811C9DC5E2CE6927050C5D336ED3C295811C9DC5\n\
  6ED3C295E2CE6926811C9DC5E2CE6923E2CE69236ED3C2956ED3C295E2CE6923\nE2CE69236ED3C295811C9DC5E2CE6927E2CE6923\n\
  \nBanner Reported: Apache/2.4.29 (Ubuntu)\nBanner Deduced: Apache/2.0.x\nScore:\
  \ 108\nConfidence: 65.06\n------------------------\nScores: \nApache/2.0.x: 108\
  \ 65.06\nApache/1.3.26: 102 52.86\nApache/1.3.27: 101 50.99\nApache/1.3.[4-24]:\
  \ 100 49.16\nApache/1.3.[1-3]: 100 49.16\nTUX/2.0 (Linux): 96 42.25\nMicrosoft-IIS/6.0:\
  \ 91 34.54\nApache/1.2.6: 90 33.11\nAgranat-EmWeb: 87 29.06\nthttpd: 72 13.46\n\
  Lotus-Domino/6.x: 71 12.68\nWebSitePro/2.3.18: 70 11.92\n..\n..\nLinksys BEFSR41/BEFSR11/BEFSRU31:\
  \ 0  0.00\nMailEnable-HTTP/5.0: 0  0.00\n\n--------------------------------------------------"
created_at: '2019-09-14T05:30:22.077788+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Httprint Scan a Web Server for Known Signatures

```bash
httprint -h http://$_TARGET_IP -s /usr/share/httprint/signatures.txt
```

## Expected Output

```
root@kali:~# httprint -h http://10.10.10.10 -s /usr/share/httprint/signatures.txt
httprint v0.301 (beta) - web server fingerprinting tool
(c) 2003-2005 net-square solutions pvt. ltd. - see readme.txt
http://net-square.com/httprint/
httprint@net-square.com

Finger Printing on http://10.10.10.10:80/
Finger Printing Completed on http://10.10.10.10:80/
--------------------------------------------------
Host: 10.10.10.10
Derived Signature:
Apache/2.4.29 (Ubuntu)
9E431BC86ED3C295811C9DC5811C9DC5050C5D32505FCFE84276E4BB811C9DC5
0D7645B5811C9DC5811C9DC5CD37187C11DDC7D7811C9DC5811C9DC52655F350
FCCC535BE2CE6923E2CE6923811C9DC5E2CE6927050C5D336ED3C295811C9DC5
6ED3C295E2CE6926811C9DC5E2CE6923E2CE69236ED3C2956ED3C295E2CE6923
E2CE69236ED3C295811C9DC5E2CE6927E2CE6923

Banner Reported: Apache/2.4.29 (Ubuntu)
Banner Deduced: Apache/2.0.x
Score: 108
Confidence: 65.06
------------------------
Scores: 
Apache/2.0.x: 108 65.06
Apache/1.3.26: 102 52.86
Apache/1.3.27: 101 50.99
Apache/1.3.[4-24]: 100 49.16
Apache/1.3.[1-3]: 100 49.16
TUX/2.0 (Linux): 96 42.25
Microsoft-IIS/6.0: 91 34.54
Apache/1.2.6: 90 33.11
Agranat-EmWeb: 87 29.06
thttpd: 72 13.46
Lotus-Domino/6.x: 71 12.68
WebSitePro/2.3.18: 70 11.92
..
..
Linksys BEFSR41/BEFSR11/BEFSRU31: 0  0.00
MailEnable-HTTP/5.0: 0  0.00

--------------------------------------------------
```


