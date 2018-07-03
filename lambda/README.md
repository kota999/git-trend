# Lib Download
    git clone https://github.com/jkehler/awslambda-psycopg2
    # And compile by following pages
    pip install sqlalchemy dataset -t .

# Lambda event
    {
        "category": "all languages", # get language name
        "timescale": "monthly", # crawling span
        "connectioin": "postgresql://localhost:5432/postgres",
        "table_name": "github_trend"
    }
