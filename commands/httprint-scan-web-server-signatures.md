---
id: af24c80f-2db9-49c0-b4b0-e0d005f8c23d
name: httprint-scan-web-server-signatures
type: command
executor: bash
data: 'httprint -h http://$_TARGET -s $_SIGNATURES_FILE'
output: >-
  root@kali:~# httprint -h http://10.10.10.10 -s
  /usr/share/httprint/signatures.txt

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
created_at: '2019-09-14T05:30:22.077788+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - web-fingerprinting
  - enumeration
verified: true
validated: true
---

# httprint-scan-web-server-signatures

## Command

```bash
httprint -h http://$_TARGET -s $_SIGNATURES_FILE
```

## Description

This command performs web server fingerprinting on a target host using httprint, analyzing HTTP responses to identify the server type and version even if obfuscated. It uses a signatures file to match characteristics like banner strings, error pages, and response headers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | Target URL or IP address (e.g., 10.10.10.10 or example.com) | Yes |
| $_SIGNATURES_FILE | Path to the signatures database file (default: /usr/share/httprint/signatures.txt) | Yes |
| -h | Specifies the host to fingerprint | Built-in |
| -s | Path to the signatures file | Built-in |

## Examples

### Basic Usage

```bash
httprint -h http://10.10.10.10 -s /usr/share/httprint/signatures.txt
```

### HTTPS Target

```bash
httprint -h https://example.com -s /usr/share/httprint/signatures.txt
```

## Expected Output

Description of what output to expect when the command runs successfully.

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

## Related

- [[tools/httprint]]
- [[procedures/web-server-fingerprinting]]
