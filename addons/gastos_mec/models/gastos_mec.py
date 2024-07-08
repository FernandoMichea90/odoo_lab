from odoo import fields, models

class GastosMec(models.Model):
    _name = "gastos.mec"
    _description = "Gastos Mec Model"

    employee_id = fields.Many2one('hr.employee', string='Employee')
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    amount = fields.Integer (string="Amount")
    date = fields.Date(string="Date")


    # employee_id = fields.Many2one('hr.employee', string='Employee')