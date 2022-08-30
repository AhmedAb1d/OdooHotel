from odoo import api, fields, models


class HotelClient(models.Model):
    _name = "hotel.restaurant"
    _description = "Hotel client"

    name = fields.Char(string='Meal Name', required=True)
    age=fields.Integer(string='Number of meals')
    note = fields.Text(string='Description')
