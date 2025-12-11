---
id: c45fd154-4879-43ae-851d-b9f890996adb
name: git-clone-trac-repo
type: command
executor: bash
data: 'git clone git://meta.git.wordpress.org/'
output: null
created_at: '2025-12-11T06:10:15.458Z'
updated_at: '2025-12-11T06:10:15.458Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - git
  - setup
verified: false
validated: true
submitted: true
---

# git-clone-trac-repo

## Command

```bash
git clone git://meta.git.wordpress.org/
```

## Description

This command clones the Git repository containing custom source code for WordPress Trac to set up a local testing environment, avoiding production testing as per policy.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `git://meta.git.wordpress.org/` | URL of the Git repository to clone | Yes |

## Examples

### Basic Usage

```bash
git clone git://meta.git.wordpress.org/
```

### Advanced Usage

```bash
git clone git://meta.git.wordpress.org/ --depth 1
```

## Expected Output

Cloned repository files in the current directory, with output showing cloning progress and completion.

## Related

- [[tools/Git]]
- [[procedures/Access-and-Prepare-for-Ticket-Creation-in-WordPress-Trac]]
