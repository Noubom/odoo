# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class mon_module_01(models.Model):
#     _name = 'mon_module_01.mon_module_01'
#     _description = 'mon_module_01.mon_module_01'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
