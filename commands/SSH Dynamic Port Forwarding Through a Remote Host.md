---
id: 20dbbbbc-ad44-4f6f-bdbc-e9cf120186b4
name: SSH Dynamic Port Forwarding Through a Remote Host
type: command
executor: bash
data: ssh -f -N -D $_PORT $_USERNAME@$_TARGET_IP
output: null
created_at: '2019-10-02T01:10:12.259359+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SSH Dynamic Port Forwarding Through a Remote Host

```bash
ssh -f -N -D $_PORT $_USERNAME@$_TARGET_IP
```


