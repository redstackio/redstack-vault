---
id: 0155d266-ec39-48c1-a6ab-3b3f6c3db8bf
name: xmllint Beautify XML
type: command
executor: bash
data: xmllint --format - < $_FILE.xml
output: "root@kali:~# xmllint --format - < rules.xml \n<?xml version=\"1.0\"?>\n<AppLockerPolicy\
  \ Version=\"1\">\n  <RuleCollection Type=\"Appx\" EnforcementMode=\"NotConfigured\"\
  />\n  <RuleCollection Type=\"Dll\" EnforcementMode=\"NotConfigured\"/>\n  <RuleCollection\
  \ Type=\"Exe\" EnforcementMode=\"Enabled\">\n    <FilePathRule Id=\"921cc481-6e17-4653-8f75-050b80acca20\"\
  \ Name=\"(Default Rule) All files located in the Program Files folder\" Description=\"\
  Allows members of the Everyone group to run applications that are located in the\
  \ Program Files folder.\" UserOrGroupSid=\"S-1-1-0\" Action=\"Allow\">\n      <Conditions>\n\
  ..."
created_at: '2020-03-04T05:01:54.789273+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# xmllint Beautify XML

```bash
xmllint --format - < $_FILE.xml
```

## Expected Output

```
root@kali:~# xmllint --format - < rules.xml 
<?xml version="1.0"?>
<AppLockerPolicy Version="1">
  <RuleCollection Type="Appx" EnforcementMode="NotConfigured"/>
  <RuleCollection Type="Dll" EnforcementMode="NotConfigured"/>
  <RuleCollection Type="Exe" EnforcementMode="Enabled">
    <FilePathRule Id="921cc481-6e17-4653-8f75-050b80acca20" Name="(Default Rule) All files located in the Program Files folder" Description="Allows members of the Everyone group to run applications that are located in the Program Files folder." UserOrGroupSid="S-1-1-0" Action="Allow">
      <Conditions>
...
```
