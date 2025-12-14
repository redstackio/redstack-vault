---
data: php bin/config set auth.require-email-verification false
tags:
  - config
  - phabricator
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.227Z'
id: 37371162-d857-4ac8-8295-d7d9469df996
verified: false
validated: true
submitted: true
---
---

# phabricator-config-disable-email-verification

## Command

```bash
php bin/config set auth.require-email-verification false
```

## Description

This command configures a local Phabricator installation to disable mandatory email verification for user login, simulating production environments where verification is optional and enabling testing of unlimited resend functionality.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `set` | Config set operation | Yes |
| `auth.require-email-verification` | Key for email verification requirement | Yes |
| `false` | Value to disable verification | Yes |

## Examples

### Basic Usage

```bash
php bin/config set auth.require-email-verification false
```

### Advanced Usage

In a Phabricator root directory:

```bash
php bin/config set --global auth.require-email-verification false
```

## Expected Output

Configuration updated; users can now log in without verifying email, allowing access to verification endpoints for repeated requests. Output: "Configuration updated."

## Related

- [[Related Procedure]]
