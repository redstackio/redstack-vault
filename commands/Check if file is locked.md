---
id: 161d3453-1485-4042-8b88-5b36e941db4e
name: Check if file is locked
type: command
executor: bash
data: '@echo off; 2>nul ( >>file.txt echo off) && (echo not locked) || (echo locked)

  '
output: null
created_at: '2020-07-14T18:21:27.749254+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Check if file is locked

```bash
@echo off; 2>nul ( >>file.txt echo off) && (echo not locked) || (echo locked)

```


