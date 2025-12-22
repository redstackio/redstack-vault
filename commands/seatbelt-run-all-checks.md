---
type: command
executor: command_prompt
data: Seatbelt.exe all
output: >-
  PS C:\Users\public\Downloads> .\SeatBelt.exe all


                          %&&@@@&&
                          &&&&&&&%%%,                       #&&@@@@@@%%%%%%###############%
                          &%&   %&%%                        &////(((&%%%%%#%################//((((###%%%%%%%%%%%%%%%
  %%%%%%%%%%%######%%%#%%####%  &%%**#                     
  @////(((&%%%%%%######################(((((((((((((((((((

  #%#%%%%%%%#######%#%%#######  %&%,,,,,,,,,,,,,,,,        
  @////(((&%%%%%#%#####################(((((((((((((((((((

  #%#%%%%%%#####%%#%#%%#######  %%%,,,,,,  ,,.   ,,        
  @////(((&%%%%%%%######################(#(((#(#((((((((((

  #####%%%####################  &%%......  ...   ..        
  @////(((&%%%%%%%###############%######((#(#(####((((((((

  #######%##########%#########  %%%......  ...   ..        
  @////(((&%%%%%#########################(#(#######((#####

  ###%##%%####################  &%%...............         
  @////(((&%%%%%%%%##############%#######(#########((#####

  #####%######################  %%%..                      
  @////(((&%%%%%%%################
                          &%&   %%%%%      Seatbelt         %////(((&%%%%%%%%#############*
                          &%%&&&%%%%%        v0.2.0         ,(((&%%%%%%%%%%%%%%%%%,
                           #%%%%##,



  === Running System Triage Checks ===
platforms:
  - Windows
tags:
  - Enumeration
  - Discovery
verified: true
validated: true
---

# seatbelt-run-all-checks

## Command

```command_prompt
Seatbelt.exe all
```

## Description

This command executes SeatBelt with the 'all' argument to perform a comprehensive enumeration of the local Windows system, running checks across all available categories such as accounts, services, network configurations, and potential privilege escalation paths. It is ideal for initial post-exploitation reconnaissance to gather a broad overview of system security posture.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `all` | Runs all predefined enumeration checks (no additional arguments needed) | Yes |

## Examples

### Basic Usage

Execute on a target Windows system:

```command_prompt
Seatbelt.exe all
```

### Advanced Usage

Redirect output to a file for later analysis:

```command_prompt
Seatbelt.exe all > seatbelt_output.txt
```

## Expected Output

The command produces ASCII art branding followed by categorized output starting with system triage checks. Successful execution begins with:

```
PS C:\Users\public\Downloads> .\SeatBelt.exe all


                        %&&@@@&&
                        &&&&&&&%%%,                       #&&@@@@@@%%%%%%###############%
                        &%&   %&%%                        &////(((&%%%%%#%################//((((###%%%%%%%%%%%%%%%
%%%%%%%%%%%######%%%#%%####%  &%%**#                      @////(((&%%%%%%######################(((((((((((((((((((
#%#%%%%%%%#######%#%%#######  %&%,,,,,,,,,,,,,,,,         @////(((&%%%%%#%#####################(((((((((((((((((((
#%#%%%%%%#####%%#%#%%#######  %%%,,,,,,  ,,.   ,,         @////(((&%%%%%%%######################(#(((#(#((((((((((
#####%%%####################  &%%......  ...   ..         @////(((&%%%%%%%###############%######((#(#(####((((((((
#######%##########%#########  %%%......  ...   ..         @////(((&%%%%%#########################(#(#######((#####
###%##%%####################  &%%...............          @////(((&%%%%%%%%##############%#######(#########((#####
#####%######################  %%%..                       @////(((&%%%%%%%################
                        &%&   %%%%%      Seatbelt         %////(((&%%%%%%%%#############*
                        &%%&&&%%%%%        v0.2.0         ,(((&%%%%%%%%%%%%%%%%%,
                         #%%%%##,



=== Running System Triage Checks ===
```

Subsequent output includes detailed findings per category, such as user accounts, installed hotfixes, and vulnerable services. Look for highlighted risks like unquoted service paths or weak ACLs.

## Related

- [[commands/seatbelt-run-specific-category]]
- [[procedures/Windows-Local-Enumeration-for-Privesc]]
