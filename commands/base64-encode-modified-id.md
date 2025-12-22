---
id: cmd-base64-encode-modified-id
data: 'echo ''gid://hackerone/EmbeddedSubmissionForm/10'' | base64'
tags:
  - encoding
  - base64
type: command
output: Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vMTA=
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.637Z'
verified: false
validated: true
submitted: true
---
# base64-encode-modified-id

## Command

```bash
echo 'gid://hackerone/EmbeddedSubmissionForm/10' | base64
```

## Description

Encodes a modified GID string (with incremented primary key) into base64 for use as a GraphQL node ID in IDOR attacks on HackerOne.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Input string | The modified GID (e.g., gid://hackerone/EmbeddedSubmissionForm/10) | Yes |

## Examples

### Basic Usage

```bash
echo 'gid://hackerone/EmbeddedSubmissionForm/10' | base64
```

### Advanced Usage

Script for multiple:
```bash
for i in {1..5}; do echo "gid://hackerone/EmbeddedSubmissionForm/$i" | base64; done
```

## Expected Output

`Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vMTA=` – New encoded node ID.

## Related

- [[Related Procedure: Modify-and-Re-encode-Node-ID-for-Enumeration]]
