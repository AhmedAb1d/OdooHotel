from odoo import api, fields, models


class HotelClient(models.Model):
    _name = "hotel.housekeeping"
    _description = "Hotel client"

    name = fields.Char(string='Name', required=True)
    age=fields.Integer(string='age')
    task = fields.Text(string='The given task')
    note = fields.Text(string='Description')