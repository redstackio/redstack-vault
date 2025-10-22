---
id: 1f18633a-25ff-4d4a-a5a7-009b213c60b9
name: Get-Process List Running Processes
type: command
executor: powershell
data: Get-Process
output: "PS C:\\> Get-Process\n\nHandles  NPM(K)    PM(K)      WS(K)     CPU(s)  \
  \   Id  SI ProcessName\n-------  ------    -----      -----     ------     --  --\
  \ -----------\n    257      16     5308      21980       0.95   6964   1 ApplicationFrameHost\n\
  \     76       5     2520       3916       0.03   6500   1 cmd\n    262      13\
  \     7532      16960       1.06   3404   1 conhost\n    617      22     1768  \
  \     4816               440   0 csrss\n    566      16     1852       5020    \
  \           524   1 csrss\n    481      41    40012     106832       1.73   1724\
  \   1 firefox"
created_at: '2020-01-02T18:45:14.101739+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Get-Process List Running Processes

```powershell
Get-Process
```

## Expected Output

```
PS C:\> Get-Process

Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
    257      16     5308      21980       0.95   6964   1 ApplicationFrameHost
     76       5     2520       3916       0.03   6500   1 cmd
    262      13     7532      16960       1.06   3404   1 conhost
    617      22     1768       4816               440   0 csrss
    566      16     1852       5020               524   1 csrss
    481      41    40012     106832       1.73   1724   1 firefox
```
