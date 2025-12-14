---
data: system("id")
tags:
  - rce
  - php
  - shell
type: command
executor: php
platforms:
  - Linux
id: 7eb58862-ab9c-439d-a1a0-eb09aee16210
created_at: '2025-12-14T17:23:54.971Z'
updated_at: '2025-12-14T17:23:54.971Z'
verified: false
validated: true
submitted: true
---
# system-id-execution

## Command

```php
system("id");
```

## Description

This PHP command executes the 'id' shell command to display the current user and group information, used here as a proof-of-concept for RCE triggered by deserialization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `"id"` | The shell command to execute (displays user ID) | Yes |

## Examples

### Basic Usage

```php
system("id");
```

### Advanced Usage

```php
system("whoami");
```

## Expected Output

uid=33(www-data) gid=33(www-data) groups=33(www-data)

## Related

- [[commands/curl-exploit-deserialization-rce]]
