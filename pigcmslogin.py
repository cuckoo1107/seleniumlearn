+#coding:utf-8
+#第一步导入webdriver模块
+from selenium import webdriver
+import time
+
+#第二步打开浏览器
+pigcms = webdriver.Chrome()
+#第三部打开访问的网址
+pigcms.get("http://k.pigcms.com.cn/cashier/merchants.php")
+pigcms.find_element_by_xpath("//*[@id='form']/div[2]/input").send_keys("kdemo")
+pigcms.find_element_by_xpath("//*[@id='form']/div[3]/input").send_keys("kdemo111222")
+time.sleep(3)
+pigcms.find_element_by_xpath("//*[@id='form']/button").click()
+time.sleep(3)
+pigcms.find_element_by_xpath("//*[@id='subscribeModel']/div[1]/div/div[1]/a").click()