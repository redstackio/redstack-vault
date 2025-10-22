---
id: 7f73c376-69bc-4083-af22-38c729e74604
name: Autostart Welcome application
type: command
executor: bash
data: 'In : ~/.config/autostart/*.desktop

  [Desktop Entry]

  Type=Application

  Name=Welcome

  Exec=/var/lib/gnome-welcome-tour

  AutostartCondition=unless-exists ~/.cache/gnome-getting-started-docs/seen-getting-started-guide

  OnlyShowIn=GNOME;

  X-GNOME-Autostart-enabled=false'
output: null
created_at: '2023-04-06T03:56:18.065245+00:00'
updated_at: '2023-04-10T20:34:18.935764+00:00'
---

# Autostart Welcome application

```bash
In : ~/.config/autostart/*.desktop

[Desktop Entry]
Type=Application
Name=Welcome
Exec=/var/lib/gnome-welcome-tour
AutostartCondition=unless-exists ~/.cache/gnome-getting-started-docs/seen-getting-started-guide
OnlyShowIn=GNOME;
X-GNOME-Autostart-enabled=false
```
