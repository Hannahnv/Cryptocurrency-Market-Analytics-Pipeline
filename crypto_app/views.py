from django.shortcuts import render

# Create your views here.
# crypto_app/views.py
import pandas as pd
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction

from .forms import CSVUploadForm
from .models import Coin, HistoricalData, GithubInfo, ProgrammingLanguage

def import_view(request):
    """View xử lý việc upload và import file CSV."""
    
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            csv_type = form.cleaned_data['csv_type']
            
            # Kiểm tra định dạng file
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'File phải có định dạng CSV')
                return redirect('import_view')
            
            try:
                # Đọc file CSV
                df = pd.read_csv(csv_file)
                
                # Xác định hàm import tương ứng với loại dữ liệu
                import_functions = {
                    'coins': import_coins,
                    'historical': import_historical,
                    'github': import_github,
                    'languages': import_languages
                }
                
                if csv_type in import_functions:
                    # Gọi hàm import tương ứng
                    records_count = import_functions[csv_type](df)
                    
                    # Hiển thị thông báo thành công
                    messages.success(
                        request, 
                        f'Đã nhập thành công {records_count} bản ghi từ file {csv_file.name}'
                    )
                else:
                    messages.error(request, f'Loại dữ liệu không hợp lệ: {csv_type}')
                
            except Exception as e:
                # Hiển thị thông báo lỗi
                messages.error(request, f'Lỗi khi nhập dữ liệu: {str(e)}')
            
            return redirect('import_view')
    else:
        form = CSVUploadForm()
    
    # Lấy số lượng bản ghi hiện có trong database để hiển thị
    stats = {
        'coins_count': Coin.objects.count(),
        'historical_count': HistoricalData.objects.count(),
        'github_count': GithubInfo.objects.count(),
        'languages_count': ProgrammingLanguage.objects.count(),
    }
    
    return render(request, 'crypto_app/import.html', {
        'form': form,
        'stats': stats
    })

@transaction.atomic
def import_coins(df):
    """Nhập dữ liệu coins từ DataFrame."""
    count = 0
    
    for _, row in df.iterrows():
        # Tạo hoặc cập nhật đối tượng Coin
        Coin.objects.update_or_create(
            coin_id=row['Coin_id'],
            defaults={
                'rank': row['Rank'],
                'name': row['Name'],
                'symbol': row['Symbol'],
                'main_link': row['Main_link'],
                'historical_link': row['Historical_link'],
                'ath': row['ATH'] if pd.notna(row['ATH']) else None,
                'atl': row['ATL'] if pd.notna(row['ATL']) else None,
                'circulating_supply': row['Circulating_Supply'],
                'total_supply': row['Total_Supply'],
                'max_supply': row['Max_Supply'],
                'fully_diluted_mcap': row['Fully_Diluted_Mcap'] if pd.notna(row['Fully_Diluted_Mcap']) else None,
                'dominance': row['Dominance%'] if pd.notna(row['Dominance%']) else None,
            }
        )
        count += 1
    
    return count

@transaction.atomic
def import_historical(df):
    """Nhập dữ liệu lịch sử từ DataFrame."""
    count = 0
    
    # Chuyển đổi chuỗi ngày thành đối tượng date
    df['Date'] = pd.to_datetime(df['Date']).dt.date
    
    for _, row in df.iterrows():
        try:
            # Tìm coin tương ứng
            coin = Coin.objects.get(coin_id=row['Coin_id'])
            
            # Tạo hoặc cập nhật dữ liệu lịch sử
            HistoricalData.objects.update_or_create(
                coin=coin,
                date=row['Date'],
                defaults={
                    'open': row['Open'],
                    'high': row['High'],
                    'low': row['Low'],
                    'close': row['Close'],
                    'volume': row['Volume'],
                    'market_cap': row['Market_cap']
                }
            )
            count += 1
            
        except Coin.DoesNotExist:
            # Bỏ qua nếu không tìm thấy coin
            continue
    
    return count

@transaction.atomic
def import_github(df):
    """Nhập dữ liệu GitHub từ DataFrame."""
    count = 0
    
    for _, row in df.iterrows():
        try:
            # Tìm coin tương ứng
            coin = Coin.objects.get(coin_id=row['Coin_id'])
            
            # Tạo hoặc cập nhật thông tin GitHub
            GithubInfo.objects.update_or_create(
                coin=coin,
                defaults={
                    'commits_count': row['Commits_count'] if pd.notna(row['Commits_count']) else None,
                    'stars_count': row['Stars_count'] if pd.notna(row['Stars_count']) else None,
                    'forks_count': row['Forks_count'] if pd.notna(row['Forks_count']) else None,
                    'contributors_count': row['Contributors_count'] if pd.notna(row['Contributors_count']) else None,
                    'github_link': row['Github_link'] if pd.notna(row['Github_link']) else None,
                }
            )
            count += 1
            
        except Coin.DoesNotExist:
            # Bỏ qua nếu không tìm thấy coin
            continue
    
    return count

@transaction.atomic
def import_languages(df):
    """Nhập dữ liệu ngôn ngữ lập trình từ DataFrame."""
    count = 0
    
    for _, row in df.iterrows():
        try:
            # Tìm coin tương ứng
            coin = Coin.objects.get(coin_id=row['Coin_id'])
            
            # Tạo hoặc cập nhật thông tin ngôn ngữ
            ProgrammingLanguage.objects.update_or_create(
                coin=coin,
                language_name=row['Languages_name'],
                defaults={
                    'percentage': row['Percentage']
                }
            )
            count += 1
            
        except Coin.DoesNotExist:
            # Bỏ qua nếu không tìm thấy coin
            continue
    
    return count