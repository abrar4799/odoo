from odoo import models , fields , api

class CustInhert(models.Model):
    _inherit = 'res.partner'
    related_patient_id = fields.Many2one('hms.patient')

    @api.constrains('related_patient_id')
    def _email_val(self):
        if self.email == self.related_patient_id.email:
            raise ValueError('Email Exist')

    def unlink(self):
        if self.related_patient_id:
            raise ValueError('Can not delete ')
        return super().unlink
