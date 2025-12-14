---
data: 'sudo -u www-data php occ user:info username'
tags:
  - nextcloud
  - management
  - workaround
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.998Z'
id: d823e8c8-4cb4-409f-9385-67d448c8452a
verified: false
validated: true
submitted: true
---
# nextcloud-occ-manage-users

## Command

```bash
sudo -u www-data php occ user:info username
```

## Description

This command uses Nextcloud's OCC (OwnCloud Console) tool to manage users via the command line, serving as a workaround when the web administration interface is broken due to a DoS vulnerability. It allows admins to view, edit, or list user information without relying on the vulnerable UI.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sudo -u www-data` | Run as the web server user (adjust for your setup, e.g., apache) | Yes |
| `php occ` | Path to PHP and OCC script (typically in Nextcloud root) | Yes |
| `user:info` | Subcommand to display user details | No (use others like `user:list` for listing) |
| `username` | Target username to query | Yes for info command |

## Examples

### Basic Usage

```bash
sudo -u www-data php occ user:info demo
```

### Advanced Usage

```bash
sudo -u www-data php occ user:list --output=json
```

This lists all users in JSON format for scripting.

## Expected Output

User details such as display name, email, enabled status, and groups, e.g.:

- User   : demo
- Display: Demo User
- Mail   : demo@example.com
- Enabled: Yes

If the command succeeds, it confirms CLI management works despite web UI failure.

## Related

- [[Related Procedure|procedures/Trigger-DoS-in-Nextcloud-User-Administration]]
