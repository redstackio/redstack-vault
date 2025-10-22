---
id: 3287bd4f-f679-406f-8553-16e357194781
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:56:17.631472+00:00'
updated_at: '2023-04-10T20:34:11.681062+00:00'
---

# Code Snippet 3287bd4f

**Language**: Bash

```bash
# A decoy file with no special characters
touch 'index.php'

# An imposter file with visually identical name
touch $'index\u200D.php'
```
