---
data: grep -rE 'username|password' repo/
tags:
  - search
  - credentials
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: d668bacb-c4b4-4dc5-a5f4-80c3f34115e9
created_at: '2025-12-11T03:47:56.535Z'
updated_at: '2025-12-11T03:47:56.535Z'
verified: false
validated: true
submitted: true
---
# grep-search-credentials

## Command

```bash
grep -rE 'username|password' repo/
```

## Description

Recursively searches files in a directory for patterns matching credentials like usernames or passwords.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-rE` | Recursive search with extended regex | Yes |
| `'username|password'` | Search pattern | Yes |
| `repo/` | Directory to search | Yes |

## Examples

### Basic Usage

```bash
grep -rE 'username|password' repo/
```

### Advanced Usage

```bash
grep -rE 'jfrog|artifactory' repo/
```

## Expected Output

List of matching lines with file paths, e.g., 'repo/config.yaml: username: leakeduser'

## Related

- [[commands/git-clone-repo]]
- [[procedures/Discover-Leaked-Credentials-in-Public-GitHub-Repository]]
