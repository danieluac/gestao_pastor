# -*- coding: utf-8 -*-
{
    'name': "gestao_pastor",
    'summary': """ """,
    'description': """  """,
    'author': "Daniel AC  ",
    'website': " ",
    'category': 'Igreja',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        'data/sequence.xml',
        'security/priest_security.xml',
        'views/pastor_views.xml',
        'views/escalas_views.xml',
        'views/cultos_views.xml',
        'views/paroquia_views.xml',
        # 'views/menus.xml',
        'views/assets.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
