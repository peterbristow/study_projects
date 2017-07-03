from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Post(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField(blank=True, default='')
	created_date = models.DateTimeField()
	created_by = models.ForeignKey(User)
	tags = models.CharField(max_length=255)
	views_total = models.IntegerField(default=0)

	def __str__(self):
		return self.title

	def published_date(self):
		return self.created_date.strftime('%d/%m/%y')

	class Meta:
		ordering = ['-created_date',]


@receiver(post_save, sender=Post)
def send_email_when_post_created_by_admin(sender, instance, **kwargs):
	# For this to work, Uncomment email google server settings in settings.py and add email and password.
	# Wait for "	Review blocked sign-in attempt" email from google then in the email
	# follow the "allowing access to less secure apps" link and click the switch to allow. Email will now
	# send when a post is created.
	title = instance.title
	link = "%s\posts\%s" % (settings.BASE_DIR, instance.id)
	created_by = instance.created_by
	to_email = "adric.warth@jisc.ac.uk"
	from_email = "Django.test@example.com"
	subject = "A new post has been created!"
	html_content = "Title: %s <br> Link: %s <br> Created by: %s"
	message = EmailMessage(subject=subject, body=html_content % (title, link, created_by), from_email=from_email, to=[to_email])
	message.content_subtype = 'html'
	message.send()
