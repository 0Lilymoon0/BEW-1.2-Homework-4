from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import ItemCategory, GroceryStore, GroceryItem

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    title = StringField('Grocery Store Title', validators=[DataRequired()])
    address = StringField('Grocery Store Address', validators=[DataRequired()])
    submit_button = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    name = StringField('Item Name', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    category = SelectField('Category', choices=ItemCategory.choices())
    photo_url = StringField('Photo URL', validators=[URL()])
    store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query, allow_blank=False)
    submit_button = SubmitField('Submit')