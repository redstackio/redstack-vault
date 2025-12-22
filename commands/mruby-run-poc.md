---
data: mruby infinite_heredoc.rb
tags:
  - mruby
  - dos
type: command
executor: bash
platforms:
  - Linux
id: 21934a4a-680e-447c-a16c-e185dc3152dd
created_at: '2025-12-11T03:47:39.204Z'
updated_at: '2025-12-11T03:47:39.204Z'
verified: false
validated: true
submitted: true
---
# mruby-run-poc

## Command

```bash
mruby infinite_heredoc.rb
```

## Description

Runs a Ruby script using the MRuby interpreter, used here to trigger an infinite loop vulnerability by executing the POC file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `infinite_heredoc.rb` | The POC script file containing invalid heredoc code | Yes |

## Examples

### Basic Usage

```bash
mruby infinite_heredoc.rb
```

## Expected Output

Infinite loop with no output; process becomes unresponsive to SIGTERM.

## Related

- [[commands/sandbox-run-poc]]
- [[procedures/Exploit-MRuby-Infinite-Loop-Vulnerability]]
