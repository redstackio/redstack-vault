---
type: command
executor: bash
data: python3 log4j-scan.py -u $_TARGET_URL --run-all-tests
output: null
created_at: '2023-04-06T03:55:56.883829+00:00'
updated_at: '2023-04-06T03:55:56.890897+00:00'
platforms:
  - Linux
tags:
  - scanning
  - log4shell
verified: true
validated: true
---

# log4j-scan-run-all-tests

## Command

```bash
python3 log4j-scan.py -u $_TARGET_URL --run-all-tests
```

## Description

This command runs a comprehensive Log4Shell vulnerability scan on the specified target URL, testing all available payloads including exploit simulations via JNDI lookups. Use it for initial detection in uncontrolled environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The full URL of the target endpoint to scan (e.g., http://example.com/login) | Yes |
| --run-all-tests | Enables all detection and exploitation tests, including DNS callbacks | Yes |
| -u | Flag to specify the target URL | Yes |

## Examples

### Basic Usage

```bash
python3 log4j-scan.py -u http://127.0.0.1:8080 --run-all-tests
```

### Advanced Usage

```bash
python3 log4j-scan.py -u https://target.com/api --run-all-tests --wait-time 2
```

## Expected Output

The tool outputs scan progress and results:

```
[*] Testing URL: http://127.0.0.1:8080
[*] Testing header: User-Agent
[+] Vulnerable! JNDI LDAP lookup detected in response.
Exploit Test: DNS callback successful to attacker.example.com
Vulnerability: High (RCE possible)
```

If not vulnerable:

```
[-] No vulnerability detected in any tested vectors.
```

## Related

- [[procedures/Log4Shell Scanning Procedure]]
- [[commands/log4j-scan-waf-bypass]]
