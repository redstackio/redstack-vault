---
data: cat /etc/hosts | grep fake-site.com
tags:
  - verification
  - network
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 5e15fbcc-f4ea-4b26-9986-ff8b87f7065a
created_at: '2025-12-14T03:15:26.525Z'
updated_at: '2025-12-14T03:15:26.525Z'
verified: false
validated: true
submitted: true
---
# cat-hosts

## Command

```bash
cat /etc/hosts | grep fake-site.com
```

## Description

Displays specific entries from the hosts file to verify DNS overrides, useful post-modification in hostname manipulation attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| grep fake-site.com | Filter for the domain | Yes |

## Examples

### Basic Usage

```bash
cat /etc/hosts | grep attacker.com
```

### Advanced Usage

```bash
cat /etc/hosts | grep -E "(fake|attacker)"
```

## Expected Output

Lines matching the grep, e.g., '11.22.33.44 fake-site.com'.

## Related

- [[commands/edit-hosts-file]]
- [[procedures/Override-Hosts-File-for-Fake-Domain-Mapping]]
