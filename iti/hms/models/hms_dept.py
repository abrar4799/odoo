from odoo import models , fields
class HmsDept(models.Model):
    _name = 'hms.dept'
    name = fields.Char(required=True)
    capacity = fields.Integer()
    is_open = fields.Boolean()
    patients_ids = fields.One2many('hms.patient' , 'dept_id')
