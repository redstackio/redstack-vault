---
id: e61ecaad-e228-4014-abf9-4f339f8e62bf
name: systemctl-list-timers-all
type: command
executor: bash
data: systemctl list-timers --all
output: null
created_at: '2023-04-06T03:56:18.766285+00:00'
updated_at: '2023-04-10T20:34:34.076380+00:00'
platforms:
  - Linux
tags:
  - systemd
  - enumeration
verified: true
validated: true
---

# systemctl-list-timers-all

## Command

```bash
systemctl list-timers --all
```

## Description

This command lists all systemd timers on the system, including active, inactive, and failed ones. It is used during privilege escalation reconnaissance to identify scheduled tasks that may be abusable for running code as root.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --all | Show all units, not just active ones | Yes |

## Examples

### Basic Usage

```bash
systemctl list-timers --all
```

### Advanced Usage

```bash
systemctl list-timers --all | grep apt
```

> Filters for timers related to apt updates.

## Expected Output

```
NEXT                          LEFT     LAST                          PASSED             UNIT                         ACTIVATES
Mon 2019-04-01 02:59:14 CEST  15h left Sun 2019-03-31 10:52:49 CEST  24min ago          apt-daily.timer              apt-daily.service
Mon 2019-04-01 06:20:40 CEST  19h left Sun 2019-03-31 10:52:49 CEST  24min ago          apt-daily-upgrade.timer      apt-daily-upgrade.service
Mon 2019-04-01 07:36:10 CEST  20h left Sat 2019-03-09 14:28:25 CET   3 weeks 0 days ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service

3 timers listed.
```

A table showing timer details. Success if timers are listed without errors.

## Related

- [[procedures/Linux-Privilege-Escalation-via-Systemd-Timers]]
