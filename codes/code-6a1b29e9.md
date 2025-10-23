---
id: 6a1b29e9-d590-4da6-8ebb-8a2bfa59ecd4
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:26.491119+00:00'
updated_at: '2023-04-10T20:37:04.081265+00:00'
---

# Code Snippet 6a1b29e9

**Language**: ps1

```ps1
rundll32 PowerShdll,main <script>
rundll32 PowerShdll,main -h      Display this message
rundll32 PowerShdll,main -f <path>       Run the script passed as argument
rundll32 PowerShdll,main -w      Start an interactive console in a new window (Default)
rundll32 PowerShdll,main -i      Start an interactive console in this console

rundll32 PowerShx.dll,main -e                           <PS script to run>
rundll32 PowerShx.dll,main -f <path>                    Run the script passed as argument
rundll32 PowerShx.dll,main -f <path> -c <PS Cmdlet>     Load a script and run a PS cmdlet
rundll32 PowerShx.dll,main -w                           Start an interactive console in a new window
rundll32 PowerShx.dll,main -i                           Start an interactive console
rundll32 PowerShx.dll,main -s                           Attempt to bypass AMSI
rundll32 PowerShx.dll,main -v                           Print Execution Output to the console
```


