import vim
import rpc
import time
import logging
import os.path

start_time = time.time()
base_activity = {
        'details': 'Nothing',
        'state': 'Nothing',
        'timestamps': {
            "start": start_time
        },
        'assets': {
            'small_text': 'Vim',
            'small_image': 'vim_logo',
            'large_text': 'Vim',
            'large_image': 'vim_logo'
        }
    }

client_id = '499582279258079233'

try:
    rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)
    rpc_obj.set_activity(base_activity)
except Exception as e:
    # Discord is not running
    pass

def update_presence():
    """Update presence in Discord
    :returns: TODO

    """
    activity = base_activity
    activity['state'] = get_cwd()
    activity['details'] = get_filename()
    # activity['assets']['large_text'] = 'Editing a {} file'.format(get_extension().upper())
    activity['assets']['large_image'] = 'vim'
    #if get_extension():
    #    activity['assets']['large_image'] = get_extension()

    try:
        rpc_obj.set_activity(activity)
    except BrokenPipeError as e:
        # Connection to Discord is lost
        pass
    except NameError as e:
        # Discord is not running
        pass

def get_filename():
    """Get current filename that is being edited
    :returns: string
    """
    return vim.eval('expand("%:t")')

def get_cwd():
    """Get current working directory
    :returns: string
    """
    return os.path.basename(os.path.normpath(vim.eval('getcwd()')))

def get_extension():
    """Get exension for file that is being edited
    :returns: string
    """
    return vim.eval('expand("%:e")')
