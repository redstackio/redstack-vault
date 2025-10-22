---
id: 2f29a908-5b5c-4da6-b210-155f938dabc8
name: Convert Raw Security Descriptor to Byte Array
type: command
executor: bash
data: $SDBytes = New-Object byte[] ($SD.BinaryLength); $SD.GetBinaryForm($SDBytes,
  0)
output: null
created_at: '2023-04-06T03:56:07.771533+00:00'
updated_at: '2023-04-06T03:56:07.808488+00:00'
---

# Convert Raw Security Descriptor to Byte Array

```bash
$SDBytes = New-Object byte[] ($SD.BinaryLength); $SD.GetBinaryForm($SDBytes, 0)
```
