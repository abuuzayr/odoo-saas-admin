# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'SMECEN SAAS Admin',
    'version' : '1.1',
    'summary': 'Manages administration of SMECEN Infrastructure',
    'sequence': 30,
    'description': 'Manages administration of SMECEN Infrastructure',
    'depends' : [
        'base',
    ],
    'data': [
        'views/main/instance.xml',
        'views/main/menuitem.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'Other proprietary',
}
