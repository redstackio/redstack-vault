---
id: 786edeca-ad67-400a-9890-0a9848f5be77
name: Wfuzz Brute Force Virtual Hosts
type: command
executor: bash
data: 'wfuzz --hc 404 -c -w $_WORDLIST -u http://$_TARGET_IP -H ''Host: FUZZ.$_DOMAIN'''
output: "root@kali:~# wfuzz --hc 404 -c -w fierce-hostlist.txt -u http://10.10.10.10 -H 'Host: FUZZ.testcorp.net'\n\n********************************************************\n* Wfuzz 2.3.4 - The Web Fuzzer                         *\n********************************************************\n\nTarget: http://10.10.10.10/\nTotal requests: 2280\n\n==================================================================\nID   Response   Lines      Word         Chars          Payload    \n==================================================================\n\n001158:  C=403     29 L\t      92 W\t   1233 Ch\t  \"member\"\n\nTotal time: 17.08417\nProcessed Requests: 2280\nFiltered Requests: 2279\nRequests/sec.: 133.4568\n"
created_at: '2019-10-17T21:12:55.974250+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - brute-force
  - reconnaissance
verified: true
validated: true
---

# wfuzz-brute-force-virtual-hosts

## Command

```bash
wfuzz --hc 404 -c -w $_WORDLIST -u http://$_TARGET_IP -H 'Host: FUZZ.$_DOMAIN'
```

## Description

This command uses Wfuzz to perform a brute force scan for virtual hosts by iterating through a wordlist and injecting each entry into the HTTP Host header sent to the target IP. It is ideal for discovering non-DNS-resolved subdomains or hidden sites during web reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_WORDLIST | Path to a text file containing potential host names (one per line) | Yes |
| $_TARGET_IP | IP address or hostname of the web server to scan | Yes |
| $_DOMAIN | Base domain to append to fuzz payloads (e.g., example.com) | Yes |
| --hc 404 | Hide (filter out) responses with HTTP status code 404 | Built-in |
| -c | Enable counter display for progress tracking | Built-in |
| -u | Specify the base URL for requests | Built-in |
| -H | Add a custom HTTP header (here, Host: FUZZ.$_DOMAIN) | Built-in |

## Examples

### Basic Usage

Scan a target IP for virtual hosts using a common wordlist:

```bash
wfuzz --hc 404 -c -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://192.168.1.100 -H 'Host: FUZZ.corporate.local'
```

### Advanced Usage

Include HTTPS support and filter additional codes:

```bash
wfuzz --hc 404,403 -c -w custom_hosts.txt -u https://10.10.10.50 --hc XXS -H 'Host: FUZZ.target.com'
```

## Expected Output

Successful execution displays progress and highlights valid responses:

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

Look for non-404 codes (e.g., 200, 403) to identify potential virtual hosts; the payload column shows the matched word.

## Related

- [[procedures/brute-force-virtual-hosts-with-wfuzz]]
- [[tools/Wfuzz]]
