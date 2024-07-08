from odoo import fields, models

class IngresosMec(models.Model):
    _name='ingresos.mec'
    _description='Ingresos Mec Model' 

    employee_id = fields.Many2one('hr.employee', string='Employee')
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    amount = fields.Integer (string="Amount")
    date = fields.Date(string="Date")
