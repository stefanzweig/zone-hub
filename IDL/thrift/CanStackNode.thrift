// Version = 1.0.20220131
include "CommonNode.thrift"



service canStackNode {
	CommonNode.result checkAlive ()
	// 获取版本
	CommonNode.version getVersion ()
	// 配置CAN协议栈
	CommonNode.result setConfigs (1: canChannelConfigs req)
	// 启动CAN协议栈
	CommonNode.result startCanStack ()
	// 停止CAN协议栈
	CommonNode.result stopCanStack ()
	// 清空定时CAN Message 发送列表
	CommonNode.result clearSend ()
	// 配置 CRC 和 RC
	CommonNode.result setCrcRcConfig (1: frameCrcRcConfig req)
	// 清除 CRC 和 RC的配置
	CommonNode.result clearCrcRcConfig (1: frameCrcRcConfig req)
	// 清除所有的 CRC 和 RC配置
	CommonNode.result clearAllCrcRcConfig ()
	// CAN message发送相关函数
	//CommonNode.result sendCanMessageCycList (1: canMessages req)
	CommonNode.result sendCanMessageCyc (1: canMessage req)

	CommonNode.result sendCanMessage (1: canMessage req)

	CommonNode.result sendCanMessages (1: canMessages req, 2: i32 stmin)
	// 获取当前协议栈状态
	CommonNode.result getStackStatus ()
	//停止某一条channel仿真的报文
	CommonNode.result stopChannelSendCyc (1: channel req)

	CommonNode.result sendCan (1: canMessage req)
	// 总线负载率相关函数
	busload getChannelBusloadCurrent (1: channel req)

	busload getChannelBusloadMax (1: channel req)

	busload getChannelBusloadAvg (1: channel req)

	errorFrameTotal getChannelErrorFrameTotal (1: channel req)
}
struct canChannelConfig {
	/**
	   int32
	   	通道index
	*/
	1: i32 channel
	/**
	   int32
	   	通道头波特率
	*/
	2: i32 bitrate
	/**
	   int32
	   	是否为FD，1为FD,0为普通can
	*/
	3: bool isFd
	/**
	   int32
	   	通道数据场波特率
	*/
	4: i32 fdBitrate
	/**
	   string
	   	支持的硬件类型字符串，目前支持vector,pcan,busmust
	*/
	5: string busType
	/**
	   string
	   	vector应用的名字
	*/
	6: string appName
	/**
	   int32
	   	同步跳转宽度，报文头
	*/
	7: i32 sjwAbr = 20
	/**
	   int32
	   	同步跳转宽度，数据场
	*/
	8: i32 sjwDbr = 5
	/**
	   int32
	   	位时间段1，报文头
	*/
	9: i32 tseg1Abr = 59
	/**
	   int32
	   	位时间段1，数据场
	*/
	10: i32 tseg1Dbr = 14
	/**
	   int32
	   	位时间段2，报文头
	*/
	11: i32 tseg2Abr = 20
	/**
	   int32
	   	位时间段2，数据场
	*/
	12: i32 tseg2Dbr = 5
	/**
	   int32
	   	是否接收自己发送的报文
	*/
	13: i32 txreceipts = 1
	/**
	   int32
	   	采样点
	*/
	14: i16 nsamplepos = 75
	/**
	   int32
	   	采样点
	*/
	15: i16 dsamplepos = 75
	/**
	   int32
	   	时钟频率
	*/
	16: i16 clockfreq = 80
	/**
	   int32
	   	波特率分频器
	*/
	17: i16 dprescaler = 2
	/**
	   int32
	   	波特率分频器
	*/
	18: i16 nprescaler = 2
	/**
	   int32
	   	硬件通道的名字，字符串
	*/
	19: string hardwareChannel = ""
}

struct canChannelConfigs {
	/**
	   list[canChannelConfig]
	   	多条CAN通道列表
	*/
	1: list<canChannelConfig> configs
}

struct frameCrcRcConfig {
	/**
	   int32
	   	软件通道信息
	*/
	1: i32 channel
	/**
	   int32
	   	报文ID信息
	*/
	2: i32 arbitrationId 
	/**
	   int32
	   	crc信号起始位置
	*/
	3: i32 crcBitStarts 
	/**
	   int32
	   	rc信号起始位置
	*/
	4: i32 rcBitStarts 
	/**
	   list[int32]
	   	需要使用的CRC table
	*/
	5: optional list<i32> crcTable // CRC 的 table
	/**
	   list[int32]
	   	配置rc最小最大值步长，例如[1,14,2],rc最小值1，最大值14，步长为2
	*/
	6: optional list<i32> rcConfig // RC 的 config
	/**
	   int32
	   	报文的周期
	*/
	7: optional i32 period // Frame 的 period
}
struct timer {
	/**
	   int64
	   	自定义定时器的时间
	*/
	1: i64 timerCycleTime //定时器事件周期
}
struct channel {
	/**
	   int32
	   	can通道信息
	*/
	1: i32 channel //CAN通道
}
struct busload {
	/**
	   int64
	   	can通道负载
	*/
	1: double busload
}
struct busloadAll {
	/**
	   list[int64]
	   	所有can通道负载
	*/
	1: list<double> busload
}
struct errorFrameTotal {
	/**
	   int64
	   	所有can通道错误帧
	*/
	1: i32 errorFrameTotal
}

struct canMessage {
	/**
	   int32
	   	can报文通道信息
	*/
	1: i32 channel
	/**
	   int32
	   	can报文是否是FD
	*/
	2: optional i32 isFd
	/**
	   int32
	   	can报文ID
	*/
	3: optional i32 id
	/**
	   int32
	   	can报文DLC
	*/
	4: optional i32 dlc
	/**
	   int32
	   	can报文是否为扩展帧
	*/
	5: optional i32 isExtended
	/**
	   int32
	   	can报文是否为远程帧
	*/
	6: optional i32 isRemote
	/**
	   list[int32]
	   	can报文数据信息
	*/
	7: list<i32> data
	/**
	   int32
	   	can报文周期信息
	*/
    8: i32 period
	/**
	   string
	   	can报文名字，可选
	*/
    9: optional string frameName
	/**
	   int32
	   	can报文发送次数
	*/
    10: optional i32 times
	/**
	   string
	   	can报文信号字典转化成字符串，可选
	*/
	11: optional string context
}

struct canMessages {
	/**
	   list[canMessage]
	   	多天can报文集合
	*/
	1: list<canMessage> canMessage
}

