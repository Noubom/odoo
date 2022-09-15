# -*- coding: utf-8 -*-
# from odoo import http


# class MonModule01(http.Controller):
#     @http.route('/mon_module_01/mon_module_01', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mon_module_01/mon_module_01/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mon_module_01.listing', {
#             'root': '/mon_module_01/mon_module_01',
#             'objects': http.request.env['mon_module_01.mon_module_01'].search([]),
#         })

#     @http.route('/mon_module_01/mon_module_01/objects/<model("mon_module_01.mon_module_01"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mon_module_01.object', {
#             'object': obj
#         })
