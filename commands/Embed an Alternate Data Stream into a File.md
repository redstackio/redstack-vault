---
id: ab7d6336-9462-43fe-b6ad-d1756d133b2b
name: Embed an Alternate Data Stream into a File
type: command
executor: command_prompt
data: type $_EMBEDDED_FILE > $_COVER_FILE:secret
output: C:\>type id_rsa > normal.txt:secret
created_at: '2019-11-22T17:24:23.001983+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Embed an Alternate Data Stream into a File

```command_prompt
type $_EMBEDDED_FILE > $_COVER_FILE:secret
```

## Expected Output

```
C:\>type id_rsa > normal.txt:secret
```
