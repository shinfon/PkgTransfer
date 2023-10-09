# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

# =============================================================================
# import sys 
# 
# SYSARG = sys.argv
# 
# print(SYSARG)
# =============================================================================

import json as js
import sys,os
import ftplib

SER_DIS = "10.14.32.84"
FILE_NAME = "root"
SERVER_ACC = "root"
SERVER_PW = "rootroot"
FILE_PATH = "/home/QCT/john/Temporary"
FILE_NAME = "PRANK.json"


JS_STR = """
{
    "PRANK_SPEC": [
        {
            "Mouse_click_sw": "off",
            "Mouse_move_sw": "off",
            "Kb_switcher": "off",
            "Kb_action_switcher": "off",
            "Sys_ctrl": "off",
            "Mouse_intervals": "20",
            "Kb_string": "WARNING: Core 11601 (hw element id 240) is defective: Non qualified device",
            "Keycode": "alt+tab",
            "Syscode": "rundll32.exe user32.dll,LockWorkStation",
            "Mouse_offsetX": "2000",
            "Mouse_offsetY": "-2000",
            "Mouse_ky": "0", 
            "Mouse_click_qty": "2",
            "Timeout": "3600",
            "Account": "chaoshunxu"
        }
    ]
}
"""
#rundll32.exe user32.dll,LockWorkStation
#logoff

#chaoshunxu
#jhongfuchen
#kuanyuchen

with open(FILE_NAME,'w',encoding="utf-8") as f1:
        datas = js.loads(JS_STR)
        js.dump(datas,f1,ensure_ascii=False)
        

Local_file = open(FILE_NAME,'rb')
ftp = ftplib.FTP(SER_DIS)
ftp.login(SERVER_ACC,SERVER_PW)
ftp.cwd(FILE_PATH)
ftp.storbinary('STOR ' + FILE_NAME,Local_file,1024)
Local_file.close()
ftp.quit()
os.remove(FILE_NAME)



# =============================================================================
# for data in datas:
#     print(data['Mouse_switcher'])
# =============================================================================






