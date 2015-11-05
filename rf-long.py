import datetime
set_universe(['000001.XSHE'])

def filter_stocks(start):
    init_time_string = '-'.join([str(start.year), str(start.month), str(start.day)]) 
    df = get_fundamentals(query(
        income.code, income.total_operating_revenue, income.total_profit
    ), date = init_time_string)
    
    new_time_string = '-'.join([str(start.year - 1), str(start.month), str(start.day)]) 
    compare_df = get_fundamentals(query(
        income.code, income.total_operating_revenue, income.total_profit
    ), date = new_time_string)
    
    log.info(df[0:10])
    log.info('changed')
    
    df['total_operating_revenue'] = (df['total_operating_revenue'] - compare_df['total_operating_revenue']) / compare_df['total_operating_revenue']
    df['total_profit'] = (df['total_profit'] - compare_df['total_profit']) / compare_df['total_operating_revenue']
    
    log.info(df[0:10])
    
    return df

def screen(date):
    filter_stocks(date)
    
    
prevMonth = 0

# 每个单位时间(如果按天回测,则每天调用一次,如果按分钟,则每分钟调用一次)调用一次
def handle_data(context, data):
    global prevMonth
    curDate = context.current_dt
    
    if (prevMonth == 10 and curDate.month == 11) or (prevMonth == 4 and curDate.month == 5):
        screen(curDate)
        
    if curDate.month != prevMonth:
        prevMonth = curDate.month
    
    pass
    
