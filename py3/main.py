#!/usr/bin/python3
#coding=utf-8
import Iciba

if __name__ == '__main__':
    # 微信配置
    wechat_config = {
        'appid': 'wxd080fcf6fbb11238', #(No.1)此处填写公众号的appid
        'appsecret': '784ecc2664e7380934d31e7d379de679', #(No.2)此处填写公众号的appsecret
        'template_id': 'HH4q0sLx6jOqQAkX_xL4lyv7sGCtgTHCyN9S1Z_hJH8' #(No.3)此处填写公众号的模板消息ID
    }
    
    # 用户列表
    openids = [
        'osAs16LdD45GsuzRYlSQn5QrLe6w', #CC (No.4)此处填写你的微信号（微信公众平台上的微信号）
		'osAs16J8W9eiFPoe26lpqI0SMiMM', #hoo
		'osAs16E9kkuXRXuGuxWHuW25oyS8', #xl
        #'xxxxx', #如果有多个用户也可以
        #'xxxxx',
    ]

    # 执行
    icb = Iciba.iciba(wechat_config)

    '''
    run()方法可以传入openids列表，也可不传参数
    不传参数则对微信公众号的所有用户进行群发
    '''
    icb.run()




