---
id: 56abad25-8e35-43d9-a2f5-10543728df63
name: avoid-relative-css-addressing
type: command
executor: bash
data: >-
  echo "Avoid using relative addressing to CSS style sheets as it can allow
  attackers to access sensitive files by manipulating the directory structure."
output: null
created_at: '2023-04-06T03:56:43.832337+00:00'
updated_at: '2023-04-06T03:56:43.856697+00:00'
platforms:
  - Web
tags:
  - defense
  - rpo
verified: true
validated: true
---

# avoid-relative-css-addressing

## Command

```bash
echo "Avoid using relative addressing to CSS style sheets as it can allow attackers to access sensitive files by manipulating the directory structure."
```

## Description

Outputs a reminder to use absolute paths for CSS to mitigate RPO attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```bash
echo "Avoid using relative addressing to CSS style sheets as it can allow attackers to access sensitive files by manipulating the directory structure."
```

## Expected Output

Avoid using relative addressing to CSS style sheets as it can allow attackers to access sensitive files by manipulating the directory structure.

## Related

- [[procedures/Exploit-RPO-for-Stored-XSS-via-CSS-Injection-in-IE]]
