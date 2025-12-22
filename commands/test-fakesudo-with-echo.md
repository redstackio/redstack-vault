---
type: command
executor: bash
data: fakesudo echo 'You do not have the necessary permissions to run this command'
platforms:
  - Linux
  - Unix
tags:
  - testing
  - backdoor
  - credential-theft
verified: true
validated: true
---

# test-fakesudo-with-echo

## Command

```bash
fakesudo echo 'You do not have the necessary permissions to run this command'
```

## Description

Tests the fake sudo backdoor by invoking it directly (or via alias) with a simple echo command. This triggers the password prompt, logs the input, and demonstrates the masquerading behavior.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| echo | Example command to run via fake sudo | Yes |
| 'You do not have the necessary permissions...' | Argument to echo (customize as needed) | No |

## Examples

### Basic Test

```bash
fakesudo echo 'test message'
```

### Via Alias (Post-Setup)

```bash
sudo echo 'test message'
```

## Expected Output

Prompt: [sudo] password for user: (user enters password)

Then: Sorry, try again. (after 2s delay)

Followed by actual sudo execution output, e.g.:

test message

The password is logged to /tmp/pass.txt.

## Related

- [[procedures/Implement-Sudo-Backdoor-via-Bashrc-Alias]]
- [[commands/create-sudo-alias-in-bashrc]]
