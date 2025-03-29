from django.core.validators import RegexValidator
from django.forms.fields import EmailField


class StudEmailField(EmailField):
    studDomain = 'stud.uni-heidelberg.de'

    def __init__(self, *args, **kwargs):
        validators = kwargs.get('validator', [])
        validators.append(
            RegexValidator(regex=f'.+@{self.studDomain}',
                           message=f'You have to use a @{self.studDomain} mail address.'))
        kwargs['validators'] = validators

        super().__init__(*args, **kwargs)
