# -*- coding: utf-8 -*-
{
    'name': "az_reclaims",

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
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['az_expedients','az_documents','base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/reclaim.xml',
        'views/license.xml',
        'views/menu.xml',
        'views/expedient.xml',
        'data/sequence.xml',
        
    ],
    'installable': True,
    'application': True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
