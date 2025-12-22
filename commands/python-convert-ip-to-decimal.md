---
id: 875a9ea8-dd4c-4912-bb22-ef12809c5c7e
name: python-convert-ip-to-decimal
type: command
executor: python
data: >-
  python3 -c "print(sum(int(octet) << (8*(3-i)) for i,octet in
  enumerate('$_TARGET_IP'.split('.'))))"
output: '2130706433'
created_at: '2023-04-06T03:56:37.367477+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - ssrf
  - bypass
  - conversion
verified: true
validated: true
---

# python-convert-ip-to-decimal

## Command

```python
python3 -c "print(sum(int(octet) << (8*(3-i)) for i,octet in enumerate('$_TARGET_IP'.split('.'))))"
```

## Description

This Python one-liner converts a dotted IPv4 address to its decimal (32-bit integer) representation, useful for SSRF bypass techniques where filters block standard IP formats. Run it in a terminal to quickly generate the numeric equivalent for use in URLs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Dotted IPv4 address to convert (e.g., 127.0.0.1) | Yes |

## Examples

### Basic Usage

```python
python3 -c "print(sum(int(octet) << (8*(3-i)) for i,octet in enumerate('127.0.0.1'.split('.'))))"
```

### Advanced Usage

For 169.254.169.254 (AWS metadata):

```python
python3 -c "print(sum(int(octet) << (8*(3-i)) for i,octet in enumerate('169.254.169.254'.split('.'))))"
```

## Expected Output

A single integer representing the IP in decimal form, e.g.,

```
2130706433
```

for 127.0.0.1. If the IP is invalid (e.g., non-numeric octets), it outputs a traceback with ValueError.

## Related

- [[procedures/Bypass-SSRF-Filters-with-Decimal-IP-Addresses]]
- [[techniques/Exploitation of Remote Services|T1210]]
