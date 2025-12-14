---
id: cmd-uuid-002
data: gem update rdoc
tags:
  - mitigation
  - update
type: command
output: Updated RDoc gem
executor: bash
platforms:
  - Ruby
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:07.889Z'
verified: false
validated: true
submitted: true
---
# gem-update-rdoc

## Command

```bash
gem update rdoc
```

## Description

Updates the RDoc gem to the latest version, mitigating CVE-2024-27281 by patching unsafe YAML deserialization. Use after identifying vulnerability to prevent RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Updates to latest | No |
| --system | Update system gems | No |

## Examples

### Basic Usage

```bash
gem update rdoc
```

### Advanced Usage

```bash
gem update rdoc --system
```

## Expected Output

Output indicating successful update, e.g., 'Successfully installed rdoc-6.6.3.1' and confirmation of version change.

## Related

- [[commands/rdoc-generate-documentation]]
- [[procedures/Exploit-RDoc-YAML-Deserialization-for-RCE]]
