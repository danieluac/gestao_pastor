# -*- coding: utf-8 -*-
# from odoo import http


# class GestaoPastor(http.Controller):
#     @http.route('/gestao_pastor/gestao_pastor/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestao_pastor/gestao_pastor/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestao_pastor.listing', {
#             'root': '/gestao_pastor/gestao_pastor',
#             'objects': http.request.env['gestao_pastor.gestao_pastor'].search([]),
#         })

#     @http.route('/gestao_pastor/gestao_pastor/objects/<model("gestao_pastor.gestao_pastor"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestao_pastor.object', {
#             'object': obj
#         })
