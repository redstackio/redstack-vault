---
type: command
executor: bash
data: >-
  cat /etc/cron.allow 2>/dev/null || echo "No cron.allow file (all users
  allowed)"; cat /etc/cron.deny 2>/dev/null || echo "No cron.deny file (all
  users allowed unless in allow)"; cat /etc/at.allow 2>/dev/null || echo "No
  at.allow file"; cat /etc/at.deny 2>/dev/null || echo "No at.deny file"
platforms:
  - Linux
tags:
  - enumeration
  - cron
  - access-control
verified: true
validated: true
---

# view-cron-access-control-files

## Command

```bash
cat /etc/cron.allow 2>/dev/null || echo "No cron.allow file (all users allowed)"; cat /etc/cron.deny 2>/dev/null || echo "No cron.deny file (all users allowed unless in allow)"; cat /etc/at.allow 2>/dev/null || echo "No at.allow file"; cat /etc/at.deny 2>/dev/null || echo "No at.deny file"
```

## Description

Displays contents of cron and at access control files, providing fallbacks if files don't exist, to determine if the current user can schedule jobs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses conditional cat with echo fallbacks | N/A |

## Examples

### Basic Usage

```bash
cat /etc/cron.allow 2>/dev/null || echo "No cron.allow file (all users allowed)"; cat /etc/cron.deny 2>/dev/null || echo "No cron.deny file (all users allowed unless in allow)"; cat /etc/at.allow 2>/dev/null || echo "No at.allow file"; cat /etc/at.deny 2>/dev/null || echo "No at.deny file"
```

## Expected Output

File contents or messages, e.g.:
root
admin
No cron.deny file (all users allowed unless in allow)
No at.allow file
No at.deny file

## Related

- [[procedures/Linux-Privilege-Escalation-via-Scheduled-Tasks]]
- [[commands/enumerate-cron-jobs-and-directories]]
