# -*- coding: utf-8 -*-
{
    'name': "AZ Reclaims",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
	'version': '1.0',
	'license': 'OPL-1',
	'installable': True,
	'auto_install': False,
	'application': True,

    # any module necessary for this one to work correctly
    'depends': ['az_expedients','az_documents','base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/expedient.xml',
        'views/settings.xml',
    ],
    'installable': True,
    'application': True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
