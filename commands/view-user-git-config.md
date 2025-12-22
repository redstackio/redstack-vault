---
id: fadc6c36-586f-433b-b589-bf31961ee459
name: view-user-git-config
type: command
executor: bash
data: cat ~/.gitconfig
output: null
created_at: '2023-04-06T03:56:18.371452+00:00'
updated_at: '2023-04-10T20:34:17.912573+00:00'
platforms:
  - Linux
tags:
  - git
  - config
  - verification
verified: true
validated: true
---

# view-user-git-config

## Command

```bash
cat ~/.gitconfig
```

## Description

This command displays the contents of the user's global Git configuration file (~/.gitconfig), allowing verification of settings like core.hooksPath after modifications. Use this to confirm persistence configurations or audit changes in a Git environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ~/.gitconfig | Default path to the user-level Git config file | Built-in (fixed) |

## Examples

### Basic Usage

```bash
cat ~/.gitconfig
```

### Advanced Usage

```bash
cat /home/otheruser/.gitconfig
```

## Expected Output

The full contents of the gitconfig file, structured in INI format. For example:
```
[user]
	name = John Doe
	email = john@example.com
[core]
	hooksPath = /home/user/.git-hooks
[alias]
	st = status
```
Look for specific sections like [core] to validate hook path changes. If the file doesn't exist, output is empty; create it implicitly by running git config commands first.

## Related

- [[procedures/Git-Hook-Persistence]]
- [[commands/git-config-set-global-hooks-path]]
