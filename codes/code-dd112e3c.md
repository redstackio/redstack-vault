---
id: dd112e3c-04f3-4a32-80de-01aff1277c1f
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:33.815785+00:00'
updated_at: '2023-04-10T20:22:41.316592+00:00'
---

# Code Snippet dd112e3c

**Language**: SQL

```sql
For integer inputs : convert(int,@@version)
For integer inputs : cast((SELECT @@version) as int)

For string inputs   : ' + convert(int,@@version) + '
For string inputs   : ' + cast((SELECT @@version) as int) + '
```


