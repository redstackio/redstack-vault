---
id: cmd-gitlab-rails-console
data: sudo gitlab-rails console
tags:
  - gitlab
  - admin
type: command
output: Interactive Ruby console prompt
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.597Z'
verified: false
validated: true
submitted: true
---
# gitlab-rails-console

## Command

```bash
sudo gitlab-rails console
```

## Description

Opens the GitLab Rails console for executing Ruby code, such as enabling feature flags, in an interactive session on the GitLab server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sudo | Run with elevated privileges | Yes |
| gitlab-rails | GitLab Rails executable | Yes |
| console | Starts interactive IRB session | Yes |

## Examples

### Basic Usage

```bash
sudo gitlab-rails console
```

### Advanced Usage

Run directly after for flag enable: `sudo gitlab-rails console -e production` (if needed).

## Expected Output

Interactive prompt like `>> ` for Ruby commands; type `exit` to quit.

## Related

- [[commands/feature-enable-bulk-import]]
