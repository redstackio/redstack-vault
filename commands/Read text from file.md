---
id: 4b015146-0e84-4ae3-83ff-829ed902e133
name: Read text from file
type: command
executor: bash
data: ${String x = new File('/path/to/file').getText('UTF-8')}
output: null
created_at: '2023-04-06T03:56:39.131545+00:00'
updated_at: '2023-04-10T20:23:42.039080+00:00'
---

# Read text from file

```bash
${String x = new File('/path/to/file').getText('UTF-8')}
```
