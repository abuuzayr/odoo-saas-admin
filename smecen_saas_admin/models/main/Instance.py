from openerp import fields, models
from openerp.addons.smecen_saas_admin.lib.ansible import Playbook

class Instance(models.Model):

    _name = 'smecen_saas_admin.instance'

    name = fields.Char()
    host_id = fields.Many2one('smecen_admin.host', string='Host')

    def start_instance(self):
        pb = Playbook(
            playbooks=['hello.yml'],
            options={
                'remote_user': self.host_id.user,
                'inventory': '{0},'.format(self.host_id.ip),
                'verbosity': 2,
                'extra_vars': [
                    'hello_name=hellyna',
                    'ansible_port={0}'.format(self.host_id.port),
                ],
                # TODO: Secure host key checking
                'ssh_common_args': '-o StrictHostKeyChecking=no'
            },
        )
        pb.play()
