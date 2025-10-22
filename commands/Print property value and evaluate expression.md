---
id: 812ad185-e2a9-4003-bd1d-338f0e61bf3c
name: Print property value and evaluate expression
type: command
executor: bash
data: '"${<property>}\n${1+1}\n\n#{<expression string>}\n#{1+1}\n\nT(<javaclass>)"'
output: null
created_at: '2023-04-06T03:56:38.949036+00:00'
updated_at: '2023-04-10T20:23:41.643219+00:00'
---

# Print property value and evaluate expression

```bash
"${<property>}\n${1+1}\n\n#{<expression string>}\n#{1+1}\n\nT(<javaclass>)"
```
