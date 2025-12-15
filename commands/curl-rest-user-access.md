---
data: >-
  curl --header "Authorization: Bearer jKSvxhuDN-Noag6N-w7R"
  "http://gitlab.joaxcar.com/api/v4/user"
tags:
  - rest
  - deactivated
type: command
output: >-
  {"message":"403 Forbidden - Your account has been deactivated by your
  administrator. Please log back in from a web browser to reactivate your
  account at http://gitlab.joaxcar.com"}
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.467Z'
id: d94b8a6d-f12d-4498-adfc-073191f64775
verified: false
validated: true
submitted: true
---
# curl-rest-user-access

## Command

```bash
curl --header "Authorization: Bearer jKSvxhuDN-Noag6N-w7R" "http://gitlab.joaxcar.com/api/v4/user"
```

## Description

Attempts to access the current user via GitLab REST API with a deactivated token, expecting denial.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H 'Authorization: Bearer ...'` | Token | Yes |

## Examples

### Basic Usage

```bash
curl --header "Authorization: Bearer jKSvxhuDN-Noag6N-w7R" "http://gitlab.joaxcar.com/api/v4/user"
```

## Expected Output

403 Forbidden JSON message about deactivation.

## Related

- [[procedures/Test-REST-API-Access-with-Deactivated-Token]]
