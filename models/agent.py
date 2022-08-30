from odoo import api, fields, models


class HotelClient(models.Model):
    _name = "hotel.agent"
    _description = "Hotel client"

    name = fields.Char(string='Name', required=True)
    age=fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    task = fields.Text(string='Task')
    note = fields.Text(string='Additional info about this agent')
