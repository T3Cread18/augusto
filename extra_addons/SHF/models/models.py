# -*- coding: utf-8 -*-

from odoo import models, fields, api


class task(models.Model):
     _name = 'shf.task'
     _description = 'SHF.task'

     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class x_customers(models.Model):
     _name = 'shf.x_customers'
     _description = 'Customers'

     name = fields.Char()
     phone = fields.Integer()
     address = fields.Char()
     city = fields.Char()
     state = fields.Char()
     zip = fields.Integer()
     comment = fields.Char()