---
id: 0155d266-ec39-48c1-a6ab-3b3f6c3db8bf
type: command
executor: bash
data: xmllint --format - < $_FILE.xml
output: |-
  root@kali:~# xmllint --format - < rules.xml 
  <?xml version="1.0"?>
  <AppLockerPolicy Version="1">
    <RuleCollection Type="Appx" EnforcementMode="NotConfigured"/>
    <RuleCollection Type="Dll" EnforcementMode="NotConfigured"/>
    <RuleCollection Type="Exe" EnforcementMode="Enabled">
      <FilePathRule Id="921cc481-6e17-4653-8f75-050b80acca20" Name="(Default Rule) All files located in the Program Files folder" Description="Allows members of the Everyone group to run applications that are located in the Program Files folder." UserOrGroupSid="S-1-1-0" Action="Allow">
        <Conditions>
  ...
created_at: '2020-03-04T05:01:54.789273+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - xml
  - formatting
  - utility
verified: true
validated: true
---

# xmllint-format-xml-file

## Command

```bash
xmllint --format - < $_FILE.xml
```

## Description

This command uses xmllint to format and pretty-print XML input from a specified file, adding indentation and line breaks for improved readability. It is particularly useful in security analysis for processing exported XML policies, such as AppLocker configurations, on Linux systems to facilitate manual review of rules and structures.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--format` | Pretty-prints the input XML with proper indentation and line breaks | Yes |
| `-` | Reads input from stdin | Built-in |
| `< $_FILE.xml` | Redirects the content of the specified XML file to stdin; replace $_FILE.xml with the path to the actual XML file (e.g., rules.xml) | Yes |

## Examples

### Basic Usage

```bash
xmllint --format - < applocker.xml
```

### Advanced Usage

Redirect output to a new file for further processing:

```bash
xmllint --format - < applocker.xml > formatted_applocker.xml
```

## Expected Output

The command produces indented and structured XML output, making nested elements easier to parse. For example, processing a sample AppLocker policy file:

```
root@kali:~# xmllint --format - < rules.xml 
<?xml version="1.0"?>
<AppLockerPolicy Version="1">
  <RuleCollection Type="Appx" EnforcementMode="NotConfigured"/>
  <RuleCollection Type="Dll" EnforcementMode="NotConfigured"/>
  <RuleCollection Type="Exe" EnforcementMode="Enabled">
    <FilePathRule Id="921cc481-6e17-4653-8f75-050b80acca20" Name="(Default Rule) All files located in the Program Files folder" Description="Allows members of the Everyone group to run applications that are located in the Program Files folder." UserOrGroupSid="S-1-1-0" Action="Allow">
      <Conditions>
        <FilePathCondition Path="%PROGRAMFILES%\*" />
      </Conditions>
    </FilePathRule>
    <!-- Additional rules follow with proper indentation -->
  </RuleCollection>
</AppLockerPolicy>
```

Success is indicated by cleanly formatted XML without parsing errors. If the input XML is malformed, xmllint will output error messages instead.

## Related

- [[tools/xmllint]]
