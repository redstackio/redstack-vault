---
id: 2cdfce5b-082d-4a87-b595-73803fa6c575
name: Retrieve the msds-allowedtoactonbehalfofotheridentity attribute of the dc01-ww2.factory.lan
  computer object
type: command
executor: bash
data: '$RawBytes = Get-DomainComputer dc01-ww2.factory.lan -Properties ''msds-allowedtoactonbehalfofotheridentity''
  | select -expand msds-allowedtoactonbehalfofotheridentity

  $Descriptor = New-Object Security.AccessControl.RawSecurityDescriptor -ArgumentList
  $RawBytes, 0

  $Descriptor.DiscretionaryAcl'
output: null
created_at: '2023-04-06T03:56:07.771308+00:00'
updated_at: '2023-04-06T03:56:07.808204+00:00'
---

# Retrieve the msds-allowedtoactonbehalfofotheridentity attribute of the dc01-ww2.factory.lan computer object

```bash
$RawBytes = Get-DomainComputer dc01-ww2.factory.lan -Properties 'msds-allowedtoactonbehalfofotheridentity' | select -expand msds-allowedtoactonbehalfofotheridentity
$Descriptor = New-Object Security.AccessControl.RawSecurityDescriptor -ArgumentList $RawBytes, 0
$Descriptor.DiscretionaryAcl
```
