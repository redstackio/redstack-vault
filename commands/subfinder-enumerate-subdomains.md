---
data: subfinder -d bountypay.h1ctf.com -o subdomains.txt
tags:
  - reconnaissance
type: command
output: >-
  List of subdomains: app.bountypay.h1ctf.com, www.bountypay.h1ctf.com,
  bountypay.h1ctf.com, software.bountypay.h1ctf.com, staff.bountypay.h1ctf.com,
  api.bountypay.h1ctf.com
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.020Z'
id: cf7b1450-f103-4b09-bebc-63114e0a5759
verified: false
validated: true
submitted: true
---
# subfinder-enumerate-subdomains

## Command

```bash
subfinder -d bountypay.h1ctf.com -o subdomains.txt
```

## Description

Enumerates subdomains of the target domain using passive sources for initial reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | Domain to enumerate | Yes |
| `-o` | Output file | No |

## Examples

### Basic Usage

```bash
subfinder -d bountypay.h1ctf.com -o subdomains.txt
```

### Advanced Usage

```bash
subfinder -d bountypay.h1ctf.com -all -o subdomains.txt
```

## Expected Output

List of discovered subdomains saved to file.

## Related

- [[tools/subfinder]]
