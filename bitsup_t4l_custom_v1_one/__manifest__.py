# -*- coding: utf-8 -*-
{
    'name': 'T4L - Odoo Custom Functionality v1',
    'version': '16.0.1.0.1',
    'category': 'Sales',
    'summary': 'Custom Functionality.',
    'author': 'Vignesh - Senior Odoo ERP Consultant',
    'company': 'BitsUp Technologies',
    'website': "https://www.bitsuptech.com",
    'depends': ['base', 'sale', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/sale.xml',
        'views/product.xml',
        'views/purchase.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
