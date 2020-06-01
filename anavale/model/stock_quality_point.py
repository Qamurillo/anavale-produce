# -*- coding: utf-8 -*-

from odoo.exceptions import ValidationError
from odoo import api, fields, models

class StockQualityPoint(models.Model):
    _name = 'stock.quality.point'
    _description = "Stock Quality Control Points"
    _order = 'sequence,name,id'  
        
    @api.model
    def _default_sequence_id(self):
        rec = self.search([], order="sequence desc", limit=1)
        return rec.sequence + 10 if rec else 10
        
    name = fields.Char('Name',required=True)
    sequence = fields.Integer(default=_default_sequence_id, help="Sequence")  