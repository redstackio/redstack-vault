---
data: sudo -u git /bin/bash
tags:
  - user-switch
  - sudo
type: command
output: bash prompt as git user
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:56.986Z'
id: 4acfad82-42cd-44fb-9b02-2c76dd357ea5
verified: false
validated: true
submitted: true
---
# sudo-switch-to-git

## Command

```bash
sudo -u git /bin/bash
```

## Description

Switches to the 'git' system user shell using sudo, simulating local access to the vulnerable user in GitLab setups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u git | Target user 'git' | Yes |
| /bin/bash | Shell to invoke | Yes |

## Examples

### Basic Usage

```bash
sudo -u git /bin/bash
```

### Advanced Usage

```bash
sudo -u git -i /bin/bash
```

## Expected Output

Prompt changes to 'git@hostname:~$'

## Related

- [[commands/apt-get-install-packages]]
- [[procedures/Prepare-Environment-as-Git-User]]
