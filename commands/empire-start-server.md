---
type: command
executor: bash
data: powershell-empire
output: >-
  root@kali:~#
  powershell-empire                                                                                                                     
  [1028/1277]
                                                                                                                                                                           
   [>] Enter server negotiation password, enter for random generation:                                                                                                     
                                                                                                                                                                           
   [*] Database setup completed!                                                                                                                                           
                                                                                                                                                                           
  [*] Loading stagers from:
  /usr/share/powershell-empire//lib/stagers/                                                                                                     

  [*] Loading modules from:
  /usr/share/powershell-empire//lib/modules/                                                                                                     

  [*] Loading listeners from:
  /usr/share/powershell-empire//lib/listeners/                                                                                                 

  [*] Empire starting
  up...                                                                                                                                                
                                                                                                                                                                           
                                `````````                                                                                                                                  
                           ``````.--::///+                                                                                                                                 
                       ````-+sydmmmNNNNNNN                                                                                                                                 
                     ``./ymmNNNNNNNNNNNNNN                                                                                                                                 
                   ``-ymmNNNNNNNNNNNNNNNNN                                                                                                                                 
                 ```ommmmNNNNNNNNNNNNNNNNN                                                                                                                                 
                ``.ydmNNNNNNNNNNNNNNNNNNNN                                                                                                                                 
               ```odmmNNNNNNNNNNNNNNNNNNNN                                                                                                                                 
              ```/hmmmNNNNNNNNNNNNNNNNMNNN                                                                                                                                 
             ````+hmmmNNNNNNNNNNNNNNNNNMMN                                                                                                                                 
            ````..ymmmNNNNNNNNNNNNNNNNNNNN                                                                                                                                 
            ````:.+so+//:---.......----::-                                                                                                                                 
           `````.`````````....----:///++++                                                                                                                                 
          ``````.-/osy+////:::---...-dNNNN                                                                                                                                 
          ````:sdyyydy`         ```:mNNNNM                                                                                                                                 
         ````-hmmdhdmm:`      ``.+hNNNNNNM                                                                                                                                 
         ```.odNNmdmmNNo````.:+yNNNNNNNNNN                                                                                                                                 
         ```-sNNNmdh/dNNhhdNNNNNNNNNNNNNNN                                                                                                                                 
         ```-hNNNmNo::mNNNNNNNNNNNNNNNNNNN                                                                                                                                 
         ```-hNNmdNo--/dNNNNNNNNNNNNNNNNNN                                                                                                                                 
        ````:dNmmdmd-:+NNNNNNNNNNNNNNNNNNm                                                                                                                                 
        ```/hNNmmddmd+mNNNNNNNNNNNNNNds++o                                                                                                                                 
       ``/dNNNNNmmmmmmmNNNNNNNNNNNmdoosydd                                                                                                                                 
       `sNNNNdyydNNNNmmmmmmNNNNNmyoymNNNNN                                                                                                                                 
       :NNmmmdso++dNNNNmmNNNNNdhymNNNNNNNN                                                                                                                                 
       -NmdmmNNdsyohNNNNmmNNNNNNNNNNNNNNNN                                                                                                                                 
       `sdhmmNNNNdyhdNNNNNNNNNNNNNNNNNNNNN                                                                                                                                 
         /yhmNNmmNNNNNNNNNNNNNNNNNNNNNNmhh                                                                                                                                 
          `+yhmmNNNNNNNNNNNNNNNNNNNNNNmh+:                                                                                                                                 
            `./dmmmmNNNNNNNNNNNNNNNNmmd.                                                                                                                                   
              `ommmmmNNNNNNNmNmNNNNmmd:                                                                                                                                    
               :dmmmmNNNNNmh../oyhhhy:                                                                                                                                     
               `sdmmmmNNNmmh/++-.+oh.                                                                                                                                      
                `/dmmmmmmmmdo-:/ossd:                                                                                                                                      
                  `/ohhdmmmmmmdddddmh/                                                                                                                                     
                     `-/osyhdddddhyo:                                                                                                                                      
                          ``.----.`                                                                                                                                        
                                                                                                                                                                           
                  Welcome to the Empire                                                                                                                                    
  ================================================================================                                                                                         
   [Empire]  Post-Exploitation Framework                                                                                                                                   
  ================================================================================                                                                                         
   [Version] 3.0.7 BC-Security Fork | [Web] https://github.com/BC-SECURITY/Empire                                                                                          
  ================================================================================                                                                                         
                                                                                                                                                                           
     _______ .___  ___. .______    __  .______       _______                                                                                                               
    |   ____||   \/   | |   _  \  |  | |   _  \     |   ____|                                                                                                              
    |  |__   |  \  /  | |  |_)  | |  | |  |_)  |    |  |__                                                                                                                 
    |   __|  |  |\/|  | |   ___/  |  | |      /     |   __|                                                                                                                
    |  |____ |  |  |  | |  |      |  | |  |\  \----.|  |____                                                                                                               
    |_______||__|  |__| | _|      |__| | _| `._____||_______|                                                                                                              
                                                                                                                                                                           
                                                                                                                                                                           
         298 modules currently loaded                                                                                                                                      
                                                                                                                                                                           
         0 listeners currently active                                                                                                                                      
                                                                                                                                                                           
         0 agents currently active 
  ...
tags:
  - c2
  - startup
platforms:
  - Linux
created_at: '2020-03-23T20:14:14.662488+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
verified: true
validated: true
---

# empire-start-server

## Command

```bash
powershell-empire
```

## Description

This command launches the Empire C2 server, initializing the framework for post-exploitation operations. It loads all stagers, modules, and listeners from the installation directory and starts the interactive console. Use this as the entry point for managing agents, generating payloads, and executing tasks on compromised systems. Ideal for red team setups where a persistent C2 infrastructure is needed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | This command has no parameters; it uses default configuration from the Empire installation | No |

## Examples

### Basic Usage

```bash
powershell-empire
```

This starts the server and prompts for a negotiation password. Press Enter to generate a random one.

### Advanced Usage

To start with a custom profile directory:

```bash
powershell-empire --profile /path/to/custom/profile
```

Or enable the REST API:

```bash
powershell-empire --rest
```

## Expected Output

Upon successful execution, the command displays a loading sequence, including database setup, module loading (e.g., 298 modules), and the Empire ASCII art banner. It then enters the interactive prompt with details on active listeners and agents (initially 0). Example excerpt:

```
[*] Database setup completed!
[*] Loading stagers from: /usr/share/powershell-empire/lib/stagers/
[*] Loading modules from: /usr/share/powershell-empire/lib/modules/
[*] Loading listeners from: /usr/share/powershell-empire/lib/listeners/
[*] Empire starting up...

[ASCII Art Banner]

Welcome to the Empire
[Empire] Post-Exploitation Framework
[Version] 3.0.7 BC-Security Fork | [Web] https://github.com/BC-SECURITY/Empire

298 modules currently loaded
0 listeners currently active
0 agents currently active

(Empire) >
```

Success is indicated by reaching the `(Empire) >` prompt without errors.

## Related

- [[tools/Empire]] (parent tool documentation)
- [[Related Procedure]] (e.g., procedures using Empire for agent deployment)
