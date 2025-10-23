---
id: e3533930-3612-4f56-8691-ee156810c082
name: Add USB device to udev rules
type: command
executor: bash
data: echo "ACTION==\\\"add\\\",ENV{DEVTYPE}==\\\"usb_device\\\",SUBSYSTEM==\\\"usb\\\",RUN+=\\\"$RSHELL\\\""
  | tee /etc/udev/rules.d/71-vbox-kernel-drivers.rules > /dev/null
output: null
created_at: '2023-04-06T03:56:18.093000+00:00'
updated_at: '2023-04-10T20:34:18.258394+00:00'
---

# Add USB device to udev rules

```bash
echo "ACTION==\\\"add\\\",ENV{DEVTYPE}==\\\"usb_device\\\",SUBSYSTEM==\\\"usb\\\",RUN+=\\\"$RSHELL\\\"" | tee /etc/udev/rules.d/71-vbox-kernel-drivers.rules > /dev/null
```


