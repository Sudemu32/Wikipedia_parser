BEFORE_PARSE_PAUSE = 20
EMAIL_ADDRESS = 'sudemu228@gmail.com'
EMAIL_PASSWORD = '***************'
RECIPIENT = 'EXAMPLE@MAIL.ru'

URLS = [
    "https://ru.wikipedia.org/wiki/Список_умерших_в_2025_году",
    "https://ru.wikipedia.org/wiki/Умершие_в_ноябре_2025_года",
    "https://ru.wikipedia.org/wiki/Умершие_в_октябре_2025_года",
    "https://ru.wikipedia.org/wiki/Умершие_в_сентябре_2025_года",
    "https://ru.wikipedia.org/wiki/Умершие_в_августе_2025_года",
    "https://ru.wikipedia.org/wiki/Умершие_в_июле_2025_года",
    "https://ru.wikipedia.org/wiki/Умершие_в_июне_2025_года",
    "https://ru.wikipedia.org/wiki/Умершие_в_мае_2025_года",
    "https://ru.wikipedia.org/wiki/Умершие_в_апреле_2025_года",
    "https://ru.wikipedia.org/wiki/Умершие_в_марте_2025_года",
    "https://ru.wikipedia.org/wiki/Умершие_в_феврале_2025_года",
    "https://ru.wikipedia.org/wiki/Умершие_в_январе_2025_года"   
]
HEADERS = [
    {
        'User-Agent': 'MyWikiResearchBot/1.0 (https://myproject.org; contact@example.com)',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br'
    },
    
    
    {
        'User-Agent': 'WikiTextParser/2.1 (data-fetching; contact@example.com)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate'
    },
    
    
    {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br'
    },
    
    
    {
        'User-Agent': 'AcademicStudy-LinguisticsDept/3.0 (Professor Smith; research-paper-2024; contact@university.edu)',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en',
        'Accept-Encoding': 'gzip, deflate',
        'From': 'research-assistant@university.edu'  
    },
    
    
    {
        'User-Agent': 'SlowWikiCrawler/0.5 (1 req/sec; +https://mywikiarchive.org/policy)',
        'Accept': 'application/json',
        'Accept-Language': '*',
        'Accept-Encoding': 'gzip'
    },
    
    
    {
        'User-Agent': 'PublicLibraryArchive/1.0 (info@publiclibrary.org)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate',
        'X-Forwarded-For': 'anonymous'  
    },
    
    
    {
        'User-Agent': 'CompressionTestClient/1.0',
        'Accept': '*/*',
        'Accept-Encoding': 'br, gzip, deflate',
        'Accept-Language': 'en'
    },
    
    
    {
        'User-Agent': 'MyCoolApp/4.2 (https://mycoolapp.com/docs; developer@mycoolapp.com)',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br'
    },
    
    
    {
        'User-Agent': 'MediaWikiResourceChecker/1.0 (sysadmin@example.net)',
        'Accept': 'image/webp,image/*,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en'
    },
]
