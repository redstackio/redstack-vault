---
id: cmd-cp-rubyluabridge-so
data: sudo cp rubyluabridge.so /opt/gitlab/embedded/lib/ruby/2.7.0/rubyluabridge.so
tags:
  - deploy
  - copy
type: command
output: Copy success
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:50.126Z'
verified: false
validated: true
submitted: true
---
# cp-rubyluabridge-so

## Command

```bash
sudo cp rubyluabridge.so /opt/gitlab/embedded/lib/ruby/2.7.0/rubyluabridge.so
```

## Description

Copies the compiled rubyluabridge shared library to GitLab's Ruby installation for loading during wiki rendering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `rubyluabridge.so` | Source file | Yes |
| `/opt/gitlab/embedded/lib/ruby/2.7.0/rubyluabridge.so` | GitLab Ruby lib destination | Yes |

## Examples

### Basic Usage

```bash
sudo cp rubyluabridge.so /opt/gitlab/embedded/lib/ruby/2.7.0/rubyluabridge.so
```

### Advanced Usage

```bash
sudo cp -v rubyluabridge.so /opt/gitlab/embedded/lib/ruby/2.7.0/
```

## Expected Output

No output if successful; use `ls` to verify file presence.

## Related

- [[commands/make-build]]
- [[procedures/Install-rubyluabridge-for-Lua-Extension]]
