---
data: sandbox infinite_heredoc.rb
tags:
  - sandbox
  - dos
type: command
executor: bash
platforms:
  - Linux
id: 9858bfcb-ea17-4586-8b94-f5a03b90fb7d
created_at: '2025-12-11T03:47:39.202Z'
updated_at: '2025-12-11T03:47:39.202Z'
verified: false
validated: true
submitted: true
---
# sandbox-run-poc

## Command

```bash
sandbox infinite_heredoc.rb
```

## Description

Runs a Ruby script in the mruby-engine sandbox environment, triggering the infinite loop vulnerability and making the process unresponsive.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `infinite_heredoc.rb` | The POC script file containing invalid heredoc code | Yes |

## Examples

### Basic Usage

```bash
sandbox infinite_heredoc.rb
```

## Expected Output

Infinite loop with no output; process unresponsive to SIGTERM, requiring SIGABRT or SIGKILL.

## Related

- [[commands/mruby-run-poc]]
- [[procedures/Exploit-MRuby-Infinite-Loop-Vulnerability]]
