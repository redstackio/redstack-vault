---
data: echo "IP fake-site.com" | sudo tee -a /etc/hosts
tags:
  - network
  - dns
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: edbd846f-11dd-462b-a332-1fdde56a5116
created_at: '2025-12-14T03:15:26.527Z'
updated_at: '2025-12-14T03:15:26.527Z'
verified: false
validated: true
submitted: true
---
# edit-hosts-file

## Command

```bash
echo "11.22.33.44 fake-site.com" | sudo tee -a /etc/hosts
```

## Description

Appends a DNS override entry to the local hosts file, mapping an IP to a custom domain for local resolution manipulation in attacks like cache poisoning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| IP | Target IP address to map | Yes |
| fake-site.com | Fake domain name | Yes |

## Examples

### Basic Usage

```bash
echo "192.168.1.1 attacker.com" | sudo tee -a /etc/hosts
```

### Advanced Usage

```bash
echo "11.22.33.44 fake-site.com www.fake-site.com" | sudo tee -a /etc/hosts
```

## Expected Output

No stdout; the file is updated silently. Verify with `cat /etc/hosts` showing the new line.

## Related

- [[commands/cat-hosts]]
- [[procedures/Override-Hosts-File-for-Fake-Domain-Mapping]]
