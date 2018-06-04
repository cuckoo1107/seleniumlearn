#coding:utf-8
#第一步导入webdriver模块
from selenium import webdriver
import time

#第二步打开浏览器
pigcms = webdriver.Chrome()
#第三部打开访问的网址
pigcms.get("https://np.pigcms.com")
pigcms.find_element_by_xpath("//*[@id='form']/div[2]/input").send_keys("test1202")
pigcms.find_element_by_xpath("//*[@id='form']/div[3]/input").send_keys("m123456")
time.sleep(2)
pigcms.find_element_by_xpath("//*[@id='form']/button").click()
time.sleep(3)
pigcms.find_element_by_xpath("//*[@id='subscribeModel']/div[1]/div/div[1]/a").click()

time.sleep(3)

pigcms.find_element_by_xpath("//*[@id='side-menu']/li[5]/a/span").click()
time.sleep(1)
pigcms.find_element_by_xpath("//*[@id='side-menu']/li[5]/ul/li[1]/a/span").click()
time.sleep(3)


card_is = pigcms.find_element_by_xpath("//*[@id='page-wrapper']/div[2]/div[1]/ol/li[3]/strong").text
card_text = card_is.encode('utf8')
print("会员卡详情：{}".format(card_text))

if card_is:
    print("删除会员卡")
    pigcms.find_element_by_xpath("/// *[ @ id = 'cardDel'] / strong").click()

else:
    print("创建会员卡")


pigcms.find_element_by_xpath("//*[@id='cost_money_unit']").send_keys("10")

time.sleep(3)
pigcms.find_element_by_xpath("//*[@id='init_increase_bonus']").send_keys("1")

time.sleep(3)
pigcms.find_element_by_xpath("//*[@id='max_increase_bonus']").send_keys("50")

time.sleep(3)
pigcms.find_element_by_xpath("//*[@id='cost_bonus_unit']").send_keys("10")

time.sleep(3)
#积分抵扣条件
#积分抵扣订单满金额
#pigcms.find_element_by_xpath("//*[@id='least_money_to_use_bonus']").send_keys("100")
#time.sleep(3)
##积分抵扣最高可抵扣积分，折合金额
#pigcms.find_element_by_xpath("//*[@id='max_reduce_bonus']").send_keys("50")
#time.sleep(3)
#积分抵扣最高可抵扣订单额的百分比
#pigcms.find_element_by_xpath("//*[@id='percent']").send_keys("20")
#time.sleep(3)
#pigcms.find_element_by_xpath("//*[@id='percent']").send_keys("20")
#time.sleep(3)
#自定义值名称
#pigcms.find_element_by_xpath("//*[@id=‘exper_name’]").send_keys("经验值")
#time.sleep(3)
#消费送经验值
#pigcms.find_element_by_xpath("//*[@id='cost_bonus_exper']").send_keys("100")
#time.sleep(3)
#pigcms.find_element_by_xpath("//*[@id='increase_exper']").send_keys("10")
#time.sleep(3)
#激活送经验值
#pigcms.find_element_by_xpath("//*[@id='init_increase_exper']").send_keys("10")
#time.sleep(3)
# #充值送经验值
#pigcms.find_element_by_xpath("//*[@id='cost_bonus_valu']").send_keys("100")
#time.sleep(1)
#pigcms.find_element_by_xpath("//*[@id='increase_valu']").send_keys("10")

#充值须知
#time.sleep(1)
#pigcms.find_element_by_xpath("//*[@id='stored_guidelines']").send_keys("充值须知")
pigcms.find_element_by_xpath("//*[@id='js_edit_area']/div[3]/ul/li[2]/a").click()




time.sleep(5)
pigcms.find_element_by_xpath("//*[@id='page-wrapper']/div[1]/nav/ul/li[4]/a").click()