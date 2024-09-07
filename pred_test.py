from pprint import pprint
from uie_predictor import UIEPredictor

schema = ['出发地', '目的地', '费用', '时间']
# 设定抽取目标和定制化模型权重路径
my_ie = UIEPredictor(model='uie-base',schema=schema)
pprint(my_ie("城市内交通费7月5日金额114广州至佛山"))