注意：
###请不要修改config.json、error.jpg、ok.jpg这三个文件###

使用方法：
1.插入PCAN后点击[Refresh]，HardWare更新为[PCAN_USBBUS1]
2.确认Baudrate是否正确
3.点击[Initialize]，确认CAN State是否OK
4.如CANOK，则选择ConfigFile，选择NGI2.0/K215等；如果CAN Fail，则检查连接是否正常
5.点击[OpenDriverDoor]，然后取消选中（模拟开关车门，唤醒整车网络）
6.必须在Run状态下才能切换档位信号

功能介绍：
Powerkey	：模拟钥匙位信号
Position	：模拟各个档位
OpenDriverDoor：模拟开关车门，选中开车门，未选择默认关车门
Speed		: 发送速度信号
Temp		：发送温度信号
Chime		：发送Chime
SWC			：SWC各功能按键
RVC			：RVC模块功能，具体包括以下内容：
	GL_Left	：导引线左偏
	GL_Right：导引线右偏
	Set_GL_Value:设置导引线值（-2048~2047.5）
	SetWarningicon：设置倒车警示符，三个Button对应Radio左中右三个位置
	SetText	：设置RVC时的Text显示

	
