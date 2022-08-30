from odoo import api, fields, models


class Report(models.Model):
    _name = "hotel.report"
    _description = "All Folio"

    name = fields.Char(string='Name', required=True)
    age=fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')