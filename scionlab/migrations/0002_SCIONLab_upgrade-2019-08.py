# Generated by Django 2.2 on 2019-08-26 09:23
# This migrations was manually edited
# It:
# - Removes all Service of type 'ZK' (Zookeeper).
# - Removes the DB field 'port' from the Service model.
# - Removes the constant 'ZK' as option for the 'type' in the Service model.
# - Bumps the version for all Host instances (all configurations will be outdated).

from django.db import migrations, models
import scionlab.models.core


def remove_zk(apps, schema_editor):
    Service = apps.get_model('scionlab', 'Service')
    Service.objects.filter(type='ZK').delete()


def bump_config(apps, schema_editor):
    Host = apps.get_model('scionlab', 'Host')
    Host.objects.bump_config()


class Migration(migrations.Migration):

    dependencies = [
        ('scionlab', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(remove_zk),
        migrations.RemoveField(
            model_name='service',
            name='port',
        ),
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(choices=[('BS', 'Beacon Server'), ('PS', 'Path Server'), ('CS', 'Certificate Server'), ('BW', 'Bandwidth tester server'), ('PP', 'Pingpong server')], max_length=16),
        ),
        # need use_in_migrations = True in HostManager for us to call .bump_config in migrations
        migrations.AlterModelManagers(
            name='host',
            managers=[
                ('objects', scionlab.models.core.HostManager()),
            ],
        ),
        migrations.RunPython(bump_config),
    ]