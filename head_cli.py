from argparse import Namespace, ArgumentParser
from head import HEAD


def get_ref(head_path):
    head = HEAD(head_path)
    ref = head.get_ref()
    print("Current reference: ", ref)


def set_ref(head_path, new_ref):
    head = HEAD(head_path)
    head.set_ref(new_ref)
    print("Reference updated")


def checkout(head_path, new_ref):
    head = HEAD(head_path)
    head.set_ref(new_ref)
    print("Checked out to: ", new_ref)


def command_handler(args: Namespace):
    '''
    Handle the commands using the functions
    '''
