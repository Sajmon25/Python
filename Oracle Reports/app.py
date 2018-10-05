# with open('XX_CEWYBAKK.rdf', 'rb') as f:
# #     print(f.readline())
# # #s.find('XX_CE_KOLEJKA_KURSOWA1_PKG')
# #
# # print('It\'s  work')
#     for line in f:
#         #print(line)
#         if (line.find('XX_CE_KOLEJKA_KURSOWA1_PKG') != -1):
#             print(line)


import os, re, subprocess


text_file = open("Output.txt", "w")
#folderList = os.listdir('/ORACLE/appl/fs1/EBSapps/appl/')
folderList = os.listdir('/ORACLE/appl/fs1/EBSapps/appl/')
folderList.sort()
#folderList = ['ar', 'ap']

try:
    for d in folderList:
        #print(d + '\n')
        #text_file.write(d + '\n')
        try:
            fileList = os.listdir("/ORACLE/appl/fs1/EBSapps/appl/" + str(d) + "/12.0.0/reports/PL/")
            #fileList = os.listdir('/ORACLE/appl/fs1/EBSapps/appl/ar/12.0.0/reports/PL')
            #print('Valid path: ' + fileList)
            for f in fileList:
                if re.match('^(XX)|(XC)', f):
                    #print(f)
                    isValid = False
                    report_lines = ""
                    #bashCommand = "/ORACLE/apps/apps_st/appl/fnd/12.0.0/bin/gscc.pl -f " + "/ORACLE/apps/apps_st/appl/" + str(d) + "/12.0.0/reports/PL/" + str(f)
                    #bashCommand = "/ORACLE/apps/apps_st/appl/fnd/12.0.0/bin/gscc.pl -f " + "/ORACLE/apps/apps_st/appl/ar/12.0.0/reports/PL/" + str(f)
                    #process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
                    #output, error = process.communicate()
                    #os.rename("gscc-out.log", "gscc-out_" + f + ".log")
                    with open('/ORACLE/appl/fs1/EBSapps/appl/' + str(d) + '/12.0.0/reports/PL/' + str(f), 'rb') as testFile:
                        for line in testFile:
                            if (line.lower().find('CE.XX_CE_KOLEJKA_KURSOWA1_PKG'.lower()) != -1):
                            #if (line.lower().find('ARPT_SQL_FUNC_UTIL'.lower()) != -1):
                                 #print(line)
                                 report_lines += line
                                 isValid = True
                    if isValid:
                        print(f)
                        print(report_lines)

        except Exception as e:
            print(e)


except Exception as e:
    #text_file.write('Error: ' + d + '\n')
    text_file.write(str(e) + '\n')
    #print('Error: ' + d)
    print(e)
