# -*- coding: utf-8 -*-
{
    'name': "sopoka_mps",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mrp', 'mrp_mps'],
    'qweb': [
        'static/src/xml/qweb_templates.xml'
    ],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/mps_select_plan_wizard.xml',
        'views/templates.xml',
        'views/mps_plan.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
