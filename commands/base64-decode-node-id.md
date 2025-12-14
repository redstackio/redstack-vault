---
id: cmd-base64-decode-node-id
data: echo 'Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vOQ==' | base64 -d
tags:
  - decoding
  - base64
type: command
output: 'gid://hackerone/EmbeddedSubmissionForm/9'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.638Z'
verified: false
validated: true
submitted: true
---
# base64-decode-node-id

## Command

```bash
echo 'Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vOQ==' | base64 -d
```

## Description

Decodes a base64-encoded HackerOne GraphQL node ID to reveal the GID structure, including the auto-incremental primary key. Use this in IDOR enumeration to understand and modify IDs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Input string | The base64-encoded node ID | Yes |

## Examples

### Basic Usage

```bash
echo 'Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vOQ==' | base64 -d
```

### Advanced Usage

For scripted decoding:
```bash
node_id="Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vOQ=="
echo $node_id | base64 -d
```

## Expected Output

`gid://hackerone/EmbeddedSubmissionForm/9` – Shows the object type and integer key.

## Related

- [[Related Procedure: Decode-HackerOne-GraphQL-Node-ID]]
