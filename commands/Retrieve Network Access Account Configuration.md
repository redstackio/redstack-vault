---
id: 04afa157-847f-4b7c-8c8a-d51fc2fdf369
name: Retrieve Network Access Account Configuration
type: command
executor: bash
data: 'Get-Wmiobject -namespace \"root\ccm\policy\Machine\ActualConfig\" -class \"CCM_NetworkAccessAccount\"\nNetworkAccessPassword
  : <![CDATA[E600000001...8C6B5]]>\nNetworkAccessUsername : <![CDATA[E600000001...00F92]]>'
output: null
created_at: '2023-04-06T03:56:08.224149+00:00'
updated_at: '2023-04-10T20:26:02.204187+00:00'
---

# Retrieve Network Access Account Configuration

```bash
Get-Wmiobject -namespace \"root\ccm\policy\Machine\ActualConfig\" -class \"CCM_NetworkAccessAccount\"\nNetworkAccessPassword : <![CDATA[E600000001...8C6B5]]>\nNetworkAccessUsername : <![CDATA[E600000001...00F92]]>
```


