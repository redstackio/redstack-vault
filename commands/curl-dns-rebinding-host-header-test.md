---
id: a5aa8e61-fa78-4857-b62f-6e58e19a8092
name: curl-dns-rebinding-host-header-test
type: command
executor: bash
data: 'curl --header ''Host: $_ARBITRARY_HOSTNAME'' http://$_VULNERABLE_IP:$_PORT'
output: null
created_at: '2023-04-06T03:55:57.599186+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - Unix
tags:
  - dns-rebinding
  - web-testing
verified: true
validated: true
---

# curl-dns-rebinding-host-header-test

## Command

```bash
curl --header 'Host: $_ARBITRARY_HOSTNAME' http://$_VULNERABLE_IP:$_PORT
```

## Description

This command uses curl to send an HTTP GET request to a target IP and port while spoofing the Host header with an arbitrary hostname. It tests if the web service validates the Host header properly, which is a key check for DNS rebinding vulnerabilities. Use this during reconnaissance to identify services that might accept requests intended for external domains but routed to internal IPs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ARBITRARY_HOSTNAME | The spoofed hostname to set in the Host header (e.g., 'attacker.com' or 'rbndr.us'), simulating an attacker-controlled domain | Yes |
| $_VULNERABLE_IP | The IP address of the target service (e.g., '192.168.1.100') | Yes |
| $_PORT | The port the service is listening on (e.g., '8080'; default HTTP is 80, HTTPS 443) | Yes |
| --header (or -H) | Adds a custom header to the request; here used for Host spoofing | Built-in |

## Examples

### Basic Usage

```bash
curl --header 'Host: attacker.com' http://192.168.1.100:8080
```

This tests a service on 192.168.1.100:8080 claiming the host is 'attacker.com'.

### Advanced Usage

```bash
curl -v --header 'Host: $_ARBITRARY_HOSTNAME' -X GET http://$_VULNERABLE_IP:$_PORT -o response.html
```

Adds verbose output (-v) for headers, specifies method (-X GET), and saves body to file (-o) for analysis.

## Expected Output

If the service is vulnerable (accepts mismatched Host):
```
<!DOCTYPE html>
<html>
<head><title>Vulnerable Service</title></head>
<body>Welcome to internal app</body>
</html>
```

If not vulnerable (rejects mismatch):
```
HTTP/1.1 400 Bad Request
Content-Type: text/plain

Invalid Host header
```

Look for 200 OK with content in vulnerable cases; errors like 400/403 indicate protection.

## Related

- [[procedures/Test-Service-for-DNS-Rebinding-Vulnerability]] (procedure that uses this command)
- [[tools/cURL]] (base tool documentation)
