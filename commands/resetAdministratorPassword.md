---
id: cmd-burp-reset-password-001
data: |
  |
    ./resetAdministratorPassword
tags:
  - password-reset
  - admin
type: command
output: Password reset successful. New password applied.
executor: bash
platforms:
  - Linux
  - Java
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.114Z'
verified: false
validated: true
submitted: true
---
# resetAdministratorPassword

## Command

```bash
./resetAdministratorPassword
```

## Description

This command resets the administrator password for Burp Suite Enterprise using the provided script. It is used in administrative tasks or testing to change the admin password, but notably does not invalidate existing sessions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None (interactive) | Script prompts for new password input | Yes |

## Examples

### Basic Usage

```bash
./resetAdministratorPassword
```

Run from the Burp Suite Enterprise scripts directory. The script will prompt: "Enter new password:" and "Confirm new password:"

### Advanced Usage

No advanced flags; always interactive for security.

## Expected Output

Description of what output to expect when the command runs successfully.

Success message: "Administrator password reset successfully." If passwords don't match, error: "Passwords do not match."

## Related

- [[procedures/Reset-Burp-Suite-Admin-Password-via-Script]]
