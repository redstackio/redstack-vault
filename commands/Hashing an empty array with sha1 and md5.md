---
id: 4234ae79-c0a7-41f2-a672-b9ee893fdbe0
name: Hashing an empty array with sha1 and md5
type: command
executor: bash
data: 'var_dump(sha1([])); # NULL

  var_dump(md5([]));  # NULL'
output: null
created_at: '2023-04-06T03:56:40.673509+00:00'
updated_at: '2023-04-06T03:56:40.681271+00:00'
---

# Hashing an empty array with sha1 and md5

```bash
var_dump(sha1([])); # NULL
var_dump(md5([]));  # NULL
```


