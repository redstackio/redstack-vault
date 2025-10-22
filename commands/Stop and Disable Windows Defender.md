---
id: fbec91e7-c5c9-4870-824d-e052fd2b9ce1
name: Stop and Disable Windows Defender
type: command
executor: command_prompt
data: 'sc config WinDefend start= disabled

  sc stop WinDefend'
output: "C:\\>sc config WinDefend start= disabled\n[SC] ChangeServiceConfig SUCCESS\n\
  \nC:\\>sc stop WinDefend\n\nSERVICE_NAME: WinDefend\n        TYPE              \
  \ : 20  WIN32_SHARE_PROCESS\n        STATE              : 4  RUNNING\n         \
  \                       (STOPPABLE, NOT_PAUSABLE, ACCEPTS_SHUTDOWN)\n        WIN32_EXIT_CODE\
  \    : 0  (0x0)\n        SERVICE_EXIT_CODE  : 0  (0x0)\n        CHECKPOINT     \
  \    : 0x0\n        WAIT_HINT          : 0x0"
created_at: '2020-01-28T21:19:38.379370+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Stop and Disable Windows Defender

```command_prompt
sc config WinDefend start= disabled
sc stop WinDefend
```

## Expected Output

```
C:\>sc config WinDefend start= disabled
[SC] ChangeServiceConfig SUCCESS

C:\>sc stop WinDefend

SERVICE_NAME: WinDefend
        TYPE               : 20  WIN32_SHARE_PROCESS
        STATE              : 4  RUNNING
                                (STOPPABLE, NOT_PAUSABLE, ACCEPTS_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x0
```
