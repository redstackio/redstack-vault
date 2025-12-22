---
id: 802302f3-40e4-4dbb-bfd4-51dd608dceb3
name: Map-Remote-Share-as-Network-Drive
type: command
executor: cmd
data: 'net use T: \\$_DOMAIN\C$\Users\Public /user:$_DOMAIN\$_USERNAME $_PASSWORD'
output: null
created_at: '2023-01-12T22:19:00.382798+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - '[[tags/file-transfer]]'
  - '[[tags/lateral-movement]]'
verified: true
validated: true
---

# Map-Remote-Share-as-Network-Drive

## Command

```cmd
net use T: \\$_DOMAIN\C$\Users\Public /user:$_DOMAIN\$_USERNAME $_PASSWORD
```

## Description

This command establishes a network connection to a remote Windows machine's administrative share (C$) using SMB, mapping it to the local T: drive. It authenticates with domain credentials and targets the Users\Public subdirectory for easy file drops. Use this prior to file transfers in lateral movement scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| T: | Local drive letter to assign (e.g., T:, Z:) | Yes |
| $_DOMAIN | Target domain or machine name (e.g., example.com or TARGETHOST) | Yes |
| C$\Users\Public | Remote path: Administrative root share and public folder | Yes |
| /user:$_DOMAIN\$_USERNAME | Specifies the domain and username for authentication | Yes |
| $_PASSWORD | Plaintext password for the user | Yes |

## Examples

### Basic Usage

```cmd
net use T: \\example.com\C$\Users\Public /user:example.com\admin pass123
```

### Advanced Usage

```cmd
net use Z: \\192.168.1.100\C$\Windows\Temp /user:DOMAIN\user123 mypass /persistent:no
```

## Expected Output

When successful:

```
The command completed successfully.
```

If failed (e.g., invalid credentials):

```
System error 5 has occurred.
Access is denied.
```

## Related

- [[procedures/Copy-File-to-Remote-Windows-Machine-via-Xcopy]]
- [[Remote File Copy]]
