---
id: 13739088-8a1b-43ea-98a2-5956b51cde17
name: windows-attrib-set-file-hidden
type: command
executor: cmd
data: attrib +h $_FILE_PATH
output: null
created_at: '2023-04-06T03:56:27.744938+00:00'
updated_at: '2023-04-10T20:37:22.093837+00:00'
platforms:
  - Windows
tags:
  - defense-evasion
  - persistence
verified: true
validated: true
---

# windows-attrib-set-file-hidden

## Command

```cmd
attrib +h $_FILE_PATH
```

## Description

This command sets the hidden attribute on a specified file or directory in Windows, making it invisible in standard file listings unless explicitly shown. Use this during post-exploitation to conceal persistence artifacts like backdoor scripts from casual discovery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| +h | Sets the hidden attribute (use -h to remove) | Yes |
| $_FILE_PATH | Full path to the target file or directory (e.g., c:\autoexec.bat) | Yes |

## Examples

### Basic Usage

```cmd
attrib +h c:\autoexec.bat
```

Hides the autoexec.bat file in the C: root.

### Advanced Usage

```cmd
attrib +h +s c:\hidden_dir\payload.exe
```

Sets both hidden (+h) and system (+s) attributes for additional evasion.

## Expected Output

On success, the command executes silently with no output. Errors appear if the file doesn't exist (e.g., "Could not find c:\nonexistent.bat"). Verify with `dir /a:h` to see the hidden file listed with an 'H' attribute.

## Related

- [[procedures/windows-hide-file-for-persistence]]
