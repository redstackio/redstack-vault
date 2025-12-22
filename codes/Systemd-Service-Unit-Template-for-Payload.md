---
id: b9319854-294d-4a24-aa70-3ff461e9a5ae
type: code
language: ini
verified: true
created_at: '2019-10-16T23:21:22.671937+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
tags:
  - systemd
  - persistence
  - service-hijack
validated: true
---

# Systemd-Service-Unit-Template-for-Payload

## Code

```ini
[Unit]
Description=rootshell
[Service]
Type=notify
ExecStart=/bin/bash -c /tmp/rootshell
[Install]
WantedBy=multi-user.target
```

## Description

This is a template for a systemd service unit file that executes a payload script (e.g., a reverse shell) when the service starts. It uses Type=notify for reliability and targets multi-user mode for boot persistence. Customize the Description and ExecStart path for stealth and functionality.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Description | Human-readable name of the service (keep innocuous) | System Update Service |
| ExecStart | Full command/path to execute the payload | /bin/bash -c /tmp/payload.sh |
| /tmp/rootshell | Path to the staged payload file | /tmp/custom-payload |

## Usage

Save as a .service file (e.g., /tmp/malicious.service), link it with systemctl link, then enable/start with systemctl enable --now. This establishes persistence as the service will run on reboot. Use in scenarios with sudo/systemctl access for root execution.

## Detection

- File monitoring: New .service files or symlinks in /etc/systemd/system with suspicious ExecStart (e.g., /tmp paths).
- Service logs: 'journalctl -u service-name' showing execution of non-standard binaries.
- Integrity checks: Verify no unauthorized services via 'systemctl list-unit-files --type=service'.
- Behavioral: Root processes spawning from systemd to bash or network tools.

## Related

- [[procedures/Create-Systemd-Service-for-Persistence]]
- [[commands/systemctl-link-service-unit-file]]
