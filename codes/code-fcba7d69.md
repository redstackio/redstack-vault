---
id: fcba7d69-c521-4578-aea8-e0279b3ad2c3
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:07.394024+00:00'
updated_at: '2023-04-10T20:26:01.513573+00:00'
---

# Code Snippet fcba7d69

**Language**: ps1

```ps1
# execute on our forest
netdom trust lab.local /domain:bastion.local /ForestTransitive:Yes 
netdom trust lab.local /domain:bastion.local /EnableSIDHistory:Yes 
netdom trust lab.local /domain:bastion.local /EnablePIMTrust:Yes 
netdom trust lab.local /domain:bastion.local /Quarantine:No
# execute on our bastion
netdom trust bastion.local /domain:lab.local /ForestTransitive:Yes
```
