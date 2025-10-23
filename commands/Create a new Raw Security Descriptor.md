---
id: aa17ab91-99a7-4b73-ab93-c0d1c79fdcd1
name: Create a new Raw Security Descriptor
type: command
executor: bash
data: $SD = New-Object Security.AccessControl.RawSecurityDescriptor -ArgumentList
  "O:BAD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;$SID_FROM_PREVIOUS_COMMAND)"
output: null
created_at: '2023-04-06T03:56:07.771485+00:00'
updated_at: '2023-04-06T03:56:07.808387+00:00'
---

# Create a new Raw Security Descriptor

```bash
$SD = New-Object Security.AccessControl.RawSecurityDescriptor -ArgumentList "O:BAD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;$SID_FROM_PREVIOUS_COMMAND)"
```


