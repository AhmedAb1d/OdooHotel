from odoo import api, fields, models


class HotelClient(models.Model):
    _name = "hotel.client"
    _description = "Hotel client"

    name = fields.Char(string='Name', required=True)
    age=fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')

class Report(models.Model):
    _name = "hotel.report"
    _description = "Hotel Report"

    name = fields.Char(string='Name', required=True)
    age=fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')