---
id: 28320ad2-aebb-4b3f-940d-81e049616fc6
name: dirsearch-brute-force-subdomains-with-custom-wordlist
type: command
executor: bash
data: >
  python3 dirsearch.py -L sub-domains.txt -e .* -w paths.txt
  --simple-report=output.txt -t 50
output: null
created_at: '2020-07-24T17:11:34.304398+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - web-scanning
verified: true
validated: true
---

# dirsearch-brute-force-subdomains-with-custom-wordlist

## Command

```bash
python3 dirsearch.py -L sub-domains.txt -e .* -w paths.txt --simple-report=output.txt -t 50
```

## Description

This command invokes Dirsearch to brute-force directories and files on a list of subdomains loaded from a file, using a custom wordlist for paths and extensions. It generates a simple report of findings and uses multi-threading for speed. Use this during web reconnaissance to discover hidden endpoints without manual testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -L sub-domains.txt | File containing list of subdomains (one per line) | Yes |
| -e .* | Extensions to test (.* matches all) | Yes |
| -w paths.txt | Custom wordlist file for directories/files | Yes |
| --simple-report=output.txt | Output file for scan results (status, paths) | Yes |
| -t 50 | Number of concurrent threads | No (default 10) |

## Examples

### Basic Usage

```bash
python3 dirsearch.py -L sub-domains.txt -e .* -w paths.txt --simple-report=output.txt -t 50
```

### Advanced Usage

```bash
python3 dirsearch.py -L sub-domains.txt -e php,html,json -w paths.txt --simple-report=output.txt -t 25 --exclude-sizes=0B
```

> This variation limits extensions and excludes empty responses for cleaner output.

## Expected Output

Console shows real-time progress:

```
[+] Scanning URL: http://sub1.example.com/
[200] /api/apidocs (1234 B)
[404] /admin.php (0 B)

[+] Scanning URL: http://sub2.example.com/
[200] /swagger-ui.html (5678 B)

INFO: 12 threads active
```

The output.txt file contains a summarized list of targets and discovered paths with status codes and sizes, e.g.:

```
http://sub1.example.com/ [200]/api/apidocs [1234]
http://sub2.example.com/ [200]/swagger-ui.html [5678]
```

## Related

- [[procedures/Brute-Force-Directories-and-Files-on-Subdomains-Using-Dirsearch]]
- [[tools/Dirsearch]]
