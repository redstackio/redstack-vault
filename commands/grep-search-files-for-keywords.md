---
id: 0db9e66b-66a6-404a-9eb0-ab25b367fb03
name: grep-search-files-for-keywords
type: command
executor: bash
data: grep -C 5 -iR '$_KEYWORD1|$_KEYWORD2' *
output: |
  root@kali:~# grep -C 5 -iR 'password|secret' *
  ./hidden.txt: The password is hunter2.
created_at: '2019-10-09T18:38:08.439612+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - search
  - grep
verified: true
validated: true
---

# grep-search-files-for-keywords

## Command

```bash
grep -C 5 -iR '$_KEYWORD1|$_KEYWORD2' *
```

## Description

Recursively searches all files in the current directory and subdirectories for specified keywords, providing 5 lines of context around each match. This is useful for enumerating file systems in security assessments to locate sensitive information like credentials or configuration details. The search is case-insensitive and uses a pipe-separated pattern for multiple keywords.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -C 5 | Show 5 lines of output context (before and after matches) | Yes |
| -i | Perform case-insensitive matching | Yes |
| -R | Recursively search directories | Yes |
| $_KEYWORD1 | First keyword to search for (e.g., 'password') | Yes |
| $_KEYWORD2 | Second keyword to search for (e.g., 'secret') | Yes |
| * | Wildcard to search all files in current directory | Yes |

## Examples

### Basic Usage

Search for 'password' in current directory recursively:

```bash
grep -C 5 -iR 'password' *
```

### Advanced Usage

Search for multiple keywords with line numbers:

```bash
grep -C 5 -iR -n 'password|secret|key' *
```

## Expected Output

The command outputs matching lines with context, prefixed by the filename if searching multiple files. Example:

```
root@kali:~# grep -C 5 -iR 'password|secret' *
./hidden.txt: The password is hunter2.
./config.ini--secret_key=abc123
```

Matches with surrounding lines for context, helping identify the relevance of findings.

## Related

- [[tools/grep]] (parent tool)
