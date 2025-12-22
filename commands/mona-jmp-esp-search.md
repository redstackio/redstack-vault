---
id: 1abf33ab-e658-4148-a552-f6a34a3582d3
type: command
executor: immunity
data: '!mona jmp -r esp'
output: >-
  [+] Command used:

  !mona jmp -r esp


  ---------- Mona command started on 2020-04-03 12:27:59 (v2.0, rev 583)
  ----------

  ...

  [+] Results :
    0x625011af : jmp esp |  {PAGE_EXECUTE_READ} [essfunc.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v-1.0- (C:\Users\Victim\Desktop\vulnserver-master\essfunc.dll)
  ...
created_at: '2019-09-21T00:36:54.550104+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - exploit-dev
  - buffer-overflow
verified: true
validated: true
---

# mona-jmp-esp-search

## Command

```immunity
!mona jmp -r esp
```

## Description

This command searches the loaded modules in the current Immunity Debugger process for 'jmp esp' instructions, which are commonly used in stack-based buffer overflow exploits to redirect execution to shellcode on the stack. It filters results to show only pointers in executable memory regions and provides details on module protections like ASLR and SafeSEH, helping identify reliable jump targets for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-r esp` | Register to jump to (esp for stack pointer redirection) | Yes |
| `-module <name>` | Limit search to a specific module | No |
| `-cpb` | Filter modules without certain protections (e.g., ASLR: False) | No |

## Examples

### Basic Usage

Search all modules for jmp esp:

```immunity
!mona jmp -r esp
```

### Advanced Usage

Search within a specific module without ASLR:

```immunity
!mona jmp -r esp -module essfunc.dll -cpb
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
[+] Command used:
!mona jmp -r esp

---------- Mona command started on 2020-04-03 12:27:59 (v2.0, rev 583) ----------
...
[+] Results :
  0x625011af : jmp esp |  {PAGE_EXECUTE_READ} [essfunc.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v-1.0- (C:\Users\Victim\Desktop\vulnserver-master\essfunc.dll)
...
```

## Related

- [[mona-pattern-create]]
- [[Related Procedure for Buffer Overflow Exploitation]]
