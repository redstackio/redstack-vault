---
id: 2dcab9d7-c636-4597-8cf6-78068743486f
name: wfuzz-fuzz-subdomains
type: command
executor: bash
data: >-
  wfuzz -c -w /SecLists/Discovery/DNS/subdomains-top1mil-5000.txt -u
  "http://$_TARGET_DOMAIN" -H "Host: FUZZ.$_TARGET_DOMAIN" --hc 311
output: null
created_at: '2020-07-24T17:11:40.367567+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - fuzzing
verified: true
validated: true
---

# wfuzz-fuzz-subdomains

## Command

```bash
wfuzz -c -w /SecLists/Discovery/DNS/subdomains-top1mil-5000.txt -u "http://$_TARGET_DOMAIN" -H "Host: FUZZ.$_TARGET_DOMAIN" --hc 311
```

## Description

This command uses wfuzz to brute-force subdomain names by fuzzing the Host header in HTTP requests to the target domain, helping discover valid subdomains during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_DOMAIN | The base domain to fuzz subdomains for (e.g., example.com) | Yes |
| /SecLists/Discovery/DNS/subdomains-top1mil-5000.txt | Path to the wordlist of subdomain names | Yes |
| -c | Enables colored output for better readability | No |
| -u | Specifies the target URL (root of the domain) | Yes |
| -H | Adds a custom Host header with FUZZ payload | Yes |
| --hc 311 | Hides responses with HTTP code 311 (filter out redirects or specific errors) | No |

## Examples

### Basic Usage

```bash
wfuzz -c -w /SecLists/Discovery/DNS/subdomains-top1mil-5000.txt -u "http://domain.htb" -H "Host: FUZZ.domain.htb" --hc 311
```

### Advanced Usage

```bash
wfuzz -c -z file,/custom/subdomains.txt -u "https://$_TARGET_DOMAIN" -H "Host: FUZZ.$_TARGET_DOMAIN" --hc 404,403 --hw 10
```
This variation uses a custom wordlist, HTTPS, hides 404/403 codes, and hides responses with headers of size 10 or less.

## Expected Output

The output shows fuzzing progress with response details for each payload:

```
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://domain.htb
Total requests: 5000

=====================================================================
ID           Response   Lines    Word       Chars       Payload
=====================================================================

000000001:   200        10       50         500         admin

000000002:   404        5        20         100         test (filtered by --hc)

Total time: 2:30:45
```
Success is indicated by non-filtered responses with varying codes (e.g., 200) or sizes, revealing valid subdomains like "admin.domain.htb".

## Related

- [[procedures/wfuzz-subdomain-fuzzing]]
- [[tools/Wfuzz]]
