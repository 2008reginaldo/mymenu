# A navegação começa de baixo para cima

from tasks import *

# level 1 ----------------------------------------------
rclone_menu = {
    1: ('Get quotas', [get_quotas, ]),
    2: ('mount gdrive-2008reginaldo', [os.system,
                             ('rclone mount gdrive-2008reginaldo: ${HOME}/Cloud/gdrive-2008reginaldo --daemon') ]),
    3: ('mount gdrive-projetocaos2501', [os.system,
                             ('rclone mount gdrive-projetocaos2501: ${HOME}/Cloud/gdrive-projetocaos2501 --daemon') ]),
    4: ('mount gdrive-receiver', [os.system,
                             ('rclone mount gdrive-receiver: ${HOME}/Cloud/gdrive-receiver --daemon') ]),
    5: ('mount gdrive-sender', [os.system,
                             ('rclone mount gdrive-sender: ${HOME}/Cloud/gdrive-sender --daemon') ]),
    6: (f'check sync status of {HOSTNAME} folder', [check_sync_status, ]),
    7: ('check sync status of common folder', [check_sync_status, ('common')]),
    8: ('rclone bisync to lst-gpu-1', [sync_remotes_rclone, ('lst-gpu-1')]),
    9: ('rclone bisync to lst-gpu-2', [sync_remotes_rclone, ('lst-gpu-2')]),
    10: ('rclone bisync to lst-gpu-3', [sync_remotes_rclone, ('lst-gpu-3')]),
    11: ('rclone bisync to lst-gpu-all', [sync_remotes_rclone, ('lst-gpu-all')]),
}

ssh_menu = {
    1: ('ssh to lst-gpu-1', [os.system,
                             (f'ssh -L 8881:localhost:8881 {SHELLHUB_LST_1}') ]),
    2: ('ssh to lst-gpu-2', [os.system,
                             (f'ssh -L 8882:localhost:8882 {SHELLHUB_LST_2}') ]),
    3: ('ssh to lst-gpu-3', [os.system,
                             (f'ssh -L 8883:localhost:8883 {SHELLHUB_LST_3}') ]),
    4: ('mount lst-gpu-1', [os.system,
                             (f'sshfs {SHELLHUB_LST_1}:/home/reginaldo {HOME_DIRECTORY}/Cloud/lst-gpu-1') ]),
    5: ('mount lst-gpu-2', [os.system,
                             (f'sshfs {SHELLHUB_LST_2}:/home/reginaldo {HOME_DIRECTORY}/Cloud/lst-gpu-2') ]),
    6: ('mount lst-gpu-3', [os.system,
                             (f'sshfs {SHELLHUB_LST_3}:/home/reginaldo {HOME_DIRECTORY}/Cloud/lst-gpu-3') ]),
    7: ('sync to lst-gpu-1 (change remote)', [sync_remotes, ('to', 'lst-gpu-1')]),
    8: ('sync to lst-gpu-2 (change remote)', [sync_remotes, ('to', 'lst-gpu-2')]),
    9: ('sync to lst-gpu-3 (change remote)', [sync_remotes, ('to', 'lst-gpu-3')]),
    10: ('sync to lst-gpu-all (change remote)', [sync_remotes, ('to', 'lst-gpu-all')]),
    11: ('sync from lst-gpu-1 (change local)', [sync_remotes, ('from', 'lst-gpu-1')]),
    12: ('sync from lst-gpu-2 (change local)', [sync_remotes, ('from', 'lst-gpu-2')]),
    13: ('sync from lst-gpu-3 (change local)', [sync_remotes, ('from', 'lst-gpu-3')]),
    14: ('sync from lst-gpu-all (change local)', [sync_remotes, ('from', 'lst-gpu-all')]),
    15: ('connect qtconsole to lst-gpu-3 jupyter server', [launch_qtc, (SHELLHUB_LST_3)])
}

nixos_menu = {
    1: ('create folders', [create_folders, ]),
    2: ('nixos rebuild', [nixos_rebuild, ]),
    3: ('test func', [check_git_status, (f'{HOME_DIRECTORY}/Dropbox/Academico/libgenw/') ]),
}

miscellaneous_menu = {
    1: ('Create github repository', [create_github_repo, ]),
    2: ('Push to github (main branch)', [push_to_github, ]),
    3: ('Qtile in a Xephyr session', [qtile_Xephyr, ]),
}

# level 0 ----------------------------------------------
menu_0 = {
    1: ('rclone', [rclone_menu, ]),
    2: ('ssh', [ssh_menu, ]),
    3: ('nixos', [nixos_menu, ]),
    4: ('miscellaneous', [miscellaneous_menu, ]),
    5: ('make local backup', [make_local_backup, ]),
}
