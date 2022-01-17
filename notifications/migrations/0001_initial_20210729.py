# Generated by Django 3.1.5 on 2021-07-29 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    replaces = [
        ('notifications', '0001_initial_20210326'),
        ('notifications', '0003_auto_20200727_1101'),
        ('notifications', '0001_initial_v2'),
        ('notifications', '0001_squashed_0004_subscription_enabled'),
        ('notifications', '0001_initial'),
        ('notifications', '0002_auto_20180920_1631'),
        ('notifications', '0003_unfurl'),
        ('notifications', '0004_subscription_enabled'),
        ('notifications', '0002_auto_20191024_0917'),
    ]

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                (
                    'external_token',
                    models.CharField(
                        blank=True,
                        help_text='If set, notifications be posted to this event through the API',
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    'slack_username',
                    models.CharField(
                        blank=True,
                        help_text='Choose a display name for Slack bot (instead of default)',
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    'slack_icon',
                    models.CharField(
                        blank=True,
                        help_text='Choose an icon for Slack bot (instead of default)',
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    'slack_unfurl_links',
                    models.BooleanField(
                        default=True, help_text='Pass true to enable unfurling of primarily text-based content on Slack'
                    ),
                ),
                (
                    'mail_from',
                    models.CharField(
                        blank=True,
                        help_text='Choose the sender address of the email (instead of default)',
                        max_length=200,
                        null=True,
                    ),
                ),
                (
                    'mail_reply_to',
                    models.CharField(
                        blank=True,
                        help_text='Choose the reply-to address of the email (instead of none)',
                        max_length=200,
                        null=True,
                    ),
                ),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'service',
                    models.CharField(choices=[('S', 'Slack'), ('M', 'Mail'), ('T', 'Mail TLA Owners')], max_length=1),
                ),
                ('target', models.TextField(blank=True, help_text='You can specify multiple targets, one per line.')),
                ('enabled', models.BooleanField(default=True)),
                (
                    'event',
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='notifications.event'),
                ),
            ],
            options={
                'verbose_name': 'Subscription',
                'verbose_name_plural': 'Subscriptions',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Sent'), (-1, 'Error')], default=0)),
                ('target', models.TextField(default=None, null=True)),
                ('options', models.TextField(default=None, null=True)),
                (
                    'subscription',
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to='notifications.subscription'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
    ]
