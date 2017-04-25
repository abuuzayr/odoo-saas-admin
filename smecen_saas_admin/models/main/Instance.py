from openerp import api, fields, models
from openerp.addons.smecen_saas_admin.lib.ansible import Playbook

class Instance(models.Model):

    _name = 'smecen_saas_admin.instance'

    name = fields.Char()
    host_id = fields.Many2one('smecen_admin.host', string='Host')


    @api.multi
    def start_instance(self):
        pb = Playbook(
            playbooks=['hello.yml'],
            options={
                'user': self.host_id.user,
                'inventory': '{0},'.format(self.host_id.ip),
                'extra-vars': ','.join([
                    'hello_name=hellyna',
                ]),
                # TODO: Secure host key checking
                'ssh-common-args': '-o StrictHostKeyChecking=no -p {0}'.format(
                    self.host_id.port),
            },
        )
        pb.play()
