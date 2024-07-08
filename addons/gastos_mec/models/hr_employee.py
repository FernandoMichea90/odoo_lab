from odoo import fields, models, api

class HREmployee(models.Model):
    _inherit = 'hr.employee'

    ingresos_mec_ids = fields.One2many('ingresos.mec', 'employee_id', string='Ingresos')
    gastos_mec_ids = fields.One2many('gastos.mec', 'employee_id', string='Gastos')
    total_income = fields.Integer(string='Total Income', compute='_compute_total_income')
    total_expenses = fields.Integer(string='Total Expenses', compute='_compute_total_expenses')

    @api.depends('ingresos_mec_ids.amount')
    def _compute_total_income(self):
        for employee in self:
            employee.total_income = sum(employee.ingresos_mec_ids.mapped('amount'))

    @api.depends('gastos_mec_ids.amount')
    def _compute_total_expenses(self):
        for employee in self:
            employee.total_expenses = sum(employee.gastos_mec_ids.mapped('amount'))
