# Cryptocurrency Market Analytics Pipeline

**Analysis of market trends and GitHub development activities of top 100 cryptocurrencies**

An end-to-end project from web scraping, data processing, data storage to data visualization.

## 📊 Project Overview

This project builds a comprehensive system to collect, manage, and analyze data from the **top 100 leading cryptocurrencies**. The system focuses on two main aspects:

- **Market data analysis**: prices, trading volumes, market capitalization
- **Development activity analysis**: data from GitHub repositories and programming languages

### 🎯 Main Objectives

- Automated data collection from CoinMarketCap and Github
- Build a structured database for information storage and management
- Create visual interfaces to observe trends and correlations in the crypto market

## 🏗️ Pipeline Architecture

![image](https://github.com/user-attachments/assets/8cc5640e-4e12-4853-8821-2c7e6af05637)

### Data Flow
1. **Web Scraping**: Collect data from [CoinMarketCap](https://coinmarketcap.com/) using Selenium + BeautifulSoup
2. **Data Processing**: Process and clean data using Python/Pandas
3. **Storage**: Import CSV to PostgreSQL through the Django web interface
4. **Visualization**: Create interactive dashboards with Tableau

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Web Scraping** | Python, Selenium, BeautifulSoup |
| **Data Processing** | Pandas, NumPy, Jupyter Notebooks |
| **Backend** | Django 4.x, Django ORM |
| **Database** | PostgreSQL |
| **Data Import** | Django Forms, CSV Processing |
| **Visualization** | Tableau |

## 📋 Project Structure

```
cryptocurrency/
├── cryptocurrency/              # Django project configuration
│   ├── settings.py             # Project settings & database config
│   ├── urls.py                 # URL routing
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
├── crypto_app/                 # Main Django application
│   ├── models.py               # Database models (Coin, HistoricalData, etc.)
│   ├── views.py                # View logic for CSV import
│   ├── forms.py                # CSV import forms
│   ├── urls.py                 # App URL patterns
│   ├── admin.py                # Django admin configuration
│   ├── templates/              # HTML templates
│   │   └── crypto_app/
│   │       ├── base.html       # Base template
│   │       └── import.html     # Data import interface
│   └── migrations/             # Database migrations
├── data/                       # Processed CSV datasets
│   ├── clean_coins_data.csv           # Top 100 crypto basic info
│   ├── clean_coins_historical_data.csv # 365 days price history
│   ├── github_coins_info.csv          # GitHub repository data
│   └── languages_data.csv             # Programming languages used
└── manage.py                   # Django management script
```

## 🔄 Data Collection Process
![image](https://github.com/user-attachments/assets/1d22db95-2a4f-45fc-ae35-ae7837f5afa0)

### Phase 1: Foundation Data Collection
- Scrape basic information of **top 100 cryptocurrencies** from CoinMarketCap
- Generate `Coin_id` and links for subsequent collection steps

### Phase 2: Historical Data Mining
- Collect price and trading volume data for **last 365 days** from 26/03/2024 to 24/03/2025
- Handle cases where new coins have less than 365 days of data

### Phase 3: GitHub Information Collection
- Search and extract GitHub repository information
- Collect commits, contributors, forks, stars count

### Phase 4: Programming Language Analysis
- Extract detailed information about programming languages used
- Scrape usage percentage of each language per project

## 🚀 Installation and Usage

### Prerequisites
- Python 3.12+
- PostgreSQL 12+
- Git

### Installation
```bash
# Clone repository
git clone https://github.com/yourusername/cryptocurrency-market-analytics-pipeline.git
cd cryptocurrency-market-analytics-pipeline

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install django psycopg2-binary pandas numpy selenium beautifulsoup4

# Configure database in cryptocurrency/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cryptocurrency_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

### Using Django Interface

1. **Access**: `http://localhost:8000/`
2. **Import data**:
   - Select data type (Cryptocurrency Information, Historical Data, GitHub Information, Programming Languages)
   - Upload the corresponding CSV file from `data/` folder
   - Click "Import Data"

  ![image](https://github.com/user-attachments/assets/7c35a11b-353b-44d5-9849-b71ea17cbb35)

3. **Monitor**: View database statistics

## 📊 Tableau Dashboards
Here is a preview of the interactive dashboard:

![image](https://github.com/user-attachments/assets/df700348-943b-4f0f-a3da-723013e397d1)


**🔗 View Live Dashboards**: [Tableau Public](https://public.tableau.com/app/profile/hang.nguyen6427/viz/CryptocurrencyAnalytics)


## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

⭐ **Found this project helpful?** Don't forget to give it a star on Github and share with the crypto community!
