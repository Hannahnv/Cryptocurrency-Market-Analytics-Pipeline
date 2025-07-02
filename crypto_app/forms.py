# crypto_app/forms.py
from django import forms

class CSVUploadForm(forms.Form):
    """Form for uploading CSV files."""
    
    # Choices for CSV data types
    CSV_TYPE_CHOICES = [
        ('coins', 'Cryptocurrency information'),
        ('historical', 'Historical data'),
        ('github', 'GitHub information'),
        ('languages', 'Programming languages'),
    ]
    
    # Field for selecting data type
    csv_type = forms.ChoiceField(
        choices=CSV_TYPE_CHOICES,
        label='Data type',
        widget=forms.Select(attrs={'class': 'form-select'}),
        help_text='Select the data type corresponding to the CSV file'
    )
    
    # Field for uploading file
    csv_file = forms.FileField(
        label='CSV File',
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': '.csv'}),
        help_text='Select the CSV file to import data'
    )