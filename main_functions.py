import os
import subprocess
from config import *
# from IPython import embed

HOME_DIRECTORY = os.getenv("HOME")
HOSTNAME = os.uname().nodename
ADDRS_FOR_SSH = {
    'lst-gpu-1': SHELLHUB_LST_1,
    'lst-gpu-2': SHELLHUB_LST_2,
    'lst-gpu-3': SHELLHUB_LST_3,
}

def confirm(msg=''):
    print(msg)
    choice = ''
    while choice != 'no' and choice != 'yes':
        choice = str( input("\nExecute this function (yes/no): "))
    print(choice)
    if choice == 'no':
        return 0
    return 1

def bisync_resync(remote_folder, local_folder):
    print("WARNING: executing bisync with --resync flag!")
    print(f"Choose an option:")
    print(f"1: to Sync {remote_folder} and {local_folder}, changing {remote_folder}")
    print(f"2: to Sync {local_folder} and {remote_folder}, changing {local_folder}")
    print("3: to exit")

    choice = ''
    while choice != '1' and choice != '2' and choice != '3':
        choice = str( input("\noption (1/2/3): "))
    if choice == '3':
        return

    if choice == '1':
        try:
            # Run rclone bisync with --resync if the specific error is detected
            subprocess.run(['rclone', 'bisync', remote_folder, local_folder,
                            '--filter-from', f'{local_folder}/rclone-filter',
                            '--resync',
                            '--create-empty-src-dirs',
                            '--resilient',
                            # '--recover',
                            # '--max-lock', '2m',
                            # '--conflict-resolve', 'newer',
                            '--verbose', '-P'], check=True)

            print(f"Resync of {remote_folder} and {local_folder} completed successfully.")
        except subprocess.CalledProcessError as resync_error:
            print(f"Error during rclone bisync --resync: {resync_error}")

    if choice == '2':
        try:
            # Run rclone bisync with --resync if the specific error is detected
            subprocess.run(['rclone', 'bisync', local_folder, remote_folder,
                            '--filter-from', f'{local_folder}/rclone-filter',
                            '--resync',
                            '--create-empty-src-dirs',
                            '--resilient',
                            # '--recover',
                            # '--max-lock', '2m',
                            # '--conflict-resolve', 'newer',
                            '--verbose', '-P'], check=True)

            print(f"Resync of {local_folder} and {remote_folder} completed successfully.")
        except subprocess.CalledProcessError as resync_error:
            print(f"Error during rclone bisync --resync: {resync_error}")

def get_status(remote_folder, local_folder):
    try:
        # Attempt to run rclone bisync normally
        subprocess.run(['rclone', 'bisync', remote_folder, local_folder,
                            '--filter-from', f'{local_folder}/rclone-filter',
                            '--create-empty-src-dirs',
                            '--resilient',
                            # '--recover',
                            # '--max-lock', '2m',
                            # '--conflict-resolve', 'newer',
                            '--verbose', '-P'], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error during rclone bisync:  {e}")
        # if 'Bisync aborted. Must run --resync to recover' in str(e):
        # embed()
        if e.returncode == 2:
            if confirm("Bisync error detected. Would you like to try with --resync?"):
                bisync_resync(remote_folder, local_folder)

def bisync_folders(remote_folder, local_folder):
    # local_folder is a local dir path!

    if not os.listdir(local_folder):  # Check if the folder is empty
        print(f"{local_folder} is empty. Gettings the status of the folders...\n")
        get_status(remote_folder, local_folder)
    else:
        print(f"{local_folder} is not empty. Synchronizing with remote...")
        # Step 3: If not empty, use rclone bisync
        try:
            subprocess.run(['rclone', 'bisync', local_folder, remote_folder,
                            '--create-empty-src-dirs', '--resilient',
                            '-Mv', '--dry-run'], check=True)
            print(f"Synchronized {local_folder} with {remote_folder}.")
        except subprocess.CalledProcessError as e:
            print(f"Error during rclone bisync: {e}")

def rsync_ssh(direction, host_target):

    if host_target == HOSTNAME:
        print('host and host_target are the same')
        return
    shellhub_add = ADDRS_FOR_SSH[host_target]
    local_folder =  os.path.join(HOME_DIRECTORY, 'SyncedFiles', host_target)
    remote_folder = shellhub_add + ':' + os.path.join('/home/reginaldo/SyncedFiles', host_target)

    if direction == 'to':
        cmd = f'rsync -avzP  {local_folder}/ -e ssh {remote_folder}/ --filter="merge {local_folder}/rsync-filter.txt"'
        print(f'Syncing {local_folder} to {remote_folder}. Changing remote')
    if direction == 'from':
        cmd = f'rsync -avzP -e ssh {remote_folder}/ {local_folder}/ --filter="merge {local_folder}/rsync-filter.txt"'
        print(f'Syncing {local_folder} from {remote_folder}. Changing local')
    print(cmd)
    os.system(cmd)
