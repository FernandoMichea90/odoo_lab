from odoo import fields,models

class PruebaMec(models.Model):
    _name='prueba.mec'
    _description='Prueba Mec Model' 

    nombre = fields.Char(string="Nombre", required=True)
    employee_id = fields.Many2one('hr.employee', string='Employee A')

