import json
import typing
import logging
import subprocess

import salt.utils.platform

# Инициализация логгера
log = logging.getLogger(__name__)

# Имя по которому будет доступен модуль grains
__virtualname__ = 'blockdevices'

# Является ли текущий миньон windows машиной
IS_WINDOWS: bool = salt.utils.platform.is_windows()

def __virtual__():
    if IS_WINDOWS:
        log.debug('Module only for Linux')
        return False
    return True

def produce_info():
    blk_dict: dict[str, dict] = {}

    log.debug('Run `lsblk --json` command')
    lsblk = subprocess.run('lsblk --json', shell=True, stdout=subprocess.PIPE, encoding='UTF-8')
    lsblk = json.loads(lsblk.stdout.replace('\n', ''))

    for dev in lsblk.get('blockdevices'):
        blk_dict.update({
            dev.get('name') : {
                'size': dev.get('size'),
                'read_only': dev.get('ro'),
                'type': dev.get('type'),
            }
        })
    res = {'blockdevices': blk_dict}

    return res

if __name__ == '__main__':
    from pprint import pprint
    pprint(produce_info())
