// Version = 1.0.20220131
include "Common.thrift"



service canStackNode {
	// 获取版本
	Common.version getVersion ()
	// 配置CAN协议栈
	Common.result setConfigs (1: canChannelConfigs req)
	// 启动CAN协议栈
	Common.result startCanStack ()
	// 停止CAN协议栈
	Common.result stopCanStack ()
	// 清空定时CAN Message 发送列表
	Common.result clearSend ()
	// 配置 CRC 和 RC
	Common.result setCrcRcConfig (1: frameCrcRcConfig req)
	// 清除 CRC 和 RC的配置
	Common.result clearCrcRcConfig (1: frameCrcRcConfig req)
	// 清除所有的 CRC 和 RC配置
	Common.result clearAllCrcRcConfig ()
	// CAN message发送相关函数
	Common.result sendCanMessageCycList (1: canMessages req)
	Common.result sendCanMessageCyc (1: canMessage req)
	Common.result sendCanMessage (1: canMessages req)

	// 设置crc报文定时器更新周期
	Common.result creatTimerEvent (1: timer req)
	// 获取当前协议栈状态
	Common.result getStackStatus ()
	//停止某一条channel仿真的报文
	Common.result stopChannelSendCyc (1: channel req)
	Common.result sendCan (1: canMessage req)
	// 总线负载率相关函数
	busload getChannelBusloadCurrent (1: channel req)
	busload getChannelBusloadMax (1: channel req)
	busload getChannelBusloadAvg (1: channel req)
	errorFrameTotal getChannelErrorFrameTotal (1: channel req)
}
struct canChannelConfig {
	1: i32 channel
	2: i32 bitrate
	3: bool isFd
	4: i32 fdBitrate
	5: string busType
	6: string appName
	7: i32 sjwAbr = 20
	8: i32 sjwDbr = 5
	9: i32 tseg1Abr = 59
	10: i32 tseg1Dbr = 14
	11: i32 tseg2Abr = 20
	12: i32 tseg2Dbr = 5
	13: i32 txreceipts = 1
	14: i16 nsamplepos = 75
	15: i16 dsamplepos = 75
	16: i16 clockfreq = 80
	17: i16 dprescaler = 2
	18: i16 nprescaler = 2
	19: string hardwareChannel = ""
}
struct canChannelConfigs {
	1: list<canChannelConfig> configs
}


// 这里 crcBitStarts与rcBitStarts是否需要定义为list？
struct frameCrcRcConfig {
	1: i32 channel // CAN 通道
	2: i32 arbitrationId // CAN 的仲裁 ID
	3: list<i32> crcBitStarts // CRC 的 byte
	4: list<i32> rcBitStarts // RC 的起始 bit
	5: optional list<i32> crcTable // CRC 的 table
	6: optional list<i32> rcConfig // RC 的 config
	7: optional i32 period // Frame 的 period
}
struct timer {
	1: i64 timerCycleTime //定时器事件周期
}
struct channel {
	1: i32 channel //CAN通道
}
struct busload {
	1: double busload
}
struct busloadAll {
	1: list<double> busload
}
struct errorFrameTotal {
	1: i32 errorFrameTotal
}
// 这一块是共性的，需要提取出来
struct canMessage {
	1: i32 channel
	2: optional i32 isFd
	3: optional i32 id
	4: optional i32 dlc
	5: optional i32 isExtended
	6: optional i32 isRemote
	7: list<i32> data
    8: i32 period
    9: optional string frameName
}

struct canMessages {
	1: list<canMessage> canMessage
}