import random
import string
import subprocess
import sys
import tempfile
import urllib
import requests
import wmi
import os
import shutil
import time

def tmp_random():
    return tempfile.gettempdir() + '\\' + ''.join(random.choice(string.ascii_uppercase) for _ in range(8)) + '.exe'

def delete_self():
    current_file = r'C:\\Sistema\\temp\\atualiza1.exe'
    if os.path.exists(current_file):
        os.remove(current_file)
        sys.exit()

fileId = tempfile.gettempdir() + '\\' + ''.join(random.choice(string.ascii_uppercase) for _ in range(8)) + '.exe'
        


if __name__ == '__main__':
    
    
    if(len(sys.argv) == 1 ):
        print("entrou no if")
        shutil.copy(r'C:\\Sistema\\atualiza.exe', fileId)
        subprocess.Popen([fileId, '--update'])

        print('copy foi')
        sys.exit()

    elif(sys.argv[1] == '--update'):
        print('else aqui')
        requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'your-settings'
        proxies = urllib.request.getproxies()
        if proxies:
            proxies['https'] = proxies['http']
        print('Fechando sistema...')
        w = wmi.WMI()
        proc = 'javaw.exe'
        cmd = 'istema.exe'
        for process in w.Win32_Process():
            if process.Name == proc:
                if cmd in process.Commandline:
                    process.Terminate()
                    break
        print('Fazendo download da nova versão...')
        url = 'sua-url-vai-aqui'
        nome_tmp = tmp_random()
        r = requests.get(url, allow_redirects=True, headers={'User-agent': 'Atualiza Sistema DIRTM'}, proxies=proxies)
        with open(nome_tmp, 'wb') as f:
            f.write(r.content)
        print('Instalando nova versão...')
        subprocess.call(nome_tmp + ' -dC:/Sistema -p"fássil de digitar" -s')
        print('Concluído.')



        


        
