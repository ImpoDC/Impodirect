{
    'name': 'stock_picking_inherit',
    'version': '1.0',
    'summary': 'Agregar valor de cotizacion para el despacho',
    'description': """
        Módulo para agregar un campo del valor de la cotizacion para el despacho
    """,
    'author': 'Ismael Calle',
    'category': 'Sales',
    'depends': ['product','purchase','stock','res_courier'],
    'data': [
        'views/stock_picking_inherit_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
