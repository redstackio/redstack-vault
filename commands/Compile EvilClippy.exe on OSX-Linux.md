---
id: 44ff2628-6a20-4969-bd26-f6432430bcf8
name: Compile EvilClippy.exe on OSX/Linux
type: command
executor: bash
data: mcs /reference:OpenMcdf.dll,System.IO.Compression.FileSystem.dll /out:EvilClippy.exe
  *.cs
output: null
created_at: '2023-04-06T03:56:23.824507+00:00'
updated_at: '2023-04-10T20:36:56.680981+00:00'
---

# Compile EvilClippy.exe on OSX/Linux

```bash
mcs /reference:OpenMcdf.dll,System.IO.Compression.FileSystem.dll /out:EvilClippy.exe *.cs
```
