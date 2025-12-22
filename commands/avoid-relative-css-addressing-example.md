---
id: 9e462b99-84d6-4d67-892b-600175b28296
name: avoid-relative-css-addressing-example
type: command
executor: bash
data: >-
  echo "Use absolute addressing instead of relative addressing to prevent
  attackers from accessing sensitive files by manipulating the directory
  structure."
output: null
created_at: '2023-04-06T03:56:43.832541+00:00'
updated_at: '2023-04-06T03:56:43.856904+00:00'
platforms:
  - Web
tags:
  - defense
  - rpo
verified: true
validated: true
---

# avoid-relative-css-addressing-example

## Command

```bash
echo "Use absolute addressing instead of relative addressing to prevent attackers from accessing sensitive files by manipulating the directory structure."
```

## Description

Provides an example of prevention advice for relative CSS paths in RPO contexts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```bash
echo "Use absolute addressing instead of relative addressing to prevent attackers from accessing sensitive files by manipulating the directory structure."
```

## Expected Output

Use absolute addressing instead of relative addressing to prevent attackers from accessing sensitive files by manipulating the directory structure.

## Related

- [[procedures/Exploit-RPO-for-Stored-XSS-via-CSS-Injection-in-IE]]
