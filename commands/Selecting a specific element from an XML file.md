---
id: 77dd856e-d514-4f58-babd-0cccf18d82b2
name: Selecting a specific element from an XML file
type: command
executor: bash
data: xmlstarlet sel -t -v '//book[2]/title' -nl data/books.xml
output: null
created_at: '2023-04-06T03:56:44.656832+00:00'
updated_at: '2023-04-10T20:24:43.080287+00:00'
---

# Selecting a specific element from an XML file

```bash
xmlstarlet sel -t -v '//book[2]/title' -nl data/books.xml
```


