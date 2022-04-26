import os
import glob
import subprocess
import unicodedata


def exec_subprocess(cmd: str, raise_error=True):
    child = subprocess.Popen(cmd, shell=True,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = child.communicate()
    rt = child.returncode
    if rt != 0 and raise_error:
        raise Exception(f"command return code is not 0. got {rt}. stderr = {stderr}")

    return stderr.decode('utf-8')
    # return stdout, stderr, rt


def move():
    ue_files = set(map(lambda x: x[3:], glob.glob('../*.wav')))
    now_files = set(map(lambda x: x[5:], glob.glob('./fix*.wav')))
    print(ue_files)
    print(now_files)
    for file in now_files:
        if file not in ue_files:
            os.system(f'mv fix{file} ../normalized/{file}')
        else:
            i = 1
            while (True):
                fnames = file.split('.')
                fnames.insert(len(fnames)-1, '_' + str(i))
                fnames.insert(len(fnames)-1, '.')
                fixed = ''.join(fnames)
                print('fixing:', fnames)
                if fixed not in ue_files:
                    os.system(f'mv fix{file} ../{fixed}')
                    break
                i = i + 1



if __name__ == "__main__":
    files = glob.glob('*.wav')
    print(os.getcwd())
    for file in files:
        # print(f'ffmpeg -i {file} -af volume=10dB {file}')
        # os.system(f'ffmpeg -i {file} -af volume=10dB 10{file}')
        ret = exec_subprocess(f'ffmpeg -i {file} -vn -af volumedetect -f null -')
        for line in ret.split('\n'):
            if 'max_volume' in line:
                vol = 0.0 - float(line.split(' ')[-2])
                os.system(f'ffmpeg -i {file} -af volume={vol}dB fix{file}')
                break
    move()


