---
id: 46d946ad-04fb-44b2-a5d1-7bfe1ff17c3a
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:35.929702+00:00'
updated_at: '2023-04-10T20:23:15.909922+00:00'
---

# Code Snippet 46d946ad

**Language**: SQL

```sql
SELECT lo_import('/etc/passwd'); -- This command imports a file and creates a large object from it in PostgreSQL. The OID of the large object is returned.
SELECT lo_get(16420); -- This command retrieves the large object with the specified OID.
SELECT * from pg_largeobject; -- This command retrieves all large objects and their data from the pg_largeobject system table.
```


