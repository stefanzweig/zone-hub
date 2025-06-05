include "Common.thrift"


service linParserNode {
	// 添加一个 DB 文件
	Common.result addDbfile (1: Common.filePath req)
	// 配置某个channel
	Common.result setChannelConfig (1: Common.linChannelConfigs req)
	Common.result setNodeSimulation (1: linNodeConfig req)
	Common.result setFrameSimulation (1: linFrameConfig req)
	Common.result setFrameData(1:linFrameData req)
	Common.result SetSignalData(1:linSignalData req)
	// 清空所有配置
	Common.result clear ()
	// 清除所有订阅
	Common.result clearSubscribe ()
	//清空所有dbfile
	Common.result clearDbfile ()
	// 获取状态
	linParserStatus getStatus ()
	linLdfJson getLdfJsonTree ()
	// 转换LinDb至python
	Common.result convertLinDbToPy (1: convertInput req)
	// 转换LinDb至json
	Common.result convertLinDbToJson (1: convertInput req)
	Common.result setCrcConfig (1: linCrcConfigParser req)
	Common.result clearCrcConfig (1: linCrcConfigParser req)
}
struct linNodeConfig {
	1: string nodeName
	2: i32 channel
	3: bool simu
}
struct linFrameConfig {
	1: i32 frameId
	2: string frameName
	3: i32 channel
	4: bool simu
}
struct linFrameData {
	1: i32 frameId
	2: string frameName
	3: i32 channel
	4: string setData
	5: string encodeType
}
struct linSignalData {
	1: string signalName
	2: i32 channel
	3: string setData
	4: string encodeType
}
// struct linChannelConfig {
// 	1: string ldfPath
// 	2: string linMode
// 	3: i32 txrecv
// 	4: i64 baudrate
// 	5: i32 linChannel
// 	6: i32 hardwareChannel
// 	7: i32 hardwareType
// }
// struct linChannelConfigs{
// 	1: list<Common.linChannelInfo> linconfigs
// }
struct linParserStatus {
	// 表达 LinParser 的状态
	// TODO 邢潇 根据实际情况调整
	1: Common.result result
	2: i32 status
	3: string strStatus
}
struct linLdfJson {
	1: i32 result
	2: string reasonbinary
	3: string jsonData
}
struct convertInput {
	1: string srcFile
	2: string dstFile
}
struct linCrcConfigParser {
	1: i32 channel
	2: i32 frameId
	3: string frameName
	4: string signalRcName
	5: string signalCrcName
	6: i32 rcMin
	7: i32 rcMax
	8: list<i32> crcTable
	9: i32 stepLen
}
