---
type: command
executor: bash
data: python3 waybackMachine.py $_DOMAIN
output: null
tags:
  - reconnaissance
  - osint
platforms:
  - Linux
verified: true
validated: true
---

# waybackmachine-search-archived-links

## Command

```bash
python3 waybackMachine.py $_DOMAIN
```

## Description

This command executes the waybackMachine.py script to query the Internet Archive's Wayback Machine for historical snapshots of the specified domain. It retrieves a list of archived URLs, which can reveal past website structures, parameters, and content for reconnaissance purposes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | The target domain to search (e.g., owasp.com) | Yes |

## Examples

### Basic Usage

```bash
python3 waybackMachine.py owasp.com
```

### Usage with Output Redirection

```bash
python3 waybackMachine.py example.com > results.txt
```

## Expected Output

The command outputs lines in CDX format for each archived snapshot:

```
20060101120000/http://owasp.com/oldpage.html text/html 200
20070101120000/http://owasp.com/admin/login.php application/x-php 200
```

Each line includes: timestamp, original URL, MIME type, and status code. Success is indicated by non-empty output if the domain has been archived.

## Related

- [[procedures/Search-Archived-Domain-Content-with-Wayback-Machine]]
- [[tools/waybackmachine]]
