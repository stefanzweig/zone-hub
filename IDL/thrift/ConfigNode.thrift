include "CommonNode.thrift"
include "SomeIpNode.thrift"



service configNode {
	hardwareInfos getHardwareInfo (1: hardwareType req)
	canCluster sendCanArxml (1: dbPath req)
	CommonNode.result sendCanConfig (1: canConfigInfo req)
	CommonNode.result sendLinConfig (1: CommonNode.linChannelConfigs req)
	CommonNode.result sendEthConfig (1: SomeIpNode.someipStackConfig req)
}
struct hardwareType {
	/**
	   list[int32]
	   	需要获取硬件品牌，vector 0x1;pcan 0x2;busmust 0x4;usbdevice 0x8;
	*/
	1: list<i32> type
}

struct channelInfo {
	/**
	   string
	   	获取硬件类型，如CAN LIN Eth
	*/
	1: string type 
	/**
	   list[string]
	   	获取到硬件名字列表，如 [e.g. VN1640A 0 channel 1]
	*/
	2: list<string> name 
}

struct hardwareInfo {
	/**
	   string
	   	获取硬件品牌名字，如Vector,PCAN,BUSMUST,USBDEVICE
	*/
	1: string hardwareType
	/**
	   list[channelInfo]
	   	该品牌硬件下所有通道信息
	*/
	2: list<channelInfo> channel
}
struct hardwareInfos {
	/**
	   list[hardwareInfo]
	   	获取到所有硬件信息
	*/
	1: list<hardwareInfo> hardware
}
struct dbPath {
	/**
	   string
	   	arxml路径信息
	*/
	1: string dbPath
}
struct canCluster {
	/**
	   list[string]
	   	解析完arxml后返回所有通道名字信息
	*/
	1: list<string> cluster
}
struct canChannelInfo {
	/**
	   int32
	   	can软件通道信息
	*/
	1: i32 softwareChannel
	/**
	   string
	   	can硬件通道信息，该值通过getHardwareInfo返回中获取
	*/
	2: string hardwareChannel
	/**
	   string
	   	该通道需要配置的数据库通道，比如BDCAN
	*/
	3: string databaseChannel 
	/**
	   int32
	   	can通道类型，0代表CAN； 1代表CANFD
	*/
	4: i32 canType
	/**
	   int32
	   	如果类型为CAN，该参数就是设置其波特率，如果类型为CANFD，该参数就是header波特率
	*/
	5: i32 arbBitrate
	/**
	   int32
	   	如果类型为CAN，该参数忽略，如果类型为CANFD，该参数就是数据域波特率
	*/
	6: i32 dataBitrate
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
}

struct canConfigInfo {
	/**
	   list[canChannelInfo]
	   	所有需要设置can通道信息的列表
	*/
	1: list<canChannelInfo> canConfigChannelInfo
}

// struct ethConfigInfo {
// 	/**
// 	   string
// 	   	以太网的IP
// 	*/
// 	1: string ip
// 	/**
// 	   string
// 	   	以太网的名字
// 	*/
// 	2: string name
// 	/**
// 	   list[string]
// 	   	所有arxml信息
// 	*/
// 	3: list<string> database 
// }
