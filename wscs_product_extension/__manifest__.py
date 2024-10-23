{
    'name': 'WSCS Product Extension',
    'version': '1.0',
    'summary': 'Extension for product forms',
    'depends': [
        'product',
        'stock_delivery'
    ],
    'author': 'WSCS',
    'category': 'Inventory',
    'data': [
        'security/ir.model.access.csv',
        'views/product_status_views.xml',
        'views/product_packaging_view.xml',
        'views/product_palletspec_view.xml',
        'menu/product_status_menu.xml',
        'menu/product_palletspec_menu.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
