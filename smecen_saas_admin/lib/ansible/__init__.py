import logging
import os
import subprocess

from odoo.exceptions import UserError


_l = logging.getLogger(__name__)

class Playbook(object):
    def __init__(self,
            playbooks=[],
            options={},
            ansible_playbook='/usr/local/bin/ansible-playbook',
            cwd=os.path.dirname(__file__)):
        self._playbooks = playbooks
        self._options = options
        self._bin = ansible_playbook
        self._cwd = cwd


    def play(self):
        p = subprocess.Popen(
                self._make_args(),
                cwd=self._cwd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

        out, err = p.communicate()

        if p.returncode != 0:
            raise UserError(_(
                'Ansible failed (error code: {0}. Message: {1}'.format(
                    str(p.returncode), err
                    )))

        # TODO: process.returncode


    def _make_args(self):
        args = [self._bin]

        for k in self._options:
            v = self._options[k]
            args.append('--{0}'.format(k))
            args.append(str(v))

        args.extend(self._playbooks)

        return args
