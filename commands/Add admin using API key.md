---
id: 89ee9e89-1213-4b73-a49c-777211913df9
name: Add admin using API key
type: command
executor: bash
data: SCMKit.exe -s gitlab -m addadmin -c apikey -u https://gitlab.something.local
  -o targetUserName
output: null
created_at: '2023-04-06T03:56:25.112852+00:00'
updated_at: '2023-04-10T20:34:07.180628+00:00'
---

# Add admin using API key

```bash
SCMKit.exe -s gitlab -m addadmin -c apikey -u https://gitlab.something.local -o targetUserName
```


