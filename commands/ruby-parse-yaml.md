---
id: cmd-uuid-3456
data: ruby -ryaml -e "puts YAML.load(ARGF.read)" < malicious.yaml
tags:
  - yaml
  - parse
  - dos
type: command
output: null
executor: bash
platforms:
  - Software
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.902Z'
verified: false
validated: true
submitted: true
---
# ruby-parse-yaml

## Command

```bash
ruby -ryaml -e "puts YAML.load(ARGF.read)" < malicious.yaml
```

## Description

This command loads and parses YAML input using Ruby's YAML library, useful for testing vulnerability to malicious input causing DoS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-ryaml` | Requires the YAML library | Yes |
| `-e` | Executes the Ruby code snippet | Yes |
| `< malicious.yaml` | Provides input file | Yes |

## Examples

### Basic Usage

```bash
ruby -ryaml -e "puts YAML.load(ARGF.read)" < test.yaml
```

### Advanced Usage

Use in a script for more complex parsing:

```bash
ruby parse_script.rb
```

## Expected Output

For valid YAML, parsed content; for malicious, process crash or error due to memory corruption.

## Related

- [[Related Procedure|procedures/Exploit-libYAML-DoS-in-Ruby-2-3-x-and-2-2-x]]
