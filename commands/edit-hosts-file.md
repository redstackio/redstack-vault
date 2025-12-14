---
id: cmd-uuid-001
data: |
  |
    notepad %WINDIR%\sysnative\drivers\etc\hosts
    # Add line: 93.184.216.34 www.google.com
tags:
  - mitm
  - dns-redirect
type: command
output: Hosts file updated; subsequent resolutions point to specified IP.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:12.452Z'
verified: false
validated: true
submitted: true
---
# edit-hosts-file

## Command

```cmd
notepad %WINDIR%\sysnative\drivers\etc\hosts
# Manually add: 93.184.216.34 www.google.com
```

## Description

Edits the Windows hosts file to override DNS resolution for a domain, simulating MitM by pointing it to an alternate IP. Run as administrator to modify the protected file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| File Path | %WINDIR%\sysnative\drivers\etc\hosts (system hosts file) | Yes |
| Line Added | IP domain mapping (e.g., 93.184.216.34 www.google.com) | Yes |

## Examples

### Basic Usage

```cmd
notepad %WINDIR%\sysnative\drivers\etc\hosts
```

Open and append the redirection line.

### Advanced Usage

```cmd
# After edit, flush DNS:
ipconfig /flushdns
ping www.google.com
```

Verifies the change takes effect.

## Expected Output

File opens in Notepad; after save, ping tests confirm redirection to the new IP (e.g., 93.184.216.34).

## Related

- [[Related Procedure|procedures/Simulate-MitM-via-Hosts-File-Modification]]
