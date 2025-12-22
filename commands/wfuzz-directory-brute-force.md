---
id: 583fd646-28c6-4614-9ee3-fd82b366694a
type: command
executor: bash
data: 'wfuzz --hc 404 -c -w $_WORDLIST -u http://$_TARGET_IP/FUZZ'
output: "root@kali:~# wfuzz --hc 404 -c -w common.txt -u http://10.10.10.10/FUZZ\n\n********************************************************\n* Wfuzz 2.3.3 - The Web Fuzzer                         *\n********************************************************\n\nTarget: http://10.10.10.10/FUZZ\nTotal requests: 4594\n\n==================================================================\nID   Response   Lines      Word         Chars          Payload    \n==================================================================\n\n000010:  C=403      9 L\t      28 W\t    276 Ch\t  \".hta\"\n000573:  C=301      9 L\t      28 W\t    308 Ch\t  \"api\"\n002094:  C=200    375 L\t     964 W\t  10918 Ch\t  \"index.html\"\n\nTotal time: 5.518419\nProcessed Requests: 4594\nFiltered Requests: 4585\nRequests/sec.: 832.4847"
created_at: '2019-09-13T23:40:37.674346+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - web
  - fuzzing
verified: true
validated: true
---

# wfuzz-directory-brute-force

## Command

```bash
wfuzz --hc 404 -c -w $_WORDLIST -u http://$_TARGET_IP/FUZZ
```

## Description

This command brute-forces directories and files on a target web server by fuzzing the URL path with entries from a wordlist. It hides 404 responses to focus on potentially valid resources and displays a progress counter for monitoring the scan.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --hc 404 | Hide responses with HTTP status code 404 (Not Found) to reduce noise from invalid paths | Yes |
| -c | Enable colored output and display a progress counter during the scan | No |
| -w $_WORDLIST | Path to the wordlist file containing directory/file names to test (e.g., common.txt with paths like admin, login) | Yes |
| -u | Specify the target URL, with FUZZ as the placeholder for wordlist entries (e.g., http://example.com/FUZZ) | Yes |
| $_TARGET_IP | IP address or hostname of the target web server | Yes |

## Examples

### Basic Usage

```bash
wfuzz --hc 404 -w common.txt -u http://10.10.10.10/FUZZ
```

### Advanced Usage

Scan over HTTPS with a custom port and additional filters for response size:

```bash
wfuzz --hc 404 --hs 1000 -c -w dirs.txt -u https://10.10.10.10:8443/FUZZ
```

## Expected Output

The command outputs a table summarizing responses, including status codes (C=), lines (L), words (W), characters (Ch), and the payload tested. Successful discoveries show codes like 200 (OK) or 301 (Redirect) for valid resources. Filtered requests (e.g., 404s) are excluded from the display. Example shows hits on ".hta" (403), "api" (301), and "index.html" (200).

## Related

- [[procedures/directory-brute-force-web-app-with-wfuzz]]
- [[tools/Wfuzz]]
