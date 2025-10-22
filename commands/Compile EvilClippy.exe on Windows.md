---
id: 2fbe1779-fe1f-46fd-bd6e-a5ffadd26654
name: Compile EvilClippy.exe on Windows
type: command
executor: bash
data: csc /reference:OpenMcdf.dll,System.IO.Compression.FileSystem.dll /out:EvilClippy.exe
  *.cs
output: null
created_at: '2023-04-06T03:56:23.824566+00:00'
updated_at: '2023-04-10T20:36:56.680981+00:00'
---

# Compile EvilClippy.exe on Windows

```bash
csc /reference:OpenMcdf.dll,System.IO.Compression.FileSystem.dll /out:EvilClippy.exe *.cs
```
