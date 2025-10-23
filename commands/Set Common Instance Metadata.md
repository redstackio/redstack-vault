---
id: 5d29e976-bddb-45f0-bd9f-b16e9f4fddae
name: Set Common Instance Metadata
type: command
executor: bash
data: "curl -X POST \"https://www.googleapis.com/compute/v1/projects/1042377752888/setCommonInstanceMetadata\"\
  \ \n-H \"Authorization: Bearer ya29.c.EmKeBq9XI09_1HK1XXXXXXXXT0rJSA\" \n-H \"Content-Type:\
  \ application/json\" \n--data '{\"items\": [{\"key\": \"sshkeyname\", \"value\"\
  : \"sshkeyvalue\"}]}'"
output: null
created_at: '2023-04-06T03:56:38.401394+00:00'
updated_at: '2023-04-10T20:24:15.130562+00:00'
---

# Set Common Instance Metadata

```bash
curl -X POST "https://www.googleapis.com/compute/v1/projects/1042377752888/setCommonInstanceMetadata" 
-H "Authorization: Bearer ya29.c.EmKeBq9XI09_1HK1XXXXXXXXT0rJSA" 
-H "Content-Type: application/json" 
--data '{"items": [{"key": "sshkeyname", "value": "sshkeyvalue"}]}'
```


