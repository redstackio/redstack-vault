---
id: 7a24e357-bd09-4904-ad7f-972bc2b77b85
name: Start a Windows Service
type: command
executor: command_prompt
data: sc.exe start $_SERVICE_NAME
output: "C:\\Windows\\system32>sc.exe start pwnSVC\n\nSERVICE_NAME: pwnSVC\n     \
  \   TYPE               : 30  WIN32\n        STATE              : 2  START_PENDING\n\
  \                                (NOT_STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)\n\
  \        WIN32_EXIT_CODE    : 0  (0x0)\n        SERVICE_EXIT_CODE  : 0  (0x0)\n\
  \        CHECKPOINT         : 0x0\n        WAIT_HINT          : 0x7d0\n        PID\
  \                : 1884\n        FLAGS              :"
created_at: '2020-04-28T21:10:21.094874+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Start a Windows Service

```command_prompt
sc.exe start $_SERVICE_NAME
```

## Expected Output

```
C:\Windows\system32>sc.exe start pwnSVC

SERVICE_NAME: pwnSVC
        TYPE               : 30  WIN32
        STATE              : 2  START_PENDING
                                (NOT_STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x7d0
        PID                : 1884
        FLAGS              :
```


