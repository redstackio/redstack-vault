---
id: 3ed431fc-a202-4d8c-8114-09b9f2c28a65
name: Compile malicious dll
type: command
executor: bash
data: '# compile a malicious dll

  - For x64 compile with: "x86_64-w64-mingw32-gcc windows_dll.c -shared -o output.dll"

  - For x86 compile with: "i686-w64-mingw32-gcc windows_dll.c -shared -o output.dll"'
output: null
created_at: '2023-04-06T03:56:29.436687+00:00'
updated_at: '2023-04-10T20:37:36.999118+00:00'
---

# Compile malicious dll

```bash
# compile a malicious dll
- For x64 compile with: "x86_64-w64-mingw32-gcc windows_dll.c -shared -o output.dll"
- For x86 compile with: "i686-w64-mingw32-gcc windows_dll.c -shared -o output.dll"
```
