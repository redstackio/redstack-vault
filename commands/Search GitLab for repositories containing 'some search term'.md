---
id: a0d8d26b-d139-4511-9a8e-b8adc6fe75da
name: Search GitLab for repositories containing 'some search term'
type: command
executor: bash
data: SCMKit.exe -s gitlab -m searchrepo -c apikey -u https://gitlab.something.local
  -o "some search term"
output: null
created_at: '2023-04-06T03:56:25.111905+00:00'
updated_at: '2023-04-10T20:34:07.180628+00:00'
---

# Search GitLab for repositories containing 'some search term'

```bash
SCMKit.exe -s gitlab -m searchrepo -c apikey -u https://gitlab.something.local -o "some search term"
```
