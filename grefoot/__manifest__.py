# -*- coding: utf-8 -*-
{
    'name': "grefoot",

    'summary': """
        An awesome module for building Ecommerce platform
        """,

    'description': """
        An awesome module for building Ecommerce platform
    """,

    'author': "Rubik",
    'website': "http://www.rubik.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','ks_theme_kinetik','checkout','facebook_messenger_chat','payment_cash_on_delivery','sales_report_product_image','website_add_whatsapp','website_js_below_the_fold','website_lazy_load_image'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/module_view.xml',
        'views/templates.xml',
        'models/inherit/contact_us_form/grefoot_contact_us_form_website.xml',
        'models/inherit/grefoot_country/grefoot_country_view.xml',
        'models/mobile_config/mobile_config_view.xml',
        'models/inherit/product_public_category/product_public_category_view.xml'
        # 'models/inherit/grefoot_website_sale_address/grefoot_website_sale_address.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}