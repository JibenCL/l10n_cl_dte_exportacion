# -*- coding: utf-8 -*-
from openerp import fields, models, api, _

class ResCurrency(models.Model):
    _inherit = 'res.currency'
    
    code = fields.Char(
            string="Código",
        )
    abreviatura = fields.Char(
            string="Abreviatura",
        )
