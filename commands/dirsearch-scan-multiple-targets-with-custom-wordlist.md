---
type: command
executor: bash
data: >
  python3 dirsearch.py -L subdomains.txt -e .* -w RobotsDisallowed-Top1000.txt
  --simple-report=output.txt -t 50
tags:
  - reconnaissance
  - web-scanning
platforms:
  - Linux
  - Web
verified: true
validated: true
---

# dirsearch-scan-multiple-targets-with-custom-wordlist

## Command

```bash
python3 dirsearch.py -L subdomains.txt -e .* -w RobotsDisallowed-Top1000.txt --simple-report=output.txt -t 50
```

## Description

This command uses dirsearch to brute-force directories and files on multiple targets listed in subdomains.txt, using a custom wordlist for path fuzzing. It scans all file extensions and outputs results to a simple text file, with 50 threads for performance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -L subdomains.txt | File containing list of target URLs/subdomains (one per line) | Yes |
| -e .* | Extensions to test (.* for all) | Yes |
| -w RobotsDisallowed-Top1000.txt | Path to the custom wordlist file | Yes |
| --simple-report=output.txt | Output file for scan results | Yes |
| -t 50 | Number of concurrent threads | No (default 10) |

## Examples

### Basic Usage

```bash
python3 dirsearch.py -L subdomains.txt -e .* -w RobotsDisallowed-Top1000.txt --simple-report=output.txt -t 50
```

### Advanced Usage

For a single target with verbose output:

```bash
python3 dirsearch.py -u https://example.com -e php,asp -w raft-large-directories.txt -t 20 --format json -o results.json
```

## Expected Output

Dirsearch will display real-time progress on the console, showing tested paths and status codes. The output.txt file will contain lines like:

```
target.com (200)  /admin -  (GET) 2.34s
example.com (403)  /backup -  (GET) 1.12s
```

Success is indicated by paths with 200 (accessible) or 301/302 (redirects) status codes, revealing hidden content.

## Related

- [[procedures/Directory-and-File-Fuzzing-with-Dirsearch-Using-Large-Wordlists]]
- [[tools/dirsearch]]
