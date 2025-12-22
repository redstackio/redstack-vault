---
id: cmd-cat-acronis-001
name: cat-acronis-launchdaemons
type: command
executor: bash
data: cat /Library/LaunchDaemons/com.acronis.*
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.029Z'
platforms:
  - macOS
tags:
  - recon
  - macos
verified: false
validated: true
submitted: true
---

# cat-acronis-launchdaemons

## Command

```bash
cat /Library/LaunchDaemons/com.acronis.*
```

## Description

This command concatenates and displays the contents of all Acronis-related LaunchDaemon plist files in /Library/LaunchDaemons/, used to discover insecure configurations where root-executed binaries are located in writable directories.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Wildcard matches all com.acronis.* plists | Yes |

## Examples

### Basic Usage

```bash
cat /Library/LaunchDaemons/com.acronis.*
```

### Advanced Usage

Pipe to grep for specific elements:

```bash
cat /Library/LaunchDaemons/com.acronis.* | grep -A5 ProgramArguments
```

## Expected Output

XML plist files detailing LaunchDaemon configurations, including <ProgramArguments> pointing to executables in the writable app folder, such as /Applications/Acronis True Image.app/Contents/MacOS/prl_stat, mms_mini.sh, etc., with <UserName>root</UserName> and triggers like <RunAtLoad>true</RunAtLoad>.

## Related

- [[Related Procedure|procedures/Examine-Acronis-LaunchDaemon-Plist-Files]]
