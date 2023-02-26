from pathlib import Path

from ally import *
from ally.requests.post_order_preview import PostOrderPreviewRequest

if __name__ == "__main__":
     f_path = Path.home().joinpath('ally.txt')
     with open(f_path, 'r') as file:
          lines = file.readlines()
     lines = [line.strip() for line in lines]
     CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_SECRET, ACCOUNT_ID = lines
     ally = AllyAPI(OAUTH_SECRET, OAUTH_TOKEN, CONSUMER_KEY, response_format="json")

     print(ally.get_member_profile())
     print(ally.get_status())
     print(ally.get_quote("AAPL"))
     print(ally.get_quote(["AAPL", "MSFT", "XLNX", "NXPI"]))
     print(ally.news_search("AAPL"))
     print(ally.news_search(["AAPL", "MSFT", "XLNX", "NXPI"]))

     quote_request = QuotesRequest(symbols=['SND', 'PRU', 'HMC'])
     response = quote_request.execute(ally)
     print(response.get_raw_data())

     accounts_balances_request = AccountsBalancesRequest()
     accounts_balances_response = accounts_balances_request.execute(ally)
     print(accounts_balances_response.get_raw_data())

     new_order = Order(acct=ACCOUNT_ID, sym="VTI", qty=1, sec_typ="CS", side=1, typ=2, px=100.00, tm_in_force=1)
     post_preview_request = PostOrderPreviewRequest(ACCOUNT_ID, new_order)
     post_preview_response = post_preview_request.execute(ally)
     print(post_preview_response.get_raw_data())
