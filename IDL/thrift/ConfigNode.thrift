include "Common.thrift"



service configNode {
	hardwareInfos getHardwareInfo (1: hardwareType req)
	canCluster sendCanArxml (1: dbPath req)
	Common.result sendCanConfig (1: canConfigInfo req)
	Common.result sendLinConfig (1: Common.linChannelConfigs req)
	Common.result sendEthConfig (1: ethConfigInfo req)
}
struct hardwareType {
	1: list<i32> type
}
struct channelInfo {
	1: string type //CAN LIN Eth
	2: list<string> name //e.g. VN1640A 0 channel 1
}
struct hardwareInfo {
	1: string hardwareType
	2: list<channelInfo> channel
}
struct hardwareInfos {
	1: list<hardwareInfo> hardware
}
struct dbPath {
	1: string dbPath
}
struct canCluster {
	1: list<string> cluster
}
struct canChannelInfo {
	1: i32 softwareChannel
	2: string hardwareChannel
	3: string databaseChannel //数据库通道名称
	4: i32 canType //0:can,1:canfd
	5: i32 arbBitrate
	6: i32 dataBitrate
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
}
struct canConfigInfo {
	1: list<canChannelInfo> canConfigChannelInfo
}
// struct linChannelInfo {
// 	1: i32 softwareChannel
// 	2: string hardwareChannel
// 	3: string databaseChannel // 数据库路径
// 	4: i32 isMaster = 0
// 	5: i32 bitrate = 19200
// 	6: i32 deviceId = 0x0
//     7: i64 combaudrate = 19200
//     8: i32 major_version = 2
//     9: i32 minor_version = 1
//     10: i32 txreceipts = 1
//     11: list<i8> DLC = []

// }
// struct linConfigInfo {
// 	1: list<Common.linChannelInfo> linConfigChannelInfo
// }
struct ethConfigInfo {
	1: string ip
	2: string name
	3: list<string> database //数据库路径
}
