---
type: command
executor: bash
data: locate password | more
tags:
  - looting
  - recon
platforms:
  - Linux
verified: true
validated: true
---

# locate-search-password-files

## Command

```bash
locate password | more
```

## Description

This command searches the system's locate database for files and directories containing 'password' in their name, piping the results to 'more' for paginated display. It's useful for quick reconnaissance of potential credential storage locations on Linux without needing root access for the search itself.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `password` | Search pattern (keyword to match in filenames) | Yes |
| `| more` | Pipes output to 'more' for scrolling through long results | No (use `less` or omit for full dump) |

## Examples

### Basic Usage

```bash
locate password | more
```

### Alternative with Grep for Filtering

```bash
locate password | grep -i config | more
```

### Without Pagination

```bash
locate password > password_files.txt
```

## Expected Output

A list of file paths matching the pattern, displayed page by page:

```
/boot/grub/i386-pc/password.mod
/etc/pam.d/common-password
/etc/pam.d/gdm-password
/etc/pam.d/gdm-password.original
/lib/live/config/0031-root-password
...

--More--(50%)
```

Press space to continue, q to quit. No files found indicates an outdated database or no matches.

## Related

- [[procedures/Linux-Password-Looting]] (procedure that uses this command)
- [[updatedb-update-locate-database]] (related command for database maintenance)
