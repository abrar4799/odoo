from datetime import date

from odoo import models, fields ,api
from odoo.exceptions import UserError
from validate_email import validate_email

class HmsPatient(models.Model):
    _name = "hms.patient"
    state =fields.Selection([
        ('undetermined' , 'Undetermined') ,
        ('good', 'Good,'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),

    ])
    firstname = fields.Char(required=True)
    lastname = fields.Char(required=True)
    email = fields.Char()
    birthdate = fields.Date()
    history = fields.Html()
    crRatio = fields.Float()
    Blood = fields.Selection([('o', 'O'), ('A', 'a'), ('ab', 'AB'), ('b', 'B')])
    PCR = fields.Boolean('is done')
    image = fields.Image()
    address = fields.Text()
    age = fields.Integer(compute= '_cal_patient_age' , store= True)  #store= true to save
    dept_id = fields.Many2one('hms.dept')
    dept_name = fields.Char(related="dept_id.name")
    docs_ids = fields.Many2many('hms.doc')
    log_history_ids = fields.One2many('hms.loghistory' , 'patient_id')

    _sql_constraints = [
        ('email_unique_constraint' , 'UNIQUE(email)' , 'Email is already exist')
    ]
    @api.onchange('age')
    def _onchange(self):
        if self.age > 30 :
            self.PCR = True
            return {
                'warning':{
                    'title': 'Alert',
                    'message': 'pcr is checked'
                }
            }


    def StateUndetermined(self):
        self.state = 'undetermined'

    def StateGood(self):
        self.state = 'good'
    def StateFair(self):
        self.state = 'fair'

    def StateSerious(self):
        self.state = 'serious'

    @api.constrains('email')
    def _check_email(self):
       if len(self.email) < 3:
          raise UserError("Invalid email")


    #exe on create patient
    @api.model
    def create(self, vals_list):
           vals_list['email'] = vals_list['firstname'] + '@gmail.com'
           res = super(HmsPatient , self).create(vals_list)
           return res
    #exe on edit and save
    def write(self, vals):
        if 'firstname' in vals:
            vals['email'] = vals['firstname'] + '@gmail.com'
        super().write(vals)
    @api.depends('birthdate')
    def _cal_patient_age(self):
        for rec in self:
          if self.birthdate:
             rec.age = date.today().year - rec.birthdate.year
          else:
              rec.age = 0


    def write(self, vals):
        if 'state' in vals:
            self.env['hms.loghistory'].create({
                'description': 'your state changed',
                'patient_id': self.id
            })
        super().write(vals)