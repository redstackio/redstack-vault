---
id: f2ff86aa-a2fa-4dee-9d8e-be43998b3bbe
name: Create trust between lab.local and bastion.local
type: command
executor: bash
data: "netdom trust lab.local /domain:bastion.local /ForestTransitive:Yes \nnetdom\
  \ trust lab.local /domain:bastion.local /EnableSIDHistory:Yes \nnetdom trust lab.local\
  \ /domain:bastion.local /EnablePIMTrust:Yes \nnetdom trust lab.local /domain:bastion.local\
  \ /Quarantine:No"
output: null
created_at: '2023-04-06T03:56:07.394107+00:00'
updated_at: '2023-04-10T20:26:01.511941+00:00'
---

# Create trust between lab.local and bastion.local

```bash
netdom trust lab.local /domain:bastion.local /ForestTransitive:Yes 
netdom trust lab.local /domain:bastion.local /EnableSIDHistory:Yes 
netdom trust lab.local /domain:bastion.local /EnablePIMTrust:Yes 
netdom trust lab.local /domain:bastion.local /Quarantine:No
```


