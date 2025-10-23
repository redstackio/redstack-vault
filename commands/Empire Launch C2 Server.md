---
id: c7076387-2b2c-49df-8513-18c33b6c64b3
name: Empire Launch C2 Server
type: command
executor: bash
data: powershell-empire
output: "root@kali:~# powershell-empire                                          \
  \                                                                            [1028/1277]\n\
  \                                                                              \
  \                                                                              \
  \             \n [>] Enter server negotiation password, enter for random generation:\
  \                                                                              \
  \                       \n                                                     \
  \                                                                              \
  \                                      \n [*] Database setup completed!        \
  \                                                                              \
  \                                                     \n                       \
  \                                                                              \
  \                                                                    \n[*] Loading\
  \ stagers from: /usr/share/powershell-empire//lib/stagers/                     \
  \                                                                              \
  \  \n[*] Loading modules from: /usr/share/powershell-empire//lib/modules/      \
  \                                                                              \
  \                 \n[*] Loading listeners from: /usr/share/powershell-empire//lib/listeners/\
  \                                                                              \
  \                   \n[*] Empire starting up...                                \
  \                                                                              \
  \                                  \n                                          \
  \                                                                              \
  \                                                 \n                           \
  \   `````````                                                                  \
  \                                                                \n            \
  \             ``````.--::///+                                                  \
  \                                                                              \
  \ \n                     ````-+sydmmmNNNNNNN                                   \
  \                                                                              \
  \                \n                   ``./ymmNNNNNNNNNNNNNN                    \
  \                                                                              \
  \                               \n                 ``-ymmNNNNNNNNNNNNNNNNN     \
  \                                                                              \
  \                                              \n               ```ommmmNNNNNNNNNNNNNNNNN\
  \                                                                              \
  \                                                   \n              ``.ydmNNNNNNNNNNNNNNNNNNNN\
  \                                                                              \
  \                                                   \n             ```odmmNNNNNNNNNNNNNNNNNNNN\
  \                                                                              \
  \                                                   \n            ```/hmmmNNNNNNNNNNNNNNNNMNNN\
  \                                                                              \
  \                                                   \n           ````+hmmmNNNNNNNNNNNNNNNNNMMN\
  \                                                                              \
  \                                                   \n          ````..ymmmNNNNNNNNNNNNNNNNNNNN\
  \                                                                              \
  \                                                   \n          ````:.+so+//:---.......----::-\
  \                                                                              \
  \                                                   \n         `````.`````````....----:///++++\
  \                                                                              \
  \                                                   \n        ``````.-/osy+////:::---...-dNNNN\
  \                                                                              \
  \                                                   \n        ````:sdyyydy`    \
  \     ```:mNNNNM                                                               \
  \                                                                  \n       ````-hmmdhdmm:`\
  \      ``.+hNNNNNNM                                                            \
  \                                                                     \n       ```.odNNmdmmNNo````.:+yNNNNNNNNNN\
  \                                                                              \
  \                                                   \n       ```-sNNNmdh/dNNhhdNNNNNNNNNNNNNNN\
  \                                                                              \
  \                                                   \n       ```-hNNNmNo::mNNNNNNNNNNNNNNNNNNN\
  \                                                                              \
  \                                                   \n       ```-hNNmdNo--/dNNNNNNNNNNNNNNNNNN\
  \                                                                              \
  \                                                   \n      ````:dNmmdmd-:+NNNNNNNNNNNNNNNNNNm\
  \                                                                              \
  \                                                   \n      ```/hNNmmddmd+mNNNNNNNNNNNNNNds++o\
  \                                                                              \
  \                                                   \n     ``/dNNNNNmmmmmmmNNNNNNNNNNNmdoosydd\
  \                                                                              \
  \                                                   \n     `sNNNNdyydNNNNmmmmmmNNNNNmyoymNNNNN\
  \                                                                              \
  \                                                   \n     :NNmmmdso++dNNNNmmNNNNNdhymNNNNNNNN\
  \                                                                              \
  \                                                   \n     -NmdmmNNdsyohNNNNmmNNNNNNNNNNNNNNNN\
  \                                                                              \
  \                                                   \n     `sdhmmNNNNdyhdNNNNNNNNNNNNNNNNNNNNN\
  \                                                                              \
  \                                                   \n       /yhmNNmmNNNNNNNNNNNNNNNNNNNNNNmhh\
  \                                                                              \
  \                                                   \n        `+yhmmNNNNNNNNNNNNNNNNNNNNNNmh+:\
  \                                                                              \
  \                                                   \n          `./dmmmmNNNNNNNNNNNNNNNNmmd.\
  \                                                                              \
  \                                                     \n            `ommmmmNNNNNNNmNmNNNNmmd:\
  \                                                                              \
  \                                                      \n             :dmmmmNNNNNmh../oyhhhy:\
  \                                                                              \
  \                                                       \n             `sdmmmmNNNmmh/++-.+oh.\
  \                                                                              \
  \                                                        \n              `/dmmmmmmmmdo-:/ossd:\
  \                                                                              \
  \                                                        \n                `/ohhdmmmmmmdddddmh/\
  \                                                                              \
  \                                                       \n                   `-/osyhdddddhyo:\
  \                                                                              \
  \                                                        \n                    \
  \    ``.----.`                                                                 \
  \                                                                       \n     \
  \                                                                              \
  \                                                                              \
  \        \n                Welcome to the Empire                               \
  \                                                                              \
  \                       \n================================================================================\
  \                                                                              \
  \           \n [Empire]  Post-Exploitation Framework                           \
  \                                                                              \
  \                          \n================================================================================\
  \                                                                              \
  \           \n [Version] 3.0.7 BC-Security Fork | [Web] https://github.com/BC-SECURITY/Empire\
  \                                                                              \
  \            \n================================================================================\
  \                                                                              \
  \           \n                                                                 \
  \                                                                              \
  \                          \n   _______ .___  ___. .______    __  .______      \
  \ _______                                                                      \
  \                                         \n  |   ____||   \\/   | |   _  \\  |\
  \  | |   _  \\     |   ____|                                                   \
  \                                                           \n  |  |__   |  \\ \
  \ /  | |  |_)  | |  | |  |_)  |    |  |__                                      \
  \                                                                           \n \
  \ |   __|  |  |\\/|  | |   ___/  |  | |      /     |   __|                     \
  \                                                                              \
  \             \n  |  |____ |  |  |  | |  |      |  | |  |\\  \\----.|  |____   \
  \                                                                              \
  \                              \n  |_______||__|  |__| | _|      |__| | _| `._____||_______|\
  \                                                                              \
  \                                \n                                            \
  \                                                                              \
  \                                               \n                             \
  \                                                                              \
  \                                                              \n       298 modules\
  \ currently loaded                                                             \
  \                                                                         \n   \
  \                                                                              \
  \                                                                              \
  \          \n       0 listeners currently active                               \
  \                                                                              \
  \                         \n                                                   \
  \                                                                              \
  \                                        \n       0 agents currently active \n..."
created_at: '2020-03-23T20:14:14.662488+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Empire Launch C2 Server

```bash
powershell-empire
```

## Expected Output

```
root@kali:~# powershell-empire                                                                                                                      [1028/1277]
                                                                                                                                                                         
 [>] Enter server negotiation password, enter for random generation:                                                                                                     
                                                                                                                                                                         
 [*] Database setup completed!                                                                                                                                           
                                                                                                                                                                         
[*] Loading stagers from: /usr/share/powershell-empire//lib/stagers/                                                                                                     
[*] Loading modules from: /usr/share/powershell-empire//lib/modules/                                                                                                     
[*] Loading listeners from: /usr/share/powershell-empire//lib/listeners/                                                                                                 
[*] Empire starting up...                                                                                                                                                
                                                                                                                                                                         
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
```


