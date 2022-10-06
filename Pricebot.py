#this bot is an example that provides BTC price from the BSC API.
from bscscan import BscScan
import telepot,pprint,time,telepot.loop

bsc = BscScan("") # BSC API Inside quotes
token = "" # Mr. Botfather
bot = telepot.Bot(token)

def handle(msg):
	pprint.pprint(msg)
	cid = msg["from"]["id"]
	text = msg["text"]
	
	if text.startswith("/start"):
		bot.sendMessage(cid,"Press /btc ")
	elif text.startswith("/btc"):
		
		btc = int(bsc.get_acc_balance_by_token_contract_address(contract_address="0x7130d2A12B9BCbFAe4f2634d864A1Ee1Ce3Ead9c",address="0x61eb789d75a95caa3ff50ed7e47b96c132fec082"))
		
		wbnbs = int(bsc.get_acc_balance_by_token_contract_address(contract_address="0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",address="0x61eb789d75a95caa3ff50ed7e47b96c132fec082"))
		
		wbnbs1 = int(bsc.get_acc_balance_by_token_contract_address(contract_address="0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",address="0x1B96B92314C44b159149f7E0303511fB2Fc4774f"))
		
		busds = int(bsc.get_acc_balance_by_token_contract_address(contract_address="0xe9e7cea3dedca5984780bafc599bd69add087d56",address="0x1B96B92314C44b159149f7E0303511fB2Fc4774f"))
		
		divide = 1000000000000000000
		
		x = (wbnbs/btc)*(busds/wbnbs1)
		btcu = round(x,4)
		
		y = wbnbs/btc
		btcb = round(y,6)
		
		z = btc/wbnbs1
		bnbt = round(z,6)
		
		a = btc/divide
		tpool = round(a,6)
		
		b = wbnbs/divide
		bnbpool = round(b,6)
		
		c = (wbnbs / btc) * (busds / wbnbs) * 200000000
		mkc = round(c,6)
		
		line = f"<b>✅ Current Price Of $btc</b>\n\n▪️<b>1 btc =</b> {btcu} $\n▪️<b>1 btc =</b> {btcb} BNB\n▪️<b>1 BNB =</b> {bnbt} btc\n\n♦️ <b>Pool Size : </b>\n         - {tpool} btc \n         - {bnbpool} BNB\n\n💎 <b>MarketCap : </b> {mkc} $"
		
		bot.sendMessage(cid,lineq,parse_mode='HTML')

telepot.loop.MessageLoop(bot,handle).run_as_thread()
while 1:
    time.sleep(60)