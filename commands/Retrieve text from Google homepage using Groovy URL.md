---
id: d9619c55-b6cd-4cae-b754-d26179bf856e
name: Retrieve text from Google homepage using Groovy URL
type: command
executor: bash
data: ${new URL("http://www.google.com").getText()}
output: null
created_at: '2023-04-06T03:56:39.172941+00:00'
updated_at: '2023-04-10T20:23:32.567347+00:00'
---

# Retrieve text from Google homepage using Groovy URL

```bash
${new URL("http://www.google.com").getText()}
```
