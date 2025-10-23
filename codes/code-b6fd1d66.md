---
id: b6fd1d66-20aa-4086-88f8-c0320a90e115
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:20.683206+00:00'
updated_at: '2023-04-10T20:36:47.547107+00:00'
---

# Code Snippet b6fd1d66

**Language**: SQL

```sql
Invoke-SQLAuditPrivTrustworthy -Instance "<DBSERVERNAME\DBInstance>" -Exploit -Verbose 

SELECT name as database_name, SUSER_NAME(owner_sid) AS database_owner, is_trustworthy_on AS TRUSTWORTHY from sys.databases
```


