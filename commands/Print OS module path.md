---
id: 35e3e0b1-eb43-41f5-8829-e0c99151c77f
name: Print OS module path
type: command
executor: bash
data: print(Template(\"${self.module.cache.util.os}\").render())
output: null
created_at: '2023-04-06T03:56:40.091629+00:00'
updated_at: '2023-04-10T20:23:30.386691+00:00'
---

# Print OS module path

```bash
print(Template(\"${self.module.cache.util.os}\").render())
```
