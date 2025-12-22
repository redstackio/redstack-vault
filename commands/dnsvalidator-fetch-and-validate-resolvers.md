---
type: command
executor: bash
data: dnsvalidator -tL $_DNS_LIST_URL -threads $_THREADS -o $_OUTPUT_FILE
output: "root@kali ~# dnsvalidator -tL https://public-dns.info/nameservers.txt -threads 20 -o resolvers.txt\n=======================================================\ndnsvalidator v0.1\tby James McLean (@vortexau) \n                \t& Michael Skelton (@codingo_)\n=======================================================\n[22:10:53] [INFO] [1.1.1.1] resolving baseline\n[22:10:53] [INFO] [8.8.8.8] resolving baseline\n[22:10:54] [INFO] [9.9.9.9] resolving baseline\n... [CUT] ...\n[22:11:20] [INFO] Validated 1500 resolvers, output to resolvers.txt"
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - dns
  - validation
  - enumeration
verified: true
validated: true
---

# dnsvalidator-fetch-and-validate-resolvers

## Command

```bash
dnsvalidator -tL $_DNS_LIST_URL -threads $_THREADS -o $_OUTPUT_FILE
```

## Description

This command fetches a list of DNS server IPs from a specified URL or file and validates their reliability by comparing query responses to baseline servers (1.1.1.1, 8.8.8.8, 9.9.9.9). It uses multithreading for efficiency and outputs a filtered list of validated resolvers to a file. Use this during reconnaissance to build a reliable DNS resolver pool for tools like Amass or dnsrecon.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -tL $_DNS_LIST_URL | URL or file path to a text list of DNS server IPs (one per line, e.g., https://public-dns.info/nameservers.txt) | Yes |
| -threads $_THREADS | Number of concurrent threads for validation (20-200 recommended; higher speeds up process but may increase load) | Yes |
| -o $_OUTPUT_FILE | Path to the output file where validated resolver IPs will be saved (one per line) | Yes |
| --timeout | Optional: DNS query timeout in seconds (default 2; increase for slower networks) | No |
| -v | Optional: Enable verbose logging for detailed progress | No |

## Examples

### Basic Usage

```bash
dnsvalidator -tL https://public-dns.info/nameservers.txt -threads 50 -o resolvers.txt
```

### Advanced Usage

```bash
dnsvalidator -tL ./custom-dns-list.txt -threads 100 -o validated-resolvers.txt --timeout 5 -v
```

## Expected Output

The command produces real-time logs showing baseline resolutions and validation progress for each server. Successful runs end with a summary of validated resolvers and create the output file containing only reliable IPs.

Example output snippet:

```
=======================================================
dnsvalidator v0.1	by James McLean (@vortexau) 
                	& Michael Skelton (@codingo_)
=======================================================
[22:10:53] [INFO] [1.1.1.1] resolving baseline
[22:10:53] [INFO] [8.8.8.8] resolving baseline
[22:10:54] [INFO] [9.9.9.9] resolving baseline
...
[22:11:20] [INFO] Validated 1500 resolvers out of 5000 tested
[22:11:20] [INFO] Output saved to resolvers.txt
```

The output file (resolvers.txt) will contain lines like:

```
1.1.1.1
8.8.8.8
9.9.9.9
...
```

## Related

- [[tools/dnsvalidator]]
