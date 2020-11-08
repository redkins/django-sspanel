# Generated by Django 3.1.2 on 2020-11-07 20:00

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sspanel', '0003_auto_20200729_0733'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrojanNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_id', models.IntegerField(unique=True)),
                ('level', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=32, verbose_name='名字')),
                ('info', models.CharField(max_length=1024, verbose_name='节点说明')),
                ('country', models.CharField(choices=[('US', '美国'), ('CN', '中国'), ('GB', '英国'), ('SG', '新加坡'), ('TW', '台湾'), ('HK', '香港'), ('JP', '日本'), ('FR', '法国'), ('DE', '德国'), ('KR', '韩国'), ('JE', '泽西岛'), ('NZ', '新西兰'), ('MX', '墨西哥'), ('CA', '加拿大'), ('BR', '巴西'), ('CU', '古巴'), ('CZ', '捷克'), ('EG', '埃及'), ('FI', '芬兰'), ('GR', '希腊'), ('GU', '关岛'), ('IS', '冰岛'), ('MO', '澳门'), ('NL', '荷兰'), ('NO', '挪威'), ('PL', '波兰'), ('IT', '意大利'), ('IE', '爱尔兰'), ('AR', '阿根廷'), ('PT', '葡萄牙'), ('AU', '澳大利亚'), ('RU', '俄罗斯联邦'), ('CF', '中非共和国')], default='CN', max_length=5, verbose_name='国家')),
                ('used_traffic', models.BigIntegerField(default=0, verbose_name='已用流量')),
                ('total_traffic', models.BigIntegerField(default=1073741824, verbose_name='总流量')),
                ('enable', models.BooleanField(db_index=True, default=True, verbose_name='是否开启')),
                ('enlarge_scale', models.DecimalField(decimal_places=2, default=Decimal('1.0'), max_digits=10, verbose_name='倍率')),
                ('ehco_listen_host', models.CharField(blank=True, max_length=64, null=True, verbose_name='隧道监听地址')),
                ('ehco_listen_port', models.CharField(blank=True, max_length=64, null=True, verbose_name='隧道监听端口')),
                ('ehco_listen_type', models.CharField(choices=[('raw', 'raw'), ('wss', 'wss'), ('mwss', 'mwss')], default='raw', max_length=64, verbose_name='隧道监听类型')),
                ('ehco_transport_type', models.CharField(choices=[('raw', 'raw'), ('wss', 'wss'), ('mwss', 'mwss')], default='raw', max_length=64, verbose_name='隧道传输类型')),
                ('enable_ehco_lb', models.BooleanField(db_index=True, default=True, verbose_name='是否负载均衡')),
                ('server', models.CharField(max_length=128, verbose_name='服务器地址')),
                ('inbound_tag', models.CharField(default='proxy', max_length=64, verbose_name='标签')),
                ('service_port', models.IntegerField(default=443, verbose_name='服务端端口')),
                ('client_port', models.IntegerField(default=443, verbose_name='客户端端口')),
                ('listen_host', models.CharField(default='0.0.0.0', max_length=64, verbose_name='本地监听地址')),
                ('grpc_host', models.CharField(default='0.0.0.0', max_length=64, verbose_name='grpc地址')),
                ('grpc_port', models.CharField(default='8080', max_length=64, verbose_name='grpc端口')),
                ('network', models.CharField(default='tcp', max_length=64, verbose_name='连接方式')),
                ('security', models.CharField(blank=True, default='tls', max_length=64, null=True, verbose_name='加密方式')),
                ('alpn', models.CharField(blank=True, max_length=64, null=True, verbose_name='alpn')),
                ('certificateFile', models.CharField(blank=True, max_length=64, null=True, verbose_name='crt地址')),
                ('keyFile', models.CharField(blank=True, max_length=64, null=True, verbose_name='key地址')),
            ],
            options={
                'verbose_name_plural': 'Trojan节点',
            },
        ),
        migrations.AddField(
            model_name='relaynode',
            name='ehco_trojan_lb_port',
            field=models.IntegerField(blank=True, help_text='trojan负载均衡端口', null=True, verbose_name='trojan负载均衡端口'),
        ),
        migrations.AlterField(
            model_name='nodeonlinelog',
            name='node_type',
            field=models.CharField(choices=[('ss', 'ss'), ('vmess', 'vmess'), ('trojan', 'trojan')], default='ss', max_length=32, verbose_name='节点类型'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='usertrafficlog',
            name='node_type',
            field=models.CharField(choices=[('ss', 'ss'), ('vmess', 'vmess'), ('trojan', 'trojan')], default='ss', max_length=32, verbose_name='节点类型'),
        ),
        migrations.CreateModel(
            name='TrojanRelayRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relay_port', models.CharField(max_length=64, verbose_name='中转端口')),
                ('listen_type', models.CharField(choices=[('raw', 'raw'), ('wss', 'wss'), ('mwss', 'mwss')], default='raw', max_length=64, verbose_name='监听类型')),
                ('transport_type', models.CharField(choices=[('raw', 'raw'), ('wss', 'wss'), ('mwss', 'mwss')], default='raw', max_length=64, verbose_name='传输类型')),
                ('relay_node', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trojan_relay_rules', to='sspanel.relaynode', verbose_name='中转节点')),
                ('trojan_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relay_rules', to='sspanel.trojannode', verbose_name='Trojan节点')),
            ],
            options={
                'verbose_name_plural': 'Trojan转发规则',
            },
        ),
    ]
