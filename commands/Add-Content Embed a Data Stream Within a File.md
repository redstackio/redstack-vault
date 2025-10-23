---
id: 77564bb4-3850-4738-a0fa-ca946ef4ed89
name: Add-Content Embed a Data Stream Within a File
type: command
executor: bash
data: Add-Content -Path $_COVER_FILE -Value "Hidden Data" -Stream $_EMBEDDED_FILE
output: PS C:\Users\Bob\Desktop> Add-Content -Path normal.txt -Value "Hidden Data"
  -Stream "hidden.txt"
created_at: '2019-11-26T17:51:06.858904+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Add-Content Embed a Data Stream Within a File

```bash
Add-Content -Path $_COVER_FILE -Value "Hidden Data" -Stream $_EMBEDDED_FILE
```

## Expected Output

```
PS C:\Users\Bob\Desktop> Add-Content -Path normal.txt -Value "Hidden Data" -Stream "hidden.txt"
```


