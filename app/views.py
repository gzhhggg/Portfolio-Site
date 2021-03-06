from django.views.generic import View
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Profile, Work, Experience, Education,OS,Language,Database,Framework,Cloud
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
import textwrap


class IndexView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by("-id")[0]
        work_data = Work.objects.order_by("id")
        return render(request, 'app/index.html', {
            'profile_data': profile_data,
            'work_data': work_data
        })

class DetailView(View):
    def get(self, request, *args , **kwargs):
        work_data = Work.objects.get(id=self.kwargs['pk'])
        return render(request,'app/detail.html',{
            'work_data':work_data
        })

class AboutView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by("-id")[0]
        experience_data = Experience.objects.order_by("-id")
        education_data = Education.objects.order_by("-id")
        OS_data = OS.objects.order_by("-id")
        Language_data = Language.objects.order_by("-id")
        Database_data = Database.objects.order_by("-id")
        Framework_data = Framework.objects.order_by("-id")
        Cloud_data = Cloud.objects.order_by("-id")
        return render(request, 'app/about.html', {
            'profile_data': profile_data,
            'experience_data': experience_data,
            'education_data': education_data,
            'OS_data':OS_data,
            'Language_data':Language_data,
            'Database_data':Database_data,
            'Framework_data':Framework_data,
            'Cloud_data':Cloud_data,
        })

class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)

        return render(request, 'app/contact.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = form = ContactForm(request.POST or None)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = '???????????????????????????????????????????????????'
            content = textwrap.dedent('''
                ???????????????????????????????????????????????????????????????

                {name} ???

                ??????????????????????????????????????????????????????
                ????????????????????????????????????????????????????????????????????????
                ????????????????????????????????????????????????????????????????????????????????????????????????????????????

                --------------------
                ????????????
                {name}

                ????????????????????????
                {email}

                ??????????????????
                {message}
                --------------------
                ''').format(
                    name=name,
                    email=email,
                    message=message
                )

            to_list = [email]
            bcc_list = [settings.EMAIL_HOST_USER]

            try:
                message = EmailMessage(subject=subject, body=content, to=to_list, bcc=bcc_list)
                message.send()
            except BadHeaderError:
                return HttpResponse("?????????????????????????????????????????????")

            return redirect('thanks') # ????????????

        return render(request, 'app/contact.html', {
            'form': form
        })

class ThanksView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/thanks.html')
