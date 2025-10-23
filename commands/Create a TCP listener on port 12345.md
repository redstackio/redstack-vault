---
id: 42f68627-7e7f-46c7-b4fe-10cb66b6051b
name: Create a TCP listener on port 12345
type: command
executor: bash
data: socat file:`tty`,raw,echo=0 tcp-listen:12345
output: null
created_at: '2023-04-06T03:56:24.983692+00:00'
updated_at: '2023-04-10T20:25:31.247390+00:00'
---

# Create a TCP listener on port 12345

```bash
socat file:`tty`,raw,echo=0 tcp-listen:12345
```


