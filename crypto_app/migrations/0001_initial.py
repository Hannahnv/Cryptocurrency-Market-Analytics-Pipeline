# Generated by Django 5.2 on 2025-05-06 03:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('coin_id', models.CharField(help_text='ID duy nhất của đồng tiền', max_length=100, primary_key=True, serialize=False)),
                ('rank', models.IntegerField(help_text='Thứ hạng của đồng tiền')),
                ('name', models.CharField(help_text='Tên đồng tiền', max_length=100)),
                ('symbol', models.CharField(help_text='Ký hiệu đồng tiền', max_length=50)),
                ('main_link', models.URLField(blank=True, help_text='Link chính của đồng tiền', null=True)),
                ('historical_link', models.URLField(blank=True, help_text='Link dữ liệu lịch sử', null=True)),
                ('ath', models.FloatField(blank=True, help_text='Giá cao nhất mọi thời đại', null=True)),
                ('atl', models.FloatField(blank=True, help_text='Giá thấp nhất mọi thời đại', null=True)),
                ('circulating_supply', models.CharField(blank=True, help_text='Số lượng tiền đang lưu hành', max_length=100, null=True)),
                ('total_supply', models.CharField(blank=True, help_text='Tổng số lượng tiền', max_length=100, null=True)),
                ('max_supply', models.CharField(blank=True, help_text='Số lượng tiền tối đa', max_length=100, null=True)),
                ('fully_diluted_mcap', models.BigIntegerField(blank=True, help_text='Vốn hóa thị trường hoàn toàn pha loãng', null=True)),
                ('dominance', models.FloatField(blank=True, help_text='Phần trăm thống trị thị trường', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GithubInfo',
            fields=[
                ('coin', models.OneToOneField(help_text='Đồng tiền liên quan', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='github_info', serialize=False, to='crypto_app.coin')),
                ('commits_count', models.FloatField(blank=True, help_text='Số lượng commits', null=True)),
                ('stars_count', models.FloatField(blank=True, help_text='Số lượng stars', null=True)),
                ('forks_count', models.FloatField(blank=True, help_text='Số lượng forks', null=True)),
                ('contributors_count', models.FloatField(blank=True, help_text='Số lượng contributors', null=True)),
                ('github_link', models.URLField(blank=True, help_text='Link GitHub của dự án', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(help_text='Ngày ghi nhận dữ liệu')),
                ('open', models.FloatField(help_text='Giá mở cửa')),
                ('high', models.FloatField(help_text='Giá cao nhất')),
                ('low', models.FloatField(help_text='Giá thấp nhất')),
                ('close', models.FloatField(help_text='Giá đóng cửa')),
                ('volume', models.BigIntegerField(help_text='Khối lượng giao dịch')),
                ('market_cap', models.BigIntegerField(help_text='Vốn hóa thị trường')),
                ('coin', models.ForeignKey(help_text='Đồng tiền liên quan', on_delete=django.db.models.deletion.CASCADE, related_name='historical_data', to='crypto_app.coin')),
            ],
            options={
                'ordering': ['-date'],
                'unique_together': {('coin', 'date')},
            },
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('language_name', models.CharField(help_text='Tên ngôn ngữ lập trình', max_length=50)),
                ('percentage', models.FloatField(help_text='Phần trăm sử dụng')),
                ('coin', models.ForeignKey(help_text='Đồng tiền liên quan', on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='crypto_app.coin')),
            ],
            options={
                'ordering': ['-percentage'],
                'unique_together': {('coin', 'language_name')},
            },
        ),
    ]
