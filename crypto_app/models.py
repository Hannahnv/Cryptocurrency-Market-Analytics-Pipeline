from django.db import models

# Create your models here.
# crypto_app/models.py

class Coin(models.Model):
    """Model đại diện cho thông tin cơ bản của tiền điện tử"""
    # Sử dụng coin_id làm khóa chính
    coin_id = models.CharField(max_length=100, primary_key=True, help_text="ID duy nhất của đồng tiền")
    
    # Thông tin cơ bản
    rank = models.IntegerField(help_text="Thứ hạng của đồng tiền")
    name = models.CharField(max_length=100, help_text="Tên đồng tiền")
    symbol = models.CharField(max_length=50, help_text="Ký hiệu đồng tiền")
    
    # Links
    main_link = models.URLField(null=True, blank=True, help_text="Link chính của đồng tiền")
    historical_link = models.URLField(null=True, blank=True, help_text="Link dữ liệu lịch sử")
    
    # Dữ liệu giá
    ath = models.FloatField(null=True, blank=True, help_text="Giá cao nhất mọi thời đại")
    atl = models.FloatField(null=True, blank=True, help_text="Giá thấp nhất mọi thời đại")
    
    # Thông tin nguồn cung
    circulating_supply = models.CharField(max_length=100, null=True, blank=True, 
                                        help_text="Số lượng tiền đang lưu hành")
    total_supply = models.CharField(max_length=100, null=True, blank=True, 
                                   help_text="Tổng số lượng tiền")
    max_supply = models.CharField(max_length=100, null=True, blank=True, 
                                 help_text="Số lượng tiền tối đa")
    
    # Thông tin thị trường
    fully_diluted_mcap = models.BigIntegerField(null=True, blank=True, 
                                              help_text="Vốn hóa thị trường hoàn toàn pha loãng")
    dominance = models.FloatField(null=True, blank=True, 
                                help_text="Phần trăm thống trị thị trường")
    
    def __str__(self):
        return f"{self.name} ({self.symbol})"

class HistoricalData(models.Model):
    """Model đại diện cho dữ liệu lịch sử giá của tiền điện tử"""
    id = models.AutoField(primary_key=True)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='historical_data',
                            help_text="Đồng tiền liên quan")
    date = models.DateField(help_text="Ngày ghi nhận dữ liệu")
    open = models.FloatField(help_text="Giá mở cửa")
    high = models.FloatField(help_text="Giá cao nhất")
    low = models.FloatField(help_text="Giá thấp nhất")
    close = models.FloatField(help_text="Giá đóng cửa")
    volume = models.BigIntegerField(help_text="Khối lượng giao dịch")
    market_cap = models.BigIntegerField(help_text="Vốn hóa thị trường")
    
    class Meta:
        unique_together = ('coin', 'date')
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.coin.name} - {self.date}"

class GithubInfo(models.Model):
    """Model đại diện cho thông tin GitHub của dự án tiền điện tử"""
    coin = models.OneToOneField(Coin, on_delete=models.CASCADE, primary_key=True, 
                              related_name='github_info', help_text="Đồng tiền liên quan")
    commits_count = models.FloatField(null=True, blank=True, help_text="Số lượng commits")
    stars_count = models.FloatField(null=True, blank=True, help_text="Số lượng stars")
    forks_count = models.FloatField(null=True, blank=True, help_text="Số lượng forks")
    contributors_count = models.FloatField(null=True, blank=True, help_text="Số lượng contributors")
    github_link = models.URLField(null=True, blank=True, help_text="Link GitHub của dự án")
    
    def __str__(self):
        return f"GitHub của {self.coin.name}"

class ProgrammingLanguage(models.Model):
    """Model đại diện cho ngôn ngữ lập trình được sử dụng trong dự án tiền điện tử"""
    id = models.AutoField(primary_key=True)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='languages',
                           help_text="Đồng tiền liên quan")
    language_name = models.CharField(max_length=50, help_text="Tên ngôn ngữ lập trình")
    percentage = models.FloatField(help_text="Phần trăm sử dụng")
    
    class Meta:
        unique_together = ('coin', 'language_name')
        ordering = ['-percentage']
    
    def __str__(self):
        return f"{self.language_name} ({self.coin.name})"