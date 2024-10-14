{
    'name': 'WSCS vendor Extension',
    'version': '1.0',
    'summary': 'Extension for vendor forms',
    'depends': ['purchase', 'product', 'stock'],
    'author': 'WSCS',
    'data': [
        'security/ir.model.access.csv',
        'views/vendor_status_view.xml',
        'views/gfsi_and_certification_view.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
