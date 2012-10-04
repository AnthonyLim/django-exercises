from django import forms
from django.core.validators import validate_email

class MultiEmailField(forms.Field):
    def to_python(self,value):
    	"Normalize data into list of strings"

    	#return an empty list if no input was given.
    	if not value:
    		return []
    	return value.split(',')

    def validate(self,value):
    	"Check if value consists only of valid emails."

    	# Use the parent's handling of required fields, etc.
    	super(MultiEmailField,self).validate(value)

    	for email in value:
    		validate_email(email)

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField()
	sender = forms.EmailField()
	recipients = MultiEmailField()
	cc_myself = forms.BooleanField(required=False)

	def clean_recipients(self):
		data = self.cleaned_data['recipients']
		if "fred@example.com" not in data:
			raise forms.ValidationError("You have forgotten about Fred!")

		# Always return the clean data, whether you have changed it or not.
		return data

	def clean(self):
		cleaned_data = super(ContactForm,self).clean()
		cc_myself = cleaned_data.get('cc_myself')
		subject = cleaned_data.get('subject')

		if cc_myself and subject and 'help' not in subject:
			# We know these are not in self._errors now
			msg = u"Must put 'help' in subject when cc'ing yourself."
			self._errors['cc_myself'] = self.error_class([msg])
			self._errors['subject'] = self.error_class([msg])

			# These fields are no longer valid, Remove them from the cleaned data

			del cleaned_data['cc_myself']
			del cleaned_data['subject']

		#Always return full collection of cleaned data
		return cleaned_data