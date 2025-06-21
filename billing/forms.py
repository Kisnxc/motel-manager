from django import forms
from .models import Bill

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['month', 'electricity', 'water']  # Chỉ cho nhập những trường này

        widgets = {
            'month': forms.DateInput(
                format='%d/%m/%Y',  # ✅ định dạng ngày/tháng/năm
                attrs={
                    'class': 'form-control',
                    'placeholder': 'dd/mm/yyyy',
                    'type': 'text'  # không dùng 'date' vì HTML type="date" dùng format yyyy-mm-dd
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(BillForm, self).__init__(*args, **kwargs)
        self.fields['month'].input_formats = ['%d/%m/%Y']
