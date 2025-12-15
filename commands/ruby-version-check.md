---
id: cmd-uuid-9012
data: ruby -v
tags:
  - version-check
  - ruby
type: command
output: 'ruby 2.3.8p459 (2018-10-18 revision 63647) [x86_64-linux]'
executor: bash
platforms:
  - Software
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.906Z'
verified: false
validated: true
submitted: true
---
# ruby-version-check

## Command

```bash
ruby -v
```

## Description

This command checks the installed Ruby version to identify if it's vulnerable (2.3.x or 2.2.x) to the libYAML DoS issue.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Displays the Ruby version | Yes |

## Examples

### Basic Usage

```bash
ruby -v
```

### Advanced Usage

Not applicable; simple flag command.

## Expected Output

Version string like "ruby 2.3.8p459 (2018-10-18 revision 63647) [x86_64-linux]", indicating vulnerable branch if 2.3.x or 2.2.x.

## Related

- [[Related Procedure|procedures/Exploit-libYAML-DoS-in-Ruby-2-3-x-and-2-2-x]]
