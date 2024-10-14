import os
import subprocess
from main_functions import *

def get_quotas():
    print("\ngdrive-sender:")
    os.system('rclone about gdrive-sender:')
    print("\ngdrive-receiver:")
    os.system('rclone about gdrive-receiver:')
    print("\ngdrive-2008reginaldo:")
    os.system('rclone about gdrive-2008reginaldo:')
    print("\ngdrive-projetocaos2501:")
    os.system('rclone about gdrive-projetocaos2501:')

def qtile_Xephyr():
    if confirm():
        os.system('Xephyr -br -ac -noreset -screen 1024x768 :2 &')
        os.system('DISPLAY=:2 konsole')
        os.system('killall Xephyr')

def create_folders():
    def create_directory_if_not_exists(dir_path):
        if not os.path.exists(dir_path):
            print(f"Directory does not exist. Creating: {dir_path}")
            os.makedirs(dir_path)
        else:
            print(f"Directory already exists: {dir_path}")

    # Use the function to create directories
    create_directory_if_not_exists(os.path.expanduser("~/SyncedFiles/flakes"))
    create_directory_if_not_exists(os.path.expanduser("~/flakes"))
    create_directory_if_not_exists(os.path.expanduser("~/SyncedFiles/bin"))
    create_directory_if_not_exists(os.path.expanduser("~/bin"))
    create_directory_if_not_exists(os.path.expanduser("~/.config/rclone"))
    create_directory_if_not_exists(os.path.expanduser("~/Cloud/gdrive-2008reginaldo"))
    create_directory_if_not_exists(os.path.expanduser("~/Cloud/gdrive-projetocaos2501"))
    create_directory_if_not_exists(os.path.expanduser("~/Cloud/gdrive-receiver"))
    create_directory_if_not_exists(os.path.expanduser("~/Cloud/gdrive-sender"))
    create_directory_if_not_exists(os.path.expanduser("~/Cloud/gphotos-pessoal"))
    create_directory_if_not_exists(os.path.expanduser("~/Cloud/lst-gpu-1"))
    create_directory_if_not_exists(os.path.expanduser("~/Cloud/lst-gpu-2"))
    create_directory_if_not_exists(os.path.expanduser("~/Cloud/lst-gpu-3"))


def check_sync_status(folder = HOSTNAME):

    if HOSTNAME in ['notebook', 'desktop']:
        remote = 'gdrive-2008reginaldo:'
    elif HOSTNAME in ['lst-gpu-1', 'lst-gpu-2', 'lst-gpu-3'] :
        remote = 'gdrive-sender:'
    else:
        print('Fail to infering the remote')
        return

    remote_folder = remote + os.path.join('SyncedFiles', folder)
    local_folder =  os.path.join(HOME_DIRECTORY, 'SyncedFiles', folder)

    get_status(remote_folder, local_folder)

def sync_remotes_rclone(target):

    if target in ['lst-gpu-1', 'lst-gpu-2', 'lst-gpu-3'] :
        remote = target
    else:
        print('Fail to infering the remote')
        return

    remote_folder = remote +':/home/reginaldo/'+ os.path.join('SyncedFiles', target)
    local_folder =  os.path.join(HOME_DIRECTORY, 'SyncedFiles', target)

    get_status(remote_folder, local_folder)

def sync_remotes(parameters):
    direction = parameters[0]
    host_target = parameters[1]
    rsync_ssh(direction=direction, host_target=host_target)

def make_local_backup():
    if HOSTNAME == 'notebook':
        source = '/home/regis/SyncedFiles/*'
        destination = '/run/media/regis/HD-Externo/SyncedFiles'

    cmd = f'rsync -avzP {source} {destination}'
    os.system(cmd)

def create_github_repo():
     repository_name = os.path.basename( os.getcwd() )
     if confirm(f'Do you want to create a repository named {repository_name}?'):
        cmd_p1 = '\'{"name":' + f'"{repository_name}' + '"}\''
        cmd = f'curl -H "Authorization: token {GH_TOLKEN}" https://api.github.com/user/repos -d {cmd_p1}'
        print('\nCreating repository')
        os.system(cmd)
        print('\nDone!!')

        cmd2 = f'git remote set-url origin https://{GH_TOLKEN}@github.com/{GH_USERNAME}/{repository_name}'
        print('\nSetting Up for CLI push')
        os.system(cmd2)
        print('\nDone!!')

def push_to_github():
    repository_name = os.path.basename( os.getcwd() )
    cmd = f'git push -u origin main'
    print(cmd)
    os.system(cmd)

def nixos_rebuild():
    flake_dir = f'{HOME_DIRECTORY}/SyncedFiles/common/flakes/{HOSTNAME}'
    cmd = f'git -C {flake_dir} log -1 --pretty=%B'
    p1 = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    last_commit_msg = result.stdout.strip().replace(' ', '_')
    print(last_commit_msg)
    cmd = f'sudo nixos-rebuild switch -p {last_commit_msg} --flake {HOME_DIRECTORY}/SyncedFiles/common/flakes/{HOSTNAME}#{HOSTNAME}'
    print(cmd)
    os.system(cmd)

def launch_qtc(remote):
    print(remote)
    cmd0 = f"rsync -avz -e ssh {remote}:/home/reginaldo/.local/share/jupyter/runtime/ /home/regis/.local/share/jupyter/runtime"
    print(cmd0)
    cmd1 = "jupyter-qtconsole --JupyterWidget.font_size=16 --JupyterWidget.font_family='SauceCodePro Nerd Font Mono' --JupyterWidget.scrollbar_visibility=False "
    cmd2 = f" --ssh={remote} --existing /home/regis/.local/share/jupyter/runtime/kernel-76937.json "
    cmd = f'nix-shell /home/regis/SyncedFiles/bin/mymenu/nix-shells/qtc3.nix --run "{cmd1} + {cmd2} &"'

    #os.system(cmd0)
    os.system(cmd)
    #p1 = subprocess.run(cmd1, shell=True, capture_output=True, text=True)
    #p1 = subprocess.run(cmd2, shell=True, capture_output=True, text=True)

