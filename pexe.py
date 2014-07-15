import urllib
import ctypes
import os
#import platform
import sys
import socket

def get_free_space_mb(folder):
#    if plattform.system() == 'Windows':
    if True:
        free_bytes = ctypes.c_ulonglong(0)
	total_bytes = ctypes.c_ulonglong(0)
	ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, ctypes.pointer(total_bytes), ctypes.pointer(free_bytes))
	return {'free':free_bytes.value / 1024 / 1024, 'total': total_bytes.value / 1024 / 1024}
    else:
        st = os.statvfs(folder)
	return {'free':st.f_bavail * st.frsize / 1024 / 1024, 'total': 0}
host = socket.gethostname()
disk_p = get_free_space_mb("c:")
free_disk = disk_p["free"]
total_disk = disk_p["total"]
#print(host)
print(total_disk)
print(free_disk)
#quit();
params = urllib.urlencode({'hostname': host,'total_disk':total_disk,'free_disk':free_disk})
url = "http://10.0.2.2/f/htdocs/JORGE_CARDONA/pexe/report_disk_status.php?%s" % params
print(url)
f = urllib.urlopen(url);
print(f.read())
