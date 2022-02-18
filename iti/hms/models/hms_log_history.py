from  odoo import models , fields
class HmsLog(models.Model):
    _name = "hms.loghistory"
    _rec_name = 'description'

    description = fields.Text(required=True)
    patient_id = fields.Many2one("hms.patient")
