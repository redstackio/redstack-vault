---
id: aaf675d8-ff9c-459e-9577-fbb2f922568e
name: Add metadata to image
type: command
executor: bash
data: exiftool -Copyright="PayloadsAllTheThings" -Artist="Pentest" -ImageUniqueID="Example"
  payload.jpg
output: null
created_at: '2023-04-06T03:56:41.078561+00:00'
updated_at: '2023-04-10T20:24:34.601053+00:00'
---

# Add metadata to image

```bash
exiftool -Copyright="PayloadsAllTheThings" -Artist="Pentest" -ImageUniqueID="Example" payload.jpg
```


