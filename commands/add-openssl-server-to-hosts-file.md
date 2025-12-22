---
id: d88b1934-7077-4e48-88fa-1d9f74d16be8
name: add-openssl-server-to-hosts-file
type: command
executor: bash
data: sudo echo "$_SERVER_IP $_TARGET_DOMAIN" >> /etc/hosts
output: null
created_at: '2023-04-06T03:56:22.335771+00:00'
updated_at: '2023-04-10T20:25:09.843906+00:00'
platforms:
  - Linux
tags:
  - mitm
  - hosts-modification
verified: true
validated: true
---

# add-openssl-server-to-hosts-file

## Command

```bash
sudo echo "$_SERVER_IP $_TARGET_DOMAIN" >> /etc/hosts
```

## Description

This command appends an entry to the /etc/hosts file on a Linux client, redirecting traffic for a specific domain to an attacker-controlled IP. It's used in MITM setups to poison local hostname resolution, forcing SSL connections to the attacker's server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SERVER_IP | IP address of the MITM server | Yes |
| $_TARGET_DOMAIN | Domain name to redirect (e.g., example.com) | Yes |

## Examples

### Basic Usage

```bash
sudo echo "192.168.1.100 example.com" >> /etc/hosts
```

### Verification

After running, use [[commands/view-hosts-file]] to confirm the entry.

## Expected Output

No stdout output; the command silently appends the line. Success is confirmed by checking /etc/hosts contents.

## Related

- [[procedures/SSL-MITM-Network-Discovery-with-OpenSSL]]
- [[commands/view-hosts-file]]
