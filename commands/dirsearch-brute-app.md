---
data: >-
  python3 ~/dirsearch/dirsearch.py -u https://app.bountypay.h1ctf.com/ -e
  php,asp,aspx,jsp,html,zip,jar -b -w ~/dirsearch/db/dicc.txt -t 200 -x 502,503
  -H 'X-FORWARDED-FOR: 127.0.0.1'
tags:
  - brute-force
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.214Z'
id: a6fd4c0f-c108-4c0f-83e5-c08465a4bb82
verified: false
validated: true
submitted: true
---
# dirsearch-brute-app

## Command

```bash
python3 ~/dirsearch/dirsearch.py -u https://app.bountypay.h1ctf.com/ -e php,asp,aspx,jsp,html,zip,jar -b -w ~/dirsearch/db/dicc.txt -t 200 -x 502,503 -H 'X-FORWARDED-FOR: 127.0.0.1'
```

## Description

Brute forces directories and files on the target URL using a wordlist, excluding certain status codes and backups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Target URL | Yes |
| -e | File extensions | Yes |
| -b | Exclude backups | No |
| -w | Wordlist path | Yes |
| -t | Number of threads | No |
| -x | Exclude status codes | No |
| -H | Custom header | No |

## Examples

### Basic Usage

```bash
python3 dirsearch.py -u https://example.com/
```

### Advanced Usage

As above with all flags.

## Expected Output

Discovered paths including /.git/.

## Related

- [[tools/Dirsearch]]
- [[procedures/Reconnaissance-and-Exposed-Git-Discovery]]
