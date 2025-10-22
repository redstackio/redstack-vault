---
id: 5a582ed1-3d8f-4d20-8b3a-c48db210a2c2
name: Enable External Scripts
type: command
executor: bash
data: 'sp_configure ''external scripts enabled'', 1;

  RECONFIGURE;'
output: null
created_at: '2023-04-06T03:56:20.580490+00:00'
updated_at: '2023-04-10T20:36:46.840714+00:00'
---

# Enable External Scripts

```bash
sp_configure 'external scripts enabled', 1;
RECONFIGURE;
```
