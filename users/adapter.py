from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
       
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.language_prefered = data.get('language_prefered')
        print("in save user")
        print(data.get('language_prefered'))
        user.mobile_number = data.get('mobil')
        user.save()
        return user