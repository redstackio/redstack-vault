---
id: 06170efa-a413-4358-bb78-ee780652dec9
name: List system databases
type: command
executor: bash
data: SELECT DB_NAME(N); -- for N = 0, 1, 2, ...
output: null
created_at: '2023-04-06T03:56:33.639321+00:00'
updated_at: '2023-04-10T20:22:46.899409+00:00'
---

# List system databases

```bash
SELECT DB_NAME(N); -- for N = 0, 1, 2, ...
```
