---
id: f90076ee-5484-4cdc-8861-6474d95f72d6
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:24.983225+00:00'
updated_at: '2023-04-10T20:25:31.246275+00:00'
---

# Code Snippet f90076ee

**Language**: Powershell

```powershell
rlwrap nc 10.0.0.1 4242

rlwrap -r -f . nc 10.0.0.1 4242
-f . will make rlwrap use the current history file as a completion word list.
-r Put all words seen on in- and output on the completion list.
```
