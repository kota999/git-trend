def lambda_handler(event, context):

    # TODO implement
    if event.get("connection") and event.get("table_name"):
        category, timescale = get_request_param(event)
        return query(event.get("connection"), event.get("table_name"), category, timescale)

    return None

def query(connection, table_name, category, timescale):
    import dataset
    sql = get_sql(table_name, category, timescale)
    db = dataset.connect(connection)
    a = db.query(sql)
    result = [item for item in a]
    return result

def get_sql(table_name, category, timescale):
    start_time, end_time = get_time_str(timescale)
    sql = "select * from %s "%(table_name)
    sql = sql + "where category='%s' and timescale='%s' and datetime>='%s' and datetime<='%s' "%(category, timescale, start_time, end_time)
    sql = sql + "order by stars desc;"
    return sql

def get_request_param(event):
    GITHUB_TRENDING_LANGS = ["all languages", "python", "unknown", "c", "c%23", "c++", "cuda", "dockerfile", "dart",
        "elixir", "erlang", "go", "graphql", "haskell", "java", "javascript", "julia",
        "jupyter-notebook", "llvm", "markdown", "numpy", "objective-c", "objective-c++",
        "powershell", "php", "r", "ruby", "rust", "scala", "shell", "swift", "vim-script"]
    GITHUB_TRENDING_TIME_SCALES = ["daily", "weekly", "monthly"]

    category = "all languages"
    if event.get("category") in GITHUB_TRENDING_LANGS:
        category = event.get("category")
    timescale = "daily"
    if event.get("timescale") in GITHUB_TRENDING_TIME_SCALES:
        timescale = event.get("timescale")
    return category, timescale

def get_time_str(timescale):
    import datetime
    end_time = datetime.datetime.now()
    if timescale == "daily":
        start_time = end_time - datetime.timedelta(days=1)
    elif timescale == "weekly":
        start_time = end_time - datetime.timedelta(weeks=1)
    elif timescale == "monthly":
        from dateutil.relativedelta import relativedelta
        start_time = end_time - relativedelta(months=1)
    end_time_str = "%04d-%02d-%02d %02d:%02d:%02d"%(end_time.year, end_time.month,
        end_time.day, end_time.hour, end_time.minute, end_time.second)
    start_time_str = "%04d-%02d-%02d %02d:%02d:%02d"%(start_time.year, start_time.month,
        start_time.day, start_time.hour, start_time.minute, start_time.second)
    return start_time_str, end_time_str



