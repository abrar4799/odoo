from odoo import models , fields
class HmsDoc(models.Model):
    _name = 'hms.doc'
    firstname = fields.Char()
    lastname = fields.Char()
    image = fields.Image()