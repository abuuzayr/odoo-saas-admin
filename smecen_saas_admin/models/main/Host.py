from openerp import fields, models

class Host(models.Model):
    _name = 'smecen_admin.host'

    name = fields.Char()
    ip = fields.Char(string='IP Address') # TODO: Validation
    port = fields.Char(default='22') # TODO: Validation
    user = fields.Char(default='root')
