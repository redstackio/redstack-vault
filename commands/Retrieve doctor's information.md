---
id: 4f37f88a-2932-48a0-9e2b-b0dfebd2443f
name: Retrieve doctor's information
type: command
executor: bash
data: '{doctors(options: "{\"patients.ssn\" :1}"){firstName lastName id patients{ssn}}}'
output: null
created_at: '2023-04-06T03:55:58.845262+00:00'
updated_at: '2023-04-10T20:22:22.551857+00:00'
---

# Retrieve doctor's information

```bash
{doctors(options: "{\"patients.ssn\" :1}"){firstName lastName id patients{ssn}}}
```
